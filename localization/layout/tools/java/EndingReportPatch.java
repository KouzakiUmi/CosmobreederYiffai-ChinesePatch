import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-only, exact Kr/Kc boundaries. Driver pins INPUT_SHA256 before parsing. */
public final class EndingReportPatch implements Opcodes {
    private EndingReportPatch() { }
    public static final Map<String,String> INPUT_SHA256;
    static {
        Map<String,String> pins = new LinkedHashMap<String,String>();
        pins.put("PRG/Kr", "99def910ad65c8fefc731b18ed6e62faf319790105bd41d261d68b14e09744b2");
        pins.put("PRG/Kc", "091ac03da5277ad71b4d8d063bbeafa98d5e6d9cfe7d9d99ba1ca83a5203af09");
        INPUT_SHA256 = Collections.unmodifiableMap(pins);
    }
    private static final String[] OWNERS = {"PRG/Kr","PRG/Kr","PRG/Kc","PRG/Kc"};
    private static final String[] NAMES = {"a","a","b","a"};
    private static final String[] DESCS = {
        "(Ljava/lang/String;IILPRG/SN;)V", "(Ljava/lang/String;IIZLPRG/SN;)V",
        "(LPRG/SN;ZI)V", "(ZLPRG/SN;IILPRG/aAJ;)V"
    };
    private static final String[] HASHES = {
        "05cb8fd88d3d6b8af089c3a5d498218edb594a1aeb99628b18d49148793258ea",
        "ccf66229eeb8912dd1e1699503ca460da44aa33ef3c18889e3c9151cfb9c09a2",
        "80f056c2a68645a2461557b2c1355b4ce254552f38864dea8f0ba2a62a7c531e",
        "17cfcf320458eee900fede4979357d71f83052a0471d4d8eda55a805afbbabd7"
    };
    private static final String ID = "(LPRG/SN;Ljava/lang/String;IILPRG/aBa;)V";
    private static final String FORMAT = "(Ljava/lang/String;LPRG/amq;LPRG/amv;Z)Ljava/lang/String;";
    private static final String PLAIN = "(Ljava/lang/String;IILjava/lang/String;)V";
    private static final String COLOUR = "(Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V";

