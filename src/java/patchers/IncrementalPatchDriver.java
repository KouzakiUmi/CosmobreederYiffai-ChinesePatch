import java.net.URL;
import java.net.URLClassLoader;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.security.MessageDigest;
import java.lang.reflect.*;
import java.util.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-only r27 incremental patch driver. Never initializes any game class. */
public final class IncrementalPatchDriver {
    private static String sha(byte[] raw) throws Exception {
        StringBuilder value=new StringBuilder();for(byte b:MessageDigest.getInstance("SHA-256").digest(raw))value.append(String.format("%02x",b&255));return value.toString();
    }
    public static void main(String[] args) throws Exception {
        if(args.length!=5)throw new IllegalArgumentException("r27.jar helpers pins.tsv passes.tsv NEW-targets.jar");
        Path source=Paths.get(args[0]).toRealPath(), helpers=Paths.get(args[1]).toRealPath();
        Path output=Paths.get(args[4]).toAbsolutePath().normalize();
        if(Files.exists(output))throw new IllegalArgumentException("New output only");
        Map<String,ClassNode> nodes=new LinkedHashMap<String,ClassNode>();
        Set<String> seen=new HashSet<String>();
        try(JarFile jar=new JarFile(source.toFile())) {
            for(String row:Files.readAllLines(Paths.get(args[2]),StandardCharsets.UTF_8)) {
                if(row.isEmpty())continue;String[] fields=row.split("\t",-1);
                if(fields.length!=2||!fields[0].startsWith("PRG/")||!fields[1].matches("[a-f0-9]{64}"))throw new IllegalArgumentException("Invalid pin row");
                String name=fields[0];if(!seen.add(name))throw new IllegalArgumentException("Duplicate target "+name);
                JarEntry entry=jar.getJarEntry(name+".class");if(entry==null)throw new IllegalArgumentException("Missing target "+name);
                byte[] raw=jar.getInputStream(entry).readAllBytes();if(!sha(raw).equals(fields[1]))throw new IllegalArgumentException("Target SHA "+name);
                ClassNode node=new ClassNode();new ClassReader(raw).accept(node,ClassReader.EXPAND_FRAMES);nodes.put(name,node);
            }
        }
        // Every target is identity-checked before any patcher sees mutable nodes.
        for(String row:Files.readAllLines(Paths.get(args[3]),StandardCharsets.UTF_8)) {
            if(row.isEmpty())continue;String[] fields=row.split("\t",-1);
            if(fields.length!=2||!fields[0].matches("[A-Za-z_$][A-Za-z0-9_$]*")||!fields[1].matches("[A-Za-z_$][A-Za-z0-9_$]*"))throw new IllegalArgumentException("Invalid patch pass");
            try {Class.forName(fields[0]).getMethod(fields[1],Map.class).invoke(null,nodes);}
            catch(InvocationTargetException ex){Throwable cause=ex.getCause();if(cause instanceof Exception)throw(Exception)cause;throw new RuntimeException(cause);}
            System.out.println("PATCH_PASS_OK "+fields[0]+"."+fields[1]);
        }
        Map<String,byte[]> completed=new LinkedHashMap<String,byte[]>();
        try(final URLClassLoader loader=new URLClassLoader(new URL[]{helpers.toUri().toURL(),source.toUri().toURL()},IncrementalPatchDriver.class.getClassLoader())) {
            for(Map.Entry<String,ClassNode> entry:nodes.entrySet()) {
                ClassWriter writer=new ClassWriter(ClassWriter.COMPUTE_FRAMES|ClassWriter.COMPUTE_MAXS){
                    @Override protected ClassLoader getClassLoader(){return loader;}
                };
                entry.getValue().accept(writer);completed.put(entry.getKey()+".class",writer.toByteArray());
            }
        }
        // No archive output exists until all passes and frame recomputation succeed.
        try(JarOutputStream out=new JarOutputStream(Files.newOutputStream(output,StandardOpenOption.CREATE_NEW))) {
            for(Map.Entry<String,byte[]> entry:completed.entrySet()) {
                out.putNextEntry(new JarEntry(entry.getKey()));out.write(entry.getValue());out.closeEntry();
            }
        }
        System.out.println("INCREMENTAL_TARGETS_OK count="+completed.size());
    }
}
