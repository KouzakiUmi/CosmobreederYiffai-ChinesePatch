import java.net.URL;
import java.net.URLClassLoader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import java.util.jar.JarOutputStream;
import jdk.internal.org.objectweb.asm.ClassReader;
import jdk.internal.org.objectweb.asm.ClassWriter;
import jdk.internal.org.objectweb.asm.tree.ClassNode;

/** Build-only ASM driver. Resolves frame hierarchy without initializing game classes. */
public final class DialogueBuild {
    private static String hash(byte[] bytes) throws Exception {
        StringBuilder out = new StringBuilder();
        for (byte b : MessageDigest.getInstance("SHA-256").digest(bytes)) out.append(String.format("%02x", b & 255));
        return out.toString();
    }
    public static void main(String[] args) throws Exception {
        Path source = Paths.get(args[0]).toRealPath();
        Path helpers = Paths.get(args[1]).toRealPath();
        Path output = Paths.get(args[2]).toAbsolutePath().normalize();
        if (Files.exists(output)) throw new IllegalArgumentException("Target output exists");
        Map<String, String> pins = new LinkedHashMap<String, String>();
        pins.put("PRG/JR", "89bc9f39fc7227f0407afa626b8f816099f7b0f0e9c0a3e43abc719378c680c9");
        pins.put("PRG/Nb", "147d037fe7553457eb1ce10310b74ca6ffa42cfeac1e78d068d0ffbc594bbb92");
        Map<String, ClassNode> classes = new LinkedHashMap<String, ClassNode>();
        try (JarFile jar = new JarFile(source.toFile())) {
            for (Map.Entry<String, String> pin : pins.entrySet()) {
                byte[] bytes = jar.getInputStream(jar.getJarEntry(pin.getKey() + ".class")).readAllBytes();
                if (!hash(bytes).equals(pin.getValue())) throw new IllegalArgumentException("Input class SHA: " + pin.getKey());
                ClassNode node = new ClassNode();
                new ClassReader(bytes).accept(node, ClassReader.EXPAND_FRAMES);
                classes.put(pin.getKey(), node);
            }
        }
        DialoguePatch.apply(classes);
        try (final URLClassLoader loader = new URLClassLoader(new URL[] {helpers.toUri().toURL(), source.toUri().toURL()},
                DialogueBuild.class.getClassLoader());
             JarOutputStream out = new JarOutputStream(Files.newOutputStream(output))) {
            for (Map.Entry<String, ClassNode> entry : classes.entrySet()) {
                ClassWriter writer = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS) {
                    @Override protected ClassLoader getClassLoader() { return loader; }
                };
                entry.getValue().accept(writer);
                out.putNextEntry(new JarEntry(entry.getKey() + ".class"));
                out.write(writer.toByteArray()); out.closeEntry();
            }
        }
        System.out.println("DIALOGUE_TARGETS_WRITTEN " + classes.size());
    }
}
