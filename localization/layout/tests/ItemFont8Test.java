import PRG.*;
import cosmoloc.layout.FontAccess;
import java.io.*;
import java.lang.reflect.*;
import java.net.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** CPU only: real pinned Lg/Lb/Le consumer bytecode, actual classic FNT parser,
 * recording SN. No game entry point, texture construction, GL, installation/save IO.
 * JDK17: original.jar helper-dir runtime-dir new-patched-test.jar
 * Original bundled JRE: --cpu patched-test.jar runtime-dir (test JAR first on classpath).
 */
public final class ItemFont8Test implements Opcodes {
    private static int assertions;
    private static void check(boolean value, String message) {
        assertions++; if (!value) throw new AssertionError(message);
    }
    private static String hash(byte[] bytes) throws Exception {
        StringBuilder out = new StringBuilder();
        for (byte b : MessageDigest.getInstance("SHA-256").digest(bytes)) out.append(String.format("%02x", b & 255));
        return out.toString();
    }
    private static MethodNode method(ClassNode c, String name, String desc) {
        for (MethodNode m : c.methods) if (m.name.equals(name) && m.desc.equals(desc)) return m;
        throw new AssertionError(c.name + name + desc);
    }
    private static byte[] methodBytes(MethodNode m) {
        ClassWriter w = new ClassWriter(0); w.visit(V1_8, ACC_PUBLIC, "Probe", null, "java/lang/Object", null);
        m.accept(w); w.visitEnd(); return w.toByteArray();
    }
    private static Map<String,ClassNode> load(Path jar) throws Exception {
        Map<String,ClassNode> result = new TreeMap<String,ClassNode>();
        try (JarFile z = new JarFile(jar.toFile())) {
            for (Map.Entry<String,String> pin : ItemFont8Patch.INPUT_SHA256.entrySet()) {
                byte[] bytes = bytes(z.getInputStream(z.getJarEntry(pin.getKey() + ".class")));
                check(hash(bytes).equals(pin.getValue()), "real input SHA " + pin.getKey());
                ClassNode node = new ClassNode(ASM8); new ClassReader(bytes).accept(node, ClassReader.EXPAND_FRAMES);
                result.put(pin.getKey(), node);
            }
        }
        return result;
    }
    private static byte[] bytes(InputStream input) throws IOException {
        try (InputStream in = input; ByteArrayOutputStream out = new ByteArrayOutputStream()) {
            byte[] buffer = new byte[8192]; int count;
            while ((count = in.read(buffer)) >= 0) out.write(buffer, 0, count);
            return out.toByteArray();
        }
    }
    private static int calls(MethodNode m, String owner, String name) {
        int count = 0;
        for (AbstractInsnNode n : m.instructions.toArray()) if (n instanceof MethodInsnNode) {
            MethodInsnNode c = (MethodInsnNode)n; if (c.owner.equals(owner) && c.name.equals(name)) count++;
        }
        return count;
    }
    private static boolean target(ClassNode c, MethodNode m) {
        return (c.name.equals("PRG/Le") && m.name.equals("<init>"))
                || (!c.name.equals("PRG/Le") && m.name.equals("b") && m.desc.equals("(LPRG/SN;)V"));
    }
    private static byte[] probe() {
        ClassWriter w = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS);
        w.visit(V1_8, ACC_PUBLIC, "PRG/ItemFont8LeProbe", null, "PRG/Le", null);
        w.visitField(ACC_PUBLIC, "selected", "LPRG/azK;", null, null).visitEnd();
        w.visitField(ACC_PUBLIC, "equipment", "LPRG/azK;", null, null).visitEnd();
        w.visitField(ACC_PUBLIC, "equipped", "Z", null, null).visitEnd();
        MethodVisitor m = w.visitMethod(ACC_PUBLIC, "G", "()Z", null, null);
        m.visitCode(); m.visitInsn(ICONST_1); m.visitInsn(IRETURN); m.visitMaxs(0,0); m.visitEnd();
        for (String name : new String[] {"P", "O"}) {
            m = w.visitMethod(ACC_PUBLIC, name, "()LPRG/azK;", null, null); m.visitCode();
            m.visitVarInsn(ALOAD,0); m.visitFieldInsn(GETFIELD,"PRG/ItemFont8LeProbe",name.equals("P")?"selected":"equipment","LPRG/azK;");
            m.visitInsn(ARETURN); m.visitMaxs(0,0); m.visitEnd();
        }
        m = w.visitMethod(ACC_PUBLIC,"a","(LPRG/aga;)Z",null,null); m.visitCode();
        m.visitVarInsn(ALOAD,0); m.visitFieldInsn(GETFIELD,"PRG/ItemFont8LeProbe","equipped","Z");
        m.visitInsn(IRETURN); m.visitMaxs(0,0); m.visitEnd(); w.visitEnd(); return w.toByteArray();
    }
    private static void patch(Path source, Path helpers, Path output) throws Exception {
        check(!Files.exists(output), "test JAR must be new");
        Map<String,ClassNode> nodes = load(source);
        Map<String,byte[]> unchanged = new TreeMap<String,byte[]>();
        for (ClassNode c : nodes.values()) for (MethodNode m : c.methods)
            if (!target(c,m)) unchanged.put(c.name + m.name + m.desc, methodBytes(m));
        ItemFont8Patch.apply(nodes);
        for (ClassNode c : nodes.values()) for (MethodNode m : c.methods) {
            byte[] old = unchanged.get(c.name + m.name + m.desc);
            if (old != null) check(Arrays.equals(old, methodBytes(m)), "unrelated method preserved " + c.name + m.name + m.desc);
        }
        MethodNode ctor = method(nodes.get("PRG/Le"),"<init>","(LPRG/apr;)V");
        check(calls(ctor,"PRG/ItemFont8","registerName") == 1, "one selected name, not category Lg");
        check(calls(ctor,"PRG/ItemFont8","registerDescription") == 1, "one selected description");
        check(calls(method(nodes.get("PRG/Le"),"b","(LPRG/Le;)Ljava/lang/String;"),"PRG/ItemFont8","drawName") == 0,
                "equipment and blink source method completely intact");
        boolean rejected = false;
        try { ItemFont8Patch.apply(nodes); } catch (IllegalStateException expected) { rejected = true; }
        check(rejected,"double patch refused");
        // A late Lb mismatch must not mutate Le/Lg first.
        Map<String,ClassNode> wrong = load(source);
        MethodNode desc = method(wrong.get("PRG/Lb"),"b","(LPRG/SN;)V");
        for (AbstractInsnNode n : desc.instructions.toArray()) if (n instanceof MethodInsnNode && ((MethodInsnNode)n).owner.equals("PRG/amw"))
            ((MethodInsnNode)n).name = "bad";
        byte[] before = methodBytes(method(wrong.get("PRG/Le"),"<init>","(LPRG/apr;)V"));
        rejected = false;
        try { ItemFont8Patch.apply(wrong); } catch (IllegalStateException expected) { rejected = true; }
        check(rejected && Arrays.equals(before,methodBytes(method(wrong.get("PRG/Le"),"<init>","(LPRG/apr;)V"))),"all preflight before mutate");
        try (JarOutputStream out = new JarOutputStream(Files.newOutputStream(output,StandardOpenOption.CREATE_NEW))) {
            for (ClassNode c : nodes.values()) {
                ClassWriter w = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS) {
                    @Override protected ClassLoader getClassLoader() { return ItemFont8Test.class.getClassLoader(); }
                };
                c.accept(w); put(out,c.name + ".class",w.toByteArray());
            }
            try (DirectoryStream<Path> stream = Files.newDirectoryStream(helpers.resolve("PRG"),"*.class")) {
                for (Path p : stream) if (p.getFileName().toString().startsWith("ItemFont8") || p.getFileName().toString().startsWith("LayoutBridge"))
                    put(out,"PRG/" + p.getFileName(),Files.readAllBytes(p));
            }
            put(out,"PRG/ItemFont8LeProbe.class",probe());
        }
    }
    private static void put(JarOutputStream out,String name,byte[] data) throws IOException {
        out.putNextEntry(new JarEntry(name)); out.write(data); out.closeEntry();
    }
    /** Real FNT reader, no texture path is consumed. */
    public static final class CpuFile extends aqX {
        CpuFile(Path path) { super(); this.a = path.toFile(); }
        @Override public InputStream e() { try { return new FileInputStream(a); } catch (IOException e) { throw new RuntimeException(e); } }
        @Override public aqX d() { return new CpuFile(a.toPath().toAbsolutePath().getParent()); }
        @Override public aqX b(String child) { return new CpuFile(a.toPath().resolve(child)); }
    }
    public static final class CpuFont extends arp {
        public final arp.a metrics;
        CpuFont(Path fnt) { this(new arp.a(new CpuFile(fnt), false)); }
        CpuFont(arp.a data) { super(data, new arI(), false); metrics = data; }
        @Override protected void a(arp.a data) { /* no texture/glyph UV upload in CPU test */ }
    }
    private static Object supplier(final Object value, final int[] count) {
        return java.lang.reflect.Proxy.newProxyInstance(ItemFont8Test.class.getClassLoader(), new Class<?>[] {azy.class},
            (proxy,m,args) -> {
                if (m.getName().startsWith("apply")) { if (count != null) count[0]++; return value; }
                if (m.getName().equals("toString")) return "CPU supplier";
                return null;
            });
    }
    private static Object allocate(Class<?> type) throws Exception {
        Class<?> unsafe = Class.forName("sun.misc.Unsafe"); Field field = unsafe.getDeclaredField("theUnsafe"); field.setAccessible(true);
        return unsafe.getMethod("allocateInstance",Class.class).invoke(field.get(null),type);
    }
    private static void cpu(Path jar, Path runtime) throws Exception {
        final CpuFont classic = new CpuFont(runtime.resolve("classic.fnt")), body = new CpuFont(runtime.resolve("bbc2-10px.fnt"));
        // Match iF.a(Yh): classic.setFixedWidthGlyphs for original ASCII32..126.
        StringBuilder fixed = new StringBuilder(); for(int cp=32;cp<127;cp++) fixed.append((char)cp);
        classic.a(fixed);
        check(classic.metrics.a('A').n && classic.metrics.a('A').l==8,"actual iF classic fixed-width setup retained");
        check(hash(Files.readAllBytes(runtime.resolve("classic.fnt"))).equals("a456bb96b944b2c443868b5ea02d2b458744eb795e161d6835a2d490a67c2510"),"real existing classic8 FNT identity");
        check(classic.metrics.i == 8 && body.metrics.i == 14,"classic8 and body10 line heights differ and remain unchanged");
        arp.b chinese = classic.metrics.a('\u4e09');
        check(chinese.d == 8 && chinese.e == 8 && chinese.l == 8,"real Chinese glyph 8x8/advance8");
        check(body.metrics.a('\u4e09').d == 10 && body.metrics.a('\u4e09').l == 10,"default Chinese remains 10px");
        final List<Object[]> draws = new ArrayList<Object[]>();
        SN sn = (SN)java.lang.reflect.Proxy.newProxyInstance(ItemFont8Test.class.getClassLoader(), new Class<?>[] {SN.class,FontAccess.class},
            (proxy,m,args) -> {
                if (m.getName().equals("cosmo$layoutFont")) return "classic".equals(args[0]) ? classic : body;
                if (m.getName().equals("b") && m.getParameterTypes().length == 0) return "default";
                if (m.getName().equals("a") && args != null && args.length == 4 && args[0] instanceof String) { draws.add(args.clone()); return null; }
                if (m.getReturnType() == boolean.class) return false;
                if (m.getReturnType() == int.class) return 0;
                if (m.getReturnType() == float.class) return 0f;
                return null;
            });
        // Run this mode in a fresh JVM with patched-test.jar FIRST on classpath.
        // Package-private arp fields require the SAME loader/runtime package;
        // copying just Lg/Lb into a child loader would be an invalid fixture.
        ClassLoader loader = ItemFont8Test.class.getClassLoader();
        {
            Class<?> api = loader.loadClass("PRG.ItemFont8"), lg = loader.loadClass("PRG.Lg"), lb = loader.loadClass("PRG.Lb");
            int[] nameCalls = {0}, descCalls = {0};
            Object name = lg.getConstructor(azy.class,azy.class,azy.class).newInstance(supplier(176,null),supplier(70,null),supplier(new amr.d("三线圈"),nameCalls));
            Object category = lg.getConstructor(azy.class,azy.class,azy.class).newInstance(supplier(56,null),supplier(70,null),supplier(new amr.d("装备"),null));
            api.getMethod("registerName",lg).invoke(null,name);
            lg.getMethod("b",SN.class).invoke(name,sn);
            check(nameCalls[0] == 1 && draws.size() == 1 && draws.get(0)[3].equals("classic"),"real Lg consumes once using classic8");
            check((Integer)draws.get(0)[1] >= 176 && (Integer)draws.get(0)[1] <= 177 && (Integer)draws.get(0)[2] == 70,"name original area/anchor, no icon row expansion");
            draws.clear(); lg.getMethod("b",SN.class).invoke(category,sn);
            check(draws.size() == 1 && draws.get(0)[3].equals("default") && (Integer)draws.get(0)[1] == 56,"unregistered category retains default10 and exact coordinate");
            Object description = lb.getConstructor(azy.class,azy.class,azy.class).newInstance(supplier(136,null),supplier(22,null),supplier(new amr.d("三线圈三线圈三线圈三线圈三线圈三线圈"),descCalls));
            api.getMethod("registerDescription",lb).invoke(null,description);
            draws.clear(); lb.getMethod("b",SN.class).invoke(description,sn);
            check(descCalls[0] == 1 && draws.size() == 2,"real Lb consumes full source once, before q14/amw");
            StringBuilder joined = new StringBuilder();
            for (int i=0;i<draws.size();i++) {
                Object[] d=draws.get(i); joined.append(d[0]);
                check(d[3].equals("classic") && (Integer)d[2] == 22 - 8*i,"description classic8/original 8px line step");
                check(((String)d[0]).length()*8<=112,"description original112px width");
            }
            check(joined.toString().equals("三线圈三线圈三线圈三线圈三线圈三线圈"),"no 14-char/zip loss");
            // ASCII-only selected name is exactly the old renderer call, no new
            // classic styling for the original English controls/statistics.
            draws.clear(); api.getMethod("drawName",SN.class,String.class,int.class,int.class,String.class,lg)
                    .invoke(null,sn,"RADIO",176,70,"default",name);
            check(draws.size()==1 && draws.get(0)[3].equals("default") && (Integer)draws.get(0)[1]==176,"ASCII name exact old role/anchor");
            draws.clear(); api.getMethod("drawName",SN.class,String.class,int.class,int.class,String.class,lg)
                    .invoke(null,sn,"",176,70,"default",name);
            check(draws.size()==1 && draws.get(0)[0].equals("") && draws.get(0)[3].equals("default"),"empty blink original call preserved");
            Object english = lb.getConstructor(azy.class,azy.class,azy.class).newInstance(supplier(136,null),supplier(22,null),supplier(new amr.d("RADIO|TEST"),null));
            api.getMethod("registerDescription",lb).invoke(null,english);
            draws.clear(); lb.getMethod("b",SN.class).invoke(english,sn);
            check(draws.size()==2 && draws.get(0)[3].equals("default") && draws.get(1)[3].equals("default"),"real original ASCII Lb chain untouched");
            Object foreign = lb.getConstructor(azy.class,azy.class,azy.class).newInstance(supplier(136,null),supplier(22,null),supplier(new amr.d("三线圈"),null));
            draws.clear(); lb.getMethod("b",SN.class).invoke(foreign,sn);
            check(!draws.isEmpty() && draws.get(0)[3].equals("default"),"unregistered real Lb Chinese remains default10");
            StringBuilder huge=new StringBuilder(); for(int i=0;i<29;i++) huge.append('三');
            Object overflow = lb.getConstructor(azy.class,azy.class,azy.class).newInstance(supplier(136,null),supplier(22,null),supplier(new amr.d(huge.toString()),null));
            api.getMethod("registerDescription",lb).invoke(null,overflow);
            draws.clear(); boolean refused=false;
            try { lb.getMethod("b",SN.class).invoke(overflow,sn); }
            catch(InvocationTargetException expected) { refused=expected.getCause() instanceof IllegalArgumentException; }
            check(refused && draws.isEmpty(),"overbudget Chinese refuses before partial draw, never truncates/overwrites icons");
            classic.metrics.o=0.5f; draws.clear(); refused=false;
            try { lg.getMethod("b",SN.class).invoke(name,sn); }
            catch(InvocationTargetException expected) { refused=expected.getCause() instanceof IllegalStateException; }
            classic.metrics.o=1;
            check(refused && draws.isEmpty(),"fractional/global mutable scale rejected");
            // Real unchanged Le name supplier, with CPU-only state overrides. Its
            // game constructor is NOT called; selected SL->SM->Tc path IS called.
            Class<?> le = loader.loadClass("PRG.Le"), probe = loader.loadClass("PRG.ItemFont8LeProbe");
            Object owner = allocate(probe);
            probe.getField("selected").set(owner,new aAw(new aAJ(new SL("三线圈","test.name"),new SL("说明","test.desc"))));
            Object item = java.lang.reflect.Proxy.newProxyInstance(ItemFont8Test.class.getClassLoader(),new Class<?>[] {aga.class},(p,m,a)->null);
            probe.getField("equipment").set(owner,new aAw(item)); probe.getField("equipped").setBoolean(owner,true);
            String equipped = (String)le.getMethod("b",le).invoke(null,owner);
            check(equipped.equals("三线圈     +"),"REAL Le equipment original pad8 + suffix retained");
            probe.getField("equipped").setBoolean(owner,false);
            check(le.getMethod("b",le).invoke(null,owner).equals("三线圈"),"REAL Le unequipped full source retained");
            check(classic.metrics.o==1 && classic.metrics.p==1 && body.metrics.o==1 && body.metrics.p==1,"no mutable scale on either font");
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length==3 && args[0].equals("--cpu")) cpu(Paths.get(args[1]),Paths.get(args[2]));
        else {
            if(args.length!=4) throw new IllegalArgumentException("original.jar helper-dir runtime-dir new-patched-test.jar");
            patch(Paths.get(args[0]),Paths.get(args[1]),Paths.get(args[3]));
            System.out.println("ITEM_FONT8_PATCH_OK assertions="+assertions+"; run --cpu in a fresh JVM with output JAR first");
            return;
        }
        System.out.println("ITEM_FONT8_CPU_OK assertions="+assertions+" (real FNT/Lg/Lb/Le; no GL/game/save verification)");
    }
}
