import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.zip.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-time only. No game main, static initializer, installation or save IO. */
public final class LayoutPatcher {
    private static String sha(byte[] bytes) throws Exception {
        byte[] hash = MessageDigest.getInstance("SHA-256").digest(bytes);
        StringBuilder out = new StringBuilder();
        for (byte value : hash) out.append(String.format("%02x", value & 255));
        return out.toString();
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 4)
            throw new IllegalArgumentException("input.jar new-output-dir pins.properties Patch1,Patch2");
        Path output = Paths.get(args[1]).toAbsolutePath().normalize();
        if (Files.exists(output)) throw new IllegalArgumentException("Refuse output overwrite");
        Properties pins = new Properties();
        try (InputStream input = Files.newInputStream(Paths.get(args[2]))) { pins.load(input); }
        Map<String, ClassNode> nodes = new TreeMap<>();
        Map<String, byte[]> originals = new TreeMap<>();
        try (ZipFile jar = new ZipFile(args[0])) {
            for (String name : new TreeSet<>(pins.stringPropertyNames())) {
                ZipEntry entry = jar.getEntry(name + ".class");
                if (entry == null) throw new IllegalArgumentException("Missing target " + name);
                byte[] original;
                try (InputStream input = jar.getInputStream(entry)) { original = input.readAllBytes(); }
                if (!sha(original).equals(pins.getProperty(name)))
                    throw new IllegalArgumentException("Original target identity mismatch: " + name);
                ClassNode node = new ClassNode(Opcodes.ASM8);
                new ClassReader(original).accept(node, ClassReader.EXPAND_FRAMES);
                if (!node.name.equals(name)) throw new IllegalArgumentException("Class name mismatch");
                nodes.put(name, node);
                originals.put(name, original);
            }
        }
        Set<String> targetSet = new TreeSet<>(nodes.keySet());
        for (String patch : args[3].split(","))
            Class.forName(patch).getMethod("apply", Map.class).invoke(null, nodes);
        if (!targetSet.equals(nodes.keySet()))
            throw new IllegalArgumentException("Patch changed the declared class set");
        Map<String, byte[]> generated = new TreeMap<>();
        List<String> report = new ArrayList<>();
        for (Map.Entry<String, ClassNode> entry : nodes.entrySet()) {
            // The driver classpath contains the pinned original game archive and
            // helper classes; frame hierarchy lookup does not initialize classes.
            ClassWriter writer = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS) {
                @Override protected ClassLoader getClassLoader() {
                    // Internal ASM itself is bootstrap-loaded. Its default null
                    // loader cannot resolve the application/game archive.
                    return LayoutPatcher.class.getClassLoader();
                }
            };
            entry.getValue().accept(writer);
            byte[] value = writer.toByteArray();
            new ClassReader(value); // structural parse before publishing any class
            generated.put(entry.getKey(), value);
            report.add(entry.getKey() + "\t" + sha(originals.get(entry.getKey())) + "\t" + sha(value));
        }
        Files.createDirectory(output);
        for (Map.Entry<String, byte[]> entry : generated.entrySet()) {
            Path target = output.resolve(entry.getKey() + ".class");
            Files.createDirectories(target.getParent());
            Files.write(target, entry.getValue(), StandardOpenOption.CREATE_NEW);
        }
        Files.write(output.resolve("patch-summary.tsv"), report, StandardCharsets.UTF_8,
                StandardOpenOption.CREATE_NEW);
        System.out.println("PATCHED " + generated.size() + " pinned classes");
    }
}