    public static void apply(Map<String,ClassNode> classes) {
        List<MethodInsnNode> calls = new ArrayList<MethodInsnNode>();
        List<MethodInsnNode> replacements = new ArrayList<MethodInsnNode>();
        List<MethodNode> methods = new ArrayList<MethodNode>();
        for (int i=0;i<OWNERS.length;i++) {
            ClassNode c=classes.get(OWNERS[i]);
            if(c==null || !OWNERS[i].equals(c.name) || c.version!=V1_8) fail("class/version "+OWNERS[i]);
            MethodNode m=VsnPatch.method(c,NAMES[i],DESCS[i]);
            if(!m.tryCatchBlocks.isEmpty() || !HASHES[i].equals(VsnPatch.fingerprint(m))) fail("method fingerprint "+OWNERS[i]+DESCS[i]);
            int found=0;
            for(AbstractInsnNode n:m.instructions) if(n instanceof MethodInsnNode) {
                MethodInsnNode a=(MethodInsnNode)n; String helper=null, desc=null;
                if(i<2 && exact(a,INVOKEVIRTUAL,"PRG/Id","a",ID)) {
                    helper="draw";desc="(LPRG/Id;LPRG/SN;Ljava/lang/String;IILPRG/aBa;)V";
                } else if(i==2 && exact(a,INVOKEVIRTUAL,"PRG/amw","a",FORMAT)) {
                    helper="formatData";desc="(LPRG/amw;Ljava/lang/String;LPRG/amq;LPRG/amv;Z)Ljava/lang/String;";
                } else if(i==3 && exact(a,INVOKEINTERFACE,"PRG/SN","a",PLAIN)) {
                    helper="drawData";desc="(LPRG/SN;Ljava/lang/String;IILjava/lang/String;)V";
                } else if(i==3 && exact(a,INVOKEINTERFACE,"PRG/SN","a",COLOUR)) {
                    helper="drawData";desc="(LPRG/SN;Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V";
                }
                if(helper!=null) {found++;calls.add(a);methods.add(m);replacements.add(new MethodInsnNode(INVOKESTATIC,"PRG/EndingReportLayout",helper,desc,false));}
            }
            if(found!=(i==3?2:1)) fail("exact callsite count "+OWNERS[i]+DESCS[i]);
        }
        // All four methods passed preflight before the first mutation. Stack shapes
        // include the original receiver, preserving prior coordinates/colour/style.
        for(int i=0;i<calls.size();i++) methods.get(i).instructions.set(calls.get(i),replacements.get(i));
    }
    private static boolean exact(MethodInsnNode m,int op,String owner,String name,String desc) {
        return m.getOpcode()==op && owner.equals(m.owner) && name.equals(m.name) && desc.equals(m.desc)
            && m.itf==(op==INVOKEINTERFACE);
    }
    private static void fail(String why) {throw new IllegalStateException("Ending report patch refused: "+why);}
    private static String sha(byte[] bytes)throws Exception {
        StringBuilder s=new StringBuilder();for(byte b:MessageDigest.getInstance("SHA-256").digest(bytes))s.append(String.format("%02x",b&255));return s.toString();
    }
    /** Isolated overlay builder: input.jar output.jar. --fingerprints input.jar is read-only. */
    public static void main(String[] args)throws Exception {
        boolean print=args.length==2 && args[0].equals("--fingerprints");
        if(args.length!=2)throw new IllegalArgumentException("input.jar NEW-output.jar OR --fingerprints input.jar");
        Path source=Paths.get(args[print?1:0]).toRealPath();
        Map<String,ClassNode> nodes=new LinkedHashMap<String,ClassNode>();
        try(JarFile jar=new JarFile(source.toFile())) {
            for(Map.Entry<String,String> p:INPUT_SHA256.entrySet()) {
                byte[] bytes=jar.getInputStream(jar.getJarEntry(p.getKey()+".class")).readAllBytes();
                if(!p.getValue().equals(sha(bytes)))fail("raw SHA256 "+p.getKey());
                ClassNode n=new ClassNode(ASM8);new ClassReader(bytes).accept(n,ClassReader.EXPAND_FRAMES);nodes.put(p.getKey(),n);
            }
        }
        if(print) {for(int i=0;i<OWNERS.length;i++)System.out.println(i+"="+VsnPatch.fingerprint(VsnPatch.method(nodes.get(OWNERS[i]),NAMES[i],DESCS[i])));return;}
        Path output=Paths.get(args[1]).toAbsolutePath().normalize();
        Path root=Paths.get("localization/work/ending-report-r24").toAbsolutePath().normalize();
        if(!output.startsWith(root) || Files.exists(output) || output.equals(source))fail("new isolated output required");
        // Negative preflight: corrupt the final Kc method, prove Kr was not mutated.
        Map<String,ClassNode> bad=new LinkedHashMap<String,ClassNode>();
        for(Map.Entry<String,ClassNode> e:nodes.entrySet()) {ClassNode clone=new ClassNode(ASM8);e.getValue().accept(clone);bad.put(e.getKey(),clone);}
        VsnPatch.method(bad.get("PRG/Kc"),NAMES[3],DESCS[3]).instructions.insert(new InsnNode(NOP));
        String before=VsnPatch.fingerprint(VsnPatch.method(bad.get("PRG/Kr"),NAMES[0],DESCS[0]));
        boolean refused=false;try{apply(bad);}catch(IllegalStateException expected){refused=true;}
        if(!refused || !before.equals(VsnPatch.fingerprint(VsnPatch.method(bad.get("PRG/Kr"),NAMES[0],DESCS[0]))))throw new AssertionError("atomic negative preflight");
        apply(nodes);Files.createDirectories(output.getParent());
        try(final URLClassLoader hierarchy=new URLClassLoader(new URL[]{source.toUri().toURL()},EndingReportPatch.class.getClassLoader());
            JarOutputStream out=new JarOutputStream(Files.newOutputStream(output,StandardOpenOption.CREATE_NEW))) {
            for(Map.Entry<String,ClassNode> e:nodes.entrySet()) {
                ClassWriter w=new ClassWriter(ClassWriter.COMPUTE_FRAMES|ClassWriter.COMPUTE_MAXS){protected ClassLoader getClassLoader(){return hierarchy;}};
                e.getValue().accept(w);out.putNextEntry(new JarEntry(e.getKey()+".class"));out.write(w.toByteArray());out.closeEntry();
            }
        }
        System.out.println("PASS EndingReportPatch raw pins, four-method atomic preflight, exactly five callsites, frames/maxs; overlay only Kr/Kc");
    }
}
