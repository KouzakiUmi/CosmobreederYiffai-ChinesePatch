import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** r27 increment only. Raw SHA gates are mandatory in the driver; apply also
 * checks the complete canonical class tree, exact method descriptors/calls. */
public final class SceneTextPatch implements Opcodes {
    public static final Map<String,String> INPUT_SHA256;
    private static final Map<String,String> TREE_SHA256;
    static {
        Map<String,String> raw=new LinkedHashMap<String,String>();
        raw.put("PRG/Ew","4034ebb934633cf4c074b8489ede4ba08bc025d63cf03c02fe18111b86df51f6");
        raw.put("PRG/Jm","e6ae7a07e1e9a5a0d59a8413a9deeef30a57b3536377c4ae0c8ec0bb51d48fa5");
        raw.put("PRG/kn","06ecd40ba83236fa72f012091e13e6ef985926db2943e2016316702f4a76e53e");
        raw.put("PRG/Lx","3affe2e2e0fb378c85e6749fc81d487d8b2b48699d90748a3b0d6030a060d300");
        raw.put("PRG/Po","9120a3493600e030737bca3eae89aee55b590869cda28d4f9e92c3446bac0050");
        raw.put("PRG/Kc","2f407f1f6c3e4e7dda3f3f47a8a3445f3047b5be87f35d1b775aa559c76a0eb2");
        INPUT_SHA256=Collections.unmodifiableMap(raw);
        Map<String,String> tree=new LinkedHashMap<String,String>();
        tree.put("PRG/Ew","6169d6e930d425e231d85cbc122fdb8ac48bdee9c707478207b383e011b73a5d"); tree.put("PRG/Jm","ddf56f8936be2c5a38054fc19ae4a78a50c1380989b7e6db7f048971fd9ee931");
        tree.put("PRG/kn","b86fccbe262b3b97b4d2de794f2bc175445e5ca2b39e7257f24b9cf5a94035f1"); tree.put("PRG/Lx","652f8c03496a70a7b741181880e28b4c4109ec28ec97ad41acfa7fb8f3266f60"); tree.put("PRG/Po","b2f053d99444928c756fd3566b96f9909912c3ecac9f8837d4471033a462faff");
        tree.put("PRG/Kc","ce22996b267e670a339b57215998dcf4fc20cc4c4b904c8ee351cb5572b91336");
        TREE_SHA256=Collections.unmodifiableMap(tree);
    }
    private static final String FORMAT="(Ljava/lang/String;LPRG/amq;LPRG/amv;Z)Ljava/lang/String;";
    private static final String PLAIN="(Ljava/lang/String;IILjava/lang/String;)V";
    private static MethodNode method(ClassNode c,String name,String desc) {
        MethodNode found=null;
        for(MethodNode m:c.methods) if(m.name.equals(name)&&m.desc.equals(desc)) {
            if(found!=null) fail("duplicate method"); found=m;
        }
        if(found==null)fail("missing method "+c.name+name+desc);
        return found;
    }
    private static String sha(byte[] b) {
        try {StringBuilder s=new StringBuilder();for(byte x:MessageDigest.getInstance("SHA-256").digest(b))s.append(String.format("%02x",x&255));return s.toString();}
        catch(Exception e){throw new IllegalStateException(e);}
    }
    private static String treeHash(ClassNode c){ClassWriter w=new ClassWriter(0);c.accept(w);return sha(w.toByteArray());}
    private static void fail(String why){throw new IllegalStateException("SceneTextPatch refused: "+why);}
    private static final class Change {
        final MethodNode m; final MethodInsnNode n; final String helper,desc; final int sn;
        Change(MethodNode m,MethodInsnNode n,String h,String d,int s){this.m=m;this.n=n;helper=h;desc=d;sn=s;}
        void apply(){if(sn>=0)m.instructions.insertBefore(n,new VarInsnNode(ALOAD,sn));m.instructions.set(n,new MethodInsnNode(INVOKESTATIC,"PRG/SceneText",helper,desc,false));}
    }
    private static void calls(List<Change> changes,ClassNode c,String name,String desc,
                              int opcode,String owner,String called,String callDesc,
                              int expected,String helper,int extraSn,int... selected) {
        MethodNode m=method(c,name,desc);int count=0,chosen=0;
        for(AbstractInsnNode node:m.instructions) if(node instanceof MethodInsnNode) {
            MethodInsnNode n=(MethodInsnNode)node;
            if(n.getOpcode()==opcode&&n.owner.equals(owner)&&n.name.equals(called)&&n.desc.equals(callDesc)&&n.itf==(opcode==INVOKEINTERFACE)) {
                boolean use=selected.length==0;for(int k:selected)if(k==count)use=true;
                if(use){String replacement="(L"+owner+";"+callDesc.substring(1);
                    if(extraSn>=0)replacement=replacement.replace(")", "LPRG/SN;)");
                    changes.add(new Change(m,n,helper,replacement,extraSn));chosen++;}
                count++;
            }
        }
        if(count!=expected || chosen!=(selected.length==0?expected:selected.length))fail("unique callsites "+c.name+name+desc+" expected="+expected+" actual="+count);
    }
    public static void apply(Map<String,ClassNode> classes) {
        for(String key:INPUT_SHA256.keySet()) {
            ClassNode c=classes.get(key);
            if(c==null||!key.equals(c.name)||c.version!=V1_8||!TREE_SHA256.get(key).equals(treeHash(c)))fail("whole class identity "+key);
        }
        List<Change> out=new ArrayList<Change>();
        ClassNode c=classes.get("PRG/Ew");
        calls(out,c,"a","(LPRG/SN;Z)V",INVOKEVIRTUAL,"PRG/amw","a",FORMAT,2,"breedAffinity",1,0);
        calls(out,c,"a","(LPRG/SN;Z)V",INVOKEVIRTUAL,"PRG/amw","a",FORMAT,2,"breedNeeds",1,1);
        calls(out,c,"a","(LPRG/SN;Z)V",INVOKEINTERFACE,"PRG/SN","a",PLAIN,4,"breedDraw",-1,2,3);
        calls(out,c,"a","(LPRG/SN;ILPRG/aAJ;)V",INVOKEINTERFACE,"PRG/SN","a",PLAIN,1,"breedDraw",-1);
        c=classes.get("PRG/Jm");
        calls(out,c,"a","(LPRG/Jm;LPRG/SN;LPRG/At;)V",INVOKEVIRTUAL,"PRG/amw","a",FORMAT,2,"cardFormat",-1);
        calls(out,c,"a","(LPRG/Jm;LPRG/SN;LPRG/At;)V",INVOKEINTERFACE,"PRG/SN","a",PLAIN,1,"cardDraw",-1);
        calls(out,c,"a","(LPRG/Jm;LPRG/SN;ILPRG/aAJ;)V",INVOKEINTERFACE,"PRG/SN","a",PLAIN,1,"cardDraw",-1);
        c=classes.get("PRG/kn");
        calls(out,c,"a","(Ljava/lang/String;LPRG/SH;LPRG/km;LPRG/SN;D)V",INVOKEVIRTUAL,"PRG/amw","a",FORMAT,1,"achievementFormat",-1);
        calls(out,c,"a","(LPRG/km;LPRG/SN;LPRG/aAJ;)V",INVOKEINTERFACE,"PRG/SN","a",PLAIN,1,"achievementDraw",-1);
        calls(out,c,"a","(LPRG/ka;LPRG/SH;LPRG/SN;D)V",INVOKEINTERFACE,"PRG/SN","a","(Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V",1,"achievementDraw",-1);
        c=classes.get("PRG/Lx");
        calls(out,c,"a","(LPRG/SN;Z)V",INVOKEINTERFACE,"PRG/SN","a","(Ljava/lang/String;ILjava/lang/String;)I",1,"mapCenter",-1);
        c=classes.get("PRG/Po");
        calls(out,c,"a","(LPRG/apr;LPRG/SH;LPRG/SN;I)V",INVOKEINTERFACE,"PRG/SN","a",PLAIN,1,"mapDraw",-1);
        calls(out,classes.get("PRG/Kc"),"a","(LPRG/Kc;LPRG/Ke$a;LPRG/SN;LPRG/SL;IILjava/lang/String;)V",
            INVOKEINTERFACE,"PRG/SN","a",PLAIN,1,"dataName",-1);
        MethodNode book=method(classes.get("PRG/Kc"),"b","(LPRG/SN;ZI)V");
        VarInsnNode source=null;
        int sourceStores=0;
        for(AbstractInsnNode n:book.instructions)if(n instanceof VarInsnNode&&n.getOpcode()==ASTORE&&((VarInsnNode)n).var==9){source=(VarInsnNode)n;sourceStores++;}
        if(sourceStores!=1 || !book.tryCatchBlocks.isEmpty())fail("Kc unique full-source local9");
        // Preflight ALL identities, descriptors and ordinal call counts before mutation.
        for(Change change:out)change.apply();
        // Preserve Kc's original selected-entry/source resolution and 3/4-row y
        // selection, replace ONLY the known lossy format/zip tail.
        AbstractInsnNode next=source.getNext();
        while(next!=null){AbstractInsnNode after=next.getNext();book.instructions.remove(next);next=after;}
        book.localVariables=null;
        book.instructions.add(new VarInsnNode(ALOAD,1));book.instructions.add(new VarInsnNode(ALOAD,9));
        book.instructions.add(new VarInsnNode(ILOAD,2));book.instructions.add(new VarInsnNode(ILOAD,4));
        book.instructions.add(new VarInsnNode(ILOAD,6));book.instructions.add(new VarInsnNode(ILOAD,3));
        book.instructions.add(new MethodInsnNode(INVOKESTATIC,"PRG/SceneText","dataBlock","(LPRG/SN;Ljava/lang/String;ZIII)V",false));
        book.instructions.add(new InsnNode(RETURN));
    }
    public static void main(String[] args)throws Exception {
        boolean print=args.length==2&&args[0].equals("--fingerprints");
        if(args.length!=2)throw new IllegalArgumentException("--fingerprints r27.jar OR r27.jar NEW-overlay.jar");
        Path input=Paths.get(args[print?1:0]).toRealPath();
        Map<String,ClassNode> nodes=new LinkedHashMap<String,ClassNode>();
        try(JarFile jar=new JarFile(input.toFile())) {
            for(String key:INPUT_SHA256.keySet()) {
                byte[] raw=jar.getInputStream(jar.getJarEntry(key+".class")).readAllBytes();
                ClassNode c=new ClassNode(ASM8);new ClassReader(raw).accept(c,ClassReader.EXPAND_FRAMES);nodes.put(key,c);
                if(print)System.out.println(key+" raw="+sha(raw)+" tree="+treeHash(c));
                else if(!sha(raw).equals(INPUT_SHA256.get(key)))fail("raw class SHA "+key);
            }
        }
        if(print)return;
        Path output=Paths.get(args[1]).toAbsolutePath().normalize();
        Path root=Paths.get("localization/optimization/r28/scenes").toAbsolutePath().normalize();
        if(!output.startsWith(root)||Files.exists(output)||output.equals(input))fail("new scene overlay only");
        apply(nodes);
        Files.createDirectories(output.getParent());
        try(JarOutputStream jar=new JarOutputStream(Files.newOutputStream(output,StandardOpenOption.CREATE_NEW))) {
            for(Map.Entry<String,ClassNode> e:nodes.entrySet()) {
                ClassWriter w=new ClassWriter(ClassWriter.COMPUTE_MAXS);e.getValue().accept(w);
                jar.putNextEntry(new JarEntry(e.getKey()+".class"));jar.write(w.toByteArray());jar.closeEntry();
            }
        }
        System.out.println("PASS SceneTextPatch: six raw/tree identities; 14 exact callsites plus unique Kc full-source tail; atomic preflight; overlay only");
    }
}
