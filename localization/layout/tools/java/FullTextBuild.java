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

/** Build-only complete text fix, resolving frames without class initialization. */
public final class FullTextBuild {
    private static String sha(byte[] data) throws Exception {
        StringBuilder b=new StringBuilder();
        for(byte v:MessageDigest.getInstance("SHA-256").digest(data))b.append(String.format("%02x",v&255));
        return b.toString();
    }
    private static void add(Map<String,String> all,Map<String,String> more) {
        for(Map.Entry<String,String> e:more.entrySet()) {
            String previous=all.put(e.getKey(),e.getValue());
            if(previous!=null&&!previous.equals(e.getValue()))throw new IllegalArgumentException("Contradictory pin");
        }
    }
    public static void main(String[] args) throws Exception {
        Path source=Paths.get(args[0]).toRealPath(),helpers=Paths.get(args[1]).toRealPath();
        Path output=Paths.get(args[2]).toAbsolutePath().normalize();
        if(Files.exists(output))throw new IllegalArgumentException("Output exists");
        Map<String,String> pins=new LinkedHashMap<String,String>();
        add(pins,DialoguePatch.INPUT_SHA256);add(pins,SubtitlePatch.INPUT_SHA256);
        add(pins,ItemFont8Patch.INPUT_SHA256);add(pins,EndingReportPatch.INPUT_SHA256);add(pins,StoryFont12Patch.INPUT_SHA256);
        pins.put("PRG/Yg","dc6c7964df17ba744ab0397d9a01be3ac97c711954c876d6b72a6d606a1d3859");
        Map<String,ClassNode> nodes=new LinkedHashMap<String,ClassNode>();
        try(JarFile jar=new JarFile(source.toFile())) {
            for(Map.Entry<String,String> e:pins.entrySet()) {
                byte[] bytes=jar.getInputStream(jar.getJarEntry(e.getKey()+".class")).readAllBytes();
                if(!sha(bytes).equals(e.getValue()))throw new IllegalArgumentException("Source SHA: "+e.getKey());
                ClassNode n=new ClassNode();new ClassReader(bytes).accept(n,ClassReader.EXPAND_FRAMES);nodes.put(e.getKey(),n);
            }
        }
        // No archive is opened until every exact source identity and every patch passes.
        BridgePatch.apply(nodes);DialoguePatch.apply(nodes);SubtitlePatch.apply(nodes);ItemFont8Patch.apply(nodes);EndingReportPatch.apply(nodes);StoryFont12Patch.apply(nodes);
        try(final URLClassLoader loader=new URLClassLoader(new URL[]{helpers.toUri().toURL(),source.toUri().toURL()},FullTextBuild.class.getClassLoader());
            JarOutputStream out=new JarOutputStream(Files.newOutputStream(output))) {
            for(Map.Entry<String,ClassNode> e:nodes.entrySet()) {
                ClassWriter cw=new ClassWriter(ClassWriter.COMPUTE_FRAMES|ClassWriter.COMPUTE_MAXS) {
                    @Override protected ClassLoader getClassLoader(){return loader;}
                };
                e.getValue().accept(cw);out.putNextEntry(new JarEntry(e.getKey()+".class"));out.write(cw.toByteArray());out.closeEntry();
            }
        }
        System.out.println("FULL_TEXT_TARGETS_WRITTEN "+nodes.keySet());
    }
}
