import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-only isolated overlay, never modifies the source archive. */
public final class CompactFieldsTest {
    static String sha(byte[] b)throws Exception{StringBuilder s=new StringBuilder();for(byte x:MessageDigest.getInstance("SHA-256").digest(b))s.append(String.format("%02x",x&255));return s.toString();}
    static Map<String,ClassNode> load(JarFile z,Map<String,String> pins)throws Exception{
        Map<String,ClassNode> result=new LinkedHashMap<String,ClassNode>();
        for(Map.Entry<String,String> p:pins.entrySet()){
            byte[] b=z.getInputStream(z.getJarEntry(p.getKey()+".class")).readAllBytes();
            if(!sha(b).equals(p.getValue()))throw new AssertionError("pin "+p.getKey());
            ClassNode c=new ClassNode(Opcodes.ASM8);new ClassReader(b).accept(c,ClassReader.EXPAND_FRAMES);result.put(p.getKey(),c);
        }return result;
    }
    static Map<String,byte[]> methods(Map<String,ClassNode> nodes){Map<String,byte[]> r=new LinkedHashMap<String,byte[]>();for(ClassNode c:nodes.values())for(MethodNode m:c.methods){ClassWriter w=new ClassWriter(0);w.visit(52,1,"Probe",null,"java/lang/Object",null);m.accept(w);w.visitEnd();r.put(c.name+"."+m.name+m.desc,w.toByteArray());}return r;}
    public static void main(String[] a)throws Exception{
        Path source=Paths.get(a[0]),helpers=Paths.get(a[1]),output=Paths.get(a[2]);
        if(Files.exists(output))throw new AssertionError("new isolated overlay required");
        Map<String,ClassNode> nodes;Map<String,byte[]> before;
        try(JarFile z=new JarFile(source.toFile())){
            nodes=load(z,CompactFieldsPatch.INPUT_SHA256);nodes.putAll(load(z,ItemFont8Patch.R27_INPUT_SHA256));
            before=methods(nodes);
            // Late mismatches must leave all original methods untouched.
            Map<String,ClassNode> bad=load(z,CompactFieldsPatch.INPUT_SHA256);
            bad.get("PRG/Mn").methods.removeIf(m->m.name.equals("a")&&m.desc.equals("(LPRG/SN;LPRG/aab;)V"));
            Map<String,byte[]> snapshot=methods(bad);boolean rejected=false;
            try{CompactFieldsPatch.apply(bad);}catch(IllegalStateException expected){rejected=true;}
            if(!rejected)throw new AssertionError("preflight rejection");
            for(Map.Entry<String,byte[]> m:methods(bad).entrySet())if(!Arrays.equals(m.getValue(),snapshot.get(m.getKey())))throw new AssertionError("partial mutation");
        }
        CompactFieldsPatch.apply(nodes);ItemFont8Patch.applyR27(nodes);
        int changed=0;
        for(Map.Entry<String,byte[]> m:methods(nodes).entrySet())if(!Arrays.equals(m.getValue(),before.get(m.getKey()))){
            String key=m.getKey();boolean expected=key.equals("PRG/LY.b(LPRG/SN;)V")||key.equals("PRG/Mb.b(LPRG/SN;)V")||key.equals("PRG/Mn.b(LPRG/SN;)V")||key.equals("PRG/Mn.a(LPRG/SN;LPRG/aab;)V")||key.equals("PRG/Lb.a(F)V")||key.equals("PRG/Lg.a(F)V")||key.equals("PRG/Le.<init>(LPRG/apr;)V");
            if(!expected)throw new AssertionError("unrelated method changed "+key);changed++;
        }
        if(changed!=7)throw new AssertionError("exact seven target methods");
        boolean rejected=false;try{CompactFieldsPatch.apply(nodes);}catch(IllegalStateException expected){rejected=true;}if(!rejected)throw new AssertionError("double patch");
        try(JarOutputStream out=new JarOutputStream(Files.newOutputStream(output,StandardOpenOption.CREATE_NEW))){
            for(ClassNode c:nodes.values()){
                ClassWriter w=new ClassWriter(ClassWriter.COMPUTE_FRAMES|ClassWriter.COMPUTE_MAXS);c.accept(w);
                out.putNextEntry(new JarEntry(c.name+".class"));out.write(w.toByteArray());out.closeEntry();
            }
            for(String n:new String[]{"CompactFields","ItemFont8"}){
                out.putNextEntry(new JarEntry("PRG/"+n+".class"));out.write(Files.readAllBytes(helpers.resolve("PRG/"+n+".class")));out.closeEntry();
            }
        }
        System.out.println("COMPACT_PATCH_OK pins=6 changed_methods="+changed+" preflight_atomic=true double_patch_rejected=true overlay_sha256="+sha(Files.readAllBytes(output)));
    }
}
