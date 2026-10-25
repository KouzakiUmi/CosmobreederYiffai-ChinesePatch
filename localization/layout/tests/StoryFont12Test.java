import PRG.*;
import cosmoloc.layout.FontAccess;
import cosmoloc.layout.PixelLayout;
import java.io.*;
import java.lang.reflect.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Isolated CPU. No GameMain, GL, native texture allocation, install/save writes.
 * --preflight original.jar
 * original.jar helper-dir story12-asset-dir NEW-test.jar
 * Fresh JVM, test.jar FIRST on classpath: --cpu runtime-font-dir
 * Test fonts use real parser/arp allocation with a CPU dimension-only shared
 * texture object; the texture's GPU constructor is NEVER executed.
 */
@SuppressWarnings({"rawtypes","unchecked"})
public final class StoryFont12Test implements Opcodes {
    private static int assertions;
    private static void check(boolean value,String why) { assertions++; if(!value) throw new AssertionError(why); }
    private static byte[] bytes(InputStream input) throws IOException {
        try(InputStream in=input;ByteArrayOutputStream out=new ByteArrayOutputStream()) {
            byte[] b=new byte[8192]; for(int n;(n=in.read(b))>=0;) out.write(b,0,n); return out.toByteArray();
        }
    }
    private static String sha(byte[] raw) throws Exception {
        StringBuilder value=new StringBuilder(); for(byte b:MessageDigest.getInstance("SHA-256").digest(raw)) value.append(String.format("%02x",b&255)); return value.toString();
    }
    private static MethodNode method(ClassNode c,String name,String desc) {
        for(MethodNode m:c.methods) if(m.name.equals(name)&&m.desc.equals(desc)) return m;
        throw new AssertionError("method "+c.name+name+desc);
    }
    private static byte[] methodBytes(MethodNode m) {
        ClassWriter w=new ClassWriter(0); w.visit(V1_8,ACC_PUBLIC,"Probe",null,"java/lang/Object",null); m.accept(w); w.visitEnd(); return w.toByteArray();
    }
    private static Map<String,ClassNode> load(Path source) throws Exception {
        Map<String,ClassNode> nodes=new TreeMap<String,ClassNode>();
        try(JarFile jar=new JarFile(source.toFile())) {
            for(Map.Entry<String,String> pin:StoryFont12Patch.INPUT_SHA256.entrySet()) {
                byte[] raw=bytes(jar.getInputStream(jar.getJarEntry(pin.getKey()+".class")));
                check(sha(raw).equals(pin.getValue()),"real raw target SHA "+pin.getKey());
                ClassNode node=new ClassNode(ASM8); new ClassReader(raw).accept(node,ClassReader.EXPAND_FRAMES); nodes.put(pin.getKey(),node);
            }
        }
        return nodes;
    }
    private static boolean target(ClassNode c,MethodNode m) {
        return (c.name.equals("PRG/Yg")&&m.name.equals("<init>"))
            ||(c.name.equals("PRG/jo")&&m.name.equals("a")&&m.desc.equals("(LPRG/jo;Ljava/lang/String;LPRG/aAJ;)V"))
            ||(c.name.equals("PRG/Na")&&m.name.equals("a")&&m.desc.equals("(LPRG/Na;LPRG/Na$a;LPRG/SN;IILPRG/aAJ;)V"));
    }
    private static AbstractInsnNode previous(AbstractInsnNode n) { do { n=n.getPrevious(); } while(n!=null&&n.getOpcode()<0); return n; }
    private static MethodNode copy(MethodNode m) {
        MethodNode out=new MethodNode(m.access,m.name,m.desc,m.signature,m.exceptions.toArray(new String[0])); m.accept(out); return out;
    }
    private static MethodNode undo(MethodNode m) {
        MethodNode out=copy(m);
        for(AbstractInsnNode n:out.instructions.toArray()) if(n instanceof MethodInsnNode&&((MethodInsnNode)n).owner.equals("PRG/StoryFont12")) {
            String name=((MethodInsnNode)n).name;
            int remove=name.equals("register")?1:(name.equals("drawSubtitle")?7:3);
            AbstractInsnNode p=previous(n);
            for(int i=0;i<remove;i++) { AbstractInsnNode before=previous(p); out.instructions.remove(p); p=before; }
            if(name.equals("register")) out.instructions.remove(n);
            else out.instructions.set(n,new MethodInsnNode(INVOKEVIRTUAL,"PRG/Id","a","(LPRG/SN;ZLjava/lang/String;II)V",false));
        }
        return out;
    }
    private static Map<String,ClassNode> patch(Path source) throws Exception {
        Map<String,ClassNode> nodes=load(source); BridgePatch.apply(nodes);
        Map<String,byte[]> before=new TreeMap<String,byte[]>();
        for(ClassNode c:nodes.values()) for(MethodNode m:c.methods) before.put(c.name+m.name+m.desc,methodBytes(m));
        StoryFont12Patch.apply(nodes);
        for(ClassNode c:nodes.values()) for(MethodNode m:c.methods) {
            check(Arrays.equals(before.get(c.name+m.name+m.desc),methodBytes(target(c,m)?undo(m):m)),
                  "only declared hook instructions changed; original bool/y/input method exact "+c.name+m.name+m.desc);
        }
        boolean rejected=false;
        try { StoryFont12Patch.apply(nodes); } catch(IllegalStateException expected) { rejected=true; }
        check(rejected,"double patch rejected");
        Map<String,ClassNode> bad=load(source); BridgePatch.apply(bad);
        MethodNode na=method(bad.get("PRG/Na"),"a","(LPRG/Na;LPRG/Na$a;LPRG/SN;IILPRG/aAJ;)V");
        for(AbstractInsnNode n:na.instructions.toArray()) if(n instanceof MethodInsnNode&&((MethodInsnNode)n).owner.equals("PRG/Id")) ((MethodInsnNode)n).name="bad";
        byte[] ygBefore=methodBytes(method(bad.get("PRG/Yg"),"<init>","(LPRG/ars;LPRG/Ym;LPRG/Yq;)V"));
        rejected=false; try { StoryFont12Patch.apply(bad); } catch(IllegalStateException expected) { rejected=true; }
        check(rejected&&Arrays.equals(ygBefore,methodBytes(method(bad.get("PRG/Yg"),"<init>","(LPRG/ars;LPRG/Ym;LPRG/Yq;)V"))),"late Na mismatch before any Yg mutate");
        check(nodes.keySet().equals(StoryFont12Patch.INPUT_SHA256.keySet()),"only Yg jo Na target set; radio/menu/save untouched");
        return nodes;
    }
    private static void writeJar(Map<String,ClassNode> nodes,Path helpers,Path assets,Path output) throws Exception {
        check(!Files.exists(output),"new test JAR only");
        // '-' is an in-memory read-only generator stream for an ISOLATED test
        // fixture, not a way to write/replace a denied runtime asset directory.
        // The shipping asset/lifecycle integration must still be done separately.
        byte[] fnt=assets.toString().equals("-") ? bytes(System.in) : Files.readAllBytes(assets.resolve("story12.fnt"));
        check(sha(fnt).equals(StoryFont12.FONT_SHA256),"generated FNT pin");
        try(JarOutputStream out=new JarOutputStream(Files.newOutputStream(output,StandardOpenOption.CREATE_NEW))) {
            for(ClassNode c:nodes.values()) {
                ClassWriter w=new ClassWriter(ClassWriter.COMPUTE_FRAMES|ClassWriter.COMPUTE_MAXS) {
                    @Override protected ClassLoader getClassLoader() { return StoryFont12Test.class.getClassLoader(); }
                };
                c.accept(w); put(out,c.name+".class",w.toByteArray());
            }
            for(String helper:StoryFont12Patch.HELPER_INVENTORY) put(out,helper,Files.readAllBytes(helpers.resolve(helper)));
            put(out,"story12.fnt",fnt);
        }
    }
    private static void put(JarOutputStream out,String name,byte[] value) throws IOException {
        out.putNextEntry(new JarEntry(name)); out.write(value); out.closeEntry();
    }
    private static <T> T allocate(Class<T> type) throws Exception {
        Class<?> unsafe=Class.forName("sun.misc.Unsafe"); Field f=unsafe.getDeclaredField("theUnsafe"); f.setAccessible(true);
        return (T)unsafe.getMethod("allocateInstance",Class.class).invoke(f.get(null),type);
    }
    public static class CpuFile extends aqX {
        private final byte[] content;
        CpuFile(byte[] content) { super(); this.content=content; this.a=new java.io.File("story12.fnt"); }
        @Override public InputStream e() { return new ByteArrayInputStream(content); }
        @Override public aqX d() { return this; }
        @Override public aqX b(String child) { return this; }
        @Override public String toString() { return "CPU font"; }
    }
    public static class CpuFont extends arp {
        public final arp.a data;
        CpuFont(byte[] fnt) { this(new arp.a(new CpuFile(fnt),false)); }
        CpuFont(arp.a data) { super(data,new arI(),false); this.data=data; }
        @Override protected void a(arp.a data) { }
    }
    public static class CpuTexture extends ark {
        private CpuTexture() { super((aqX)null); throw new AssertionError("GPU texture constructor MUST NEVER RUN"); }
        @Override public int e() { return 2048; }
        @Override public int f() { return 2048; }
        @Override public void dispose() { throw new AssertionError("borrowed texture must not be disposed here"); }
    }
    public static class CpuResources extends Yq {
        public aFh fonts; public art.a region; public int regionReads;
        private CpuResources() { super(); throw new AssertionError("game resource constructor MUST NEVER RUN"); }
        @Override public aFh f() { return fonts; }
        @Override public void a(aFh value) { fonts=value; }
        @Override public art.a i(String name) { if(!name.equals("bbc2")) throw new AssertionError(name); regionReads++; return region; }
    }
    public static class CpuBatch extends ars {
        private CpuBatch() { super(); throw new AssertionError("GPU batch constructor MUST NEVER RUN"); }
        @Override public asj h() { return new asj(); }
        @Override public void a(int source,int destination) { if(source!=1||destination!=771) throw new AssertionError("blend changed"); }
    }
    public static class CpuMN extends MN {
        private CpuMN() { super(null,null,false,"",(azK)azI.MODULE$); throw new AssertionError("game MN constructor MUST NEVER RUN"); }
        @Override public boolean c() { return false; }
    }
    private static arp.a data(arp font) throws Exception { Field f=arp.class.getDeclaredField("a"); f.setAccessible(true); return (arp.a)f.get(font); }
    private static String spaces(int count) { StringBuilder out=new StringBuilder(); for(int i=0;i<count;i++) out.append(' '); return out.toString(); }
    private static anh state(String page) {
        amn animation=new amn(page,0,(azK)azI.MODULE$,0.05f);
        return new anh(null,0,new aAw(new amG(animation,(azK)azI.MODULE$,"Normal")),(aEO)aFC.MODULE$,(aEO)aFC.MODULE$,null,false,null,null,(aEO)aFC.MODULE$,(azK)azI.MODULE$);
    }
    private static void cpu(Path runtime) throws Exception {
        byte[] fontBytes=bytes(StoryFont12Test.class.getResourceAsStream("/story12.fnt"));
        check(sha(fontBytes).equals(StoryFont12.FONT_SHA256),"real root story FNT");
        PixelLayout.Metrics metrics=StoryFont12.metrics();
        check(metrics==StoryFont12.metrics(),"lazy metrics singleton");
        check(metrics.glyph('中').width==12&&metrics.glyph('中').height==12&&metrics.glyph('中').xAdvance==12,"true native12 glyph cell/advance");
        check(StoryFont12.uses12("ABC中")&&StoryFont12.uses12("……")&&StoryFont12.uses12("“”")&&!StoryFont12.uses12("ASCII..."),"full caption Chinese/independent punctuation discriminator");
        byte[] bad=fontBytes.clone(); bad[bad.length-1]^=1; boolean refused=false;
        try { StoryFont12.readMetrics(new ByteArrayInputStream(bad)); } catch(IOException expected) { refused=true; }
        check(refused,"metrics SHA fails closed");
        final CpuFont body=new CpuFont(Files.readAllBytes(runtime.resolve("bbc2-10px.fnt")));
        final CpuFont classic=new CpuFont(Files.readAllBytes(runtime.resolve("classic.fnt")));
        final CpuResources resources=allocate(CpuResources.class);
        resources.fonts=(aFh)azQ.MODULE$.a().a((aEO)aFC.MODULE$);
        resources.region=new art.a(allocate(CpuTexture.class),0,0,2048,2048);
        resources.a("default",body,8); resources.a("classic",classic,8); resources.a("dingbats",body,8);
        final int[] files={0};
        apQ.e=(apO)java.lang.reflect.Proxy.newProxyInstance(StoryFont12Test.class.getClassLoader(),new Class<?>[]{apO.class},(p,m,a)-> {
            if(m.getName().equals("b")&&a!=null&&a.length==1&&a[0].equals("story12.fnt")) { files[0]++; return new CpuFile(fontBytes); }
            throw new AssertionError("unexpected file/texture load "+m);
        });
        // Execute the ACTUAL patched Yg constructor twice using CPU-only batch
        // and resource dependencies. Both share one original Yq font map.
        CpuBatch batch=allocate(CpuBatch.class);
        Yg first=new Yg(batch,null,resources), second=new Yg(batch,null,resources);
        arp story=((Yq.b)resources.fonts.apply("story12")).a(); arp.a sd=data(story);
        check(files[0]==1&&resources.regionReads==1,"actual Yg registration once per Yq, no second font allocation");
        check(((FontAccess)first).cosmo$layoutFont("story12")==story&&((FontAccess)second).cosmo$layoutFont("default")==body,"BridgePatch coexists and exact map objects preserved");
        check(((Yq.b)resources.fonts.apply("classic")).a()==classic&&((Yq.b)resources.fonts.apply("dingbats")).a()==body,"all old roles retain identity");
        Field owned=arp.class.getDeclaredField("f"); owned.setAccessible(true);
        check(!owned.getBoolean(story)&&story.a().a(0)==resources.region,"real arp ownsTexture=false and original shared atlas region");
        check(sd.i==16&&body.data.i==14&&classic.data.i==8,"story16-line/body14/classic8 unchanged");
        check(sd.o==1&&sd.p==1&&body.data.o==1&&body.data.p==1&&classic.data.o==1&&classic.data.p==1,"no mutable font scale");
        check(sd.k==body.data.k&&sd.h==body.data.h,"ASCII actual engine ascent/padding identical across roles");
        for(int cp=32;cp<127;cp++) {
            arp.b a=sd.a((char)cp),b=body.data.a((char)cp);
            check(a.d==b.d&&a.e==b.e&&a.j==b.j&&a.k==b.k&&a.l==b.l&&a.l==8,"real original ASCII glyph metrics "+cp);
        }
        check(sd.a('中').d==12&&sd.a('中').e==12&&sd.a('中').l==12&&body.data.a('中').l==10,"real parsed registered12 and default10 coexist");
        int nativeCount=0;
        for(int cp=128;cp<=65535;cp++) {
            arp.b g=sd.a((char)cp); if(g==null) continue;
            if(!StoryFont12.uses12(String.valueOf((char)cp))) {
                arp.b old=body.data.a((char)cp);
                check(old!=null&&g.d==old.d&&g.e==old.e&&g.l==old.l,"original nonwide legacy glyph (including pound) preserved");
                continue;
            }
            nativeCount++;
            check(g.d==12&&g.e==12&&g.l==12,"ALL real native12 glyph fields/uses12 parity U+"+Integer.toHexString(cp));
        }
        check(nativeCount==2312,"full native12 corpus glyph count");
        final List<Object[]> draws=new ArrayList<Object[]>();
        SN sn=(SN)java.lang.reflect.Proxy.newProxyInstance(StoryFont12Test.class.getClassLoader(),new Class<?>[]{SN.class},(p,m,a)-> {
            if(m.getName().equals("b")&&m.getParameterTypes().length==0) return "default";
            if(m.getName().equals("a")&&a!=null&&a.length==4&&a[0] instanceof String) { draws.add(a.clone()); return null; }
            if(m.getReturnType()==boolean.class) return false; if(m.getReturnType()==int.class) return 0; if(m.getReturnType()==float.class) return 0f; return null;
        });
        String page="HELLO中……"; jo subtitle=new jo(state(page),28,false,sn,16,160,Ol.MODULE$,null);
        Method joLine=jo.class.getMethod("a",jo.class,String.class,aAJ.class);
        for(String mask:new String[]{spaces(28),"HELLO"+spaces(23),"HELLO中……"+spaces(20)}) {
            draws.clear(); joLine.invoke(null,subtitle,"Normal",new aAJ(new amr.d(mask),Integer.valueOf(1)));
            check(draws.size()==1&&draws.get(0)[3].equals("story12")&&(Integer)draws.get(0)[1]==8&&(Integer)draws.get(0)[2]==144,"REAL jo full-page stable12/x8 for all-space, ASCII-prefix and CJK mask");
        }
        String twenty=""; for(int i=0;i<20;i++) twenty+="中";
        jo exact=new jo(state(twenty),28,false,sn,16,160,Ol.MODULE$,null);
        draws.clear(); joLine.invoke(null,exact,"Normal",new aAJ(new amr.d(twenty+spaces(8)),Integer.valueOf(0)));
        check(draws.size()==1&&(Integer)draws.get(0)[1]+240==248,"REAL jo20Han fits logical8+240<=248 despite grid padding");
        for(String style:new String[]{"Fox","HardFox"}) {
            draws.clear(); joLine.invoke(null,subtitle,style,new aAJ(new amr.d("HELLO"),Integer.valueOf(0)));
            check(draws.size()==1&&draws.get(0)[3].equals("dingbats")&&(Integer)draws.get(0)[1]==16,"REAL jo original pattern branch "+style);
        }
        jo english=new jo(state("HELLO"),28,false,sn,16,160,Ol.MODULE$,null);
        draws.clear(); joLine.invoke(null,english,"Normal",new aAJ(new amr.d("HELLO"),Integer.valueOf(0)));
        check(draws.size()==1&&draws.get(0)[3].equals("default")&&(Integer)draws.get(0)[1]==16,"REAL jo pure ASCII page untouched");
        Na storyOwner=new Na(allocate(CpuMN.class));
        Method naLine=Na.class.getMethod("a",Na.class,Na.a.class,SN.class,int.class,int.class,aAJ.class);
        Na.a storyPage=new Na.a(new amn(page,0,(azK)azI.MODULE$,0.05f),"Normal",(aEO)aFC.MODULE$,null);
        for(String mask:new String[]{spaces(28),"HELLO"+spaces(23),"HELLO中……"+spaces(20)}) {
            draws.clear(); naLine.invoke(null,storyOwner,storyPage,sn,16,160,new aAJ(new amr.d(mask),Integer.valueOf(2)));
            check(draws.size()==1&&draws.get(0)[3].equals("story12")&&(Integer)draws.get(0)[1]==8&&(Integer)draws.get(0)[2]==128,"REAL Na fullpage stable12/x8 and original16px ystep");
        }
        Na.a asciiPage=new Na.a(new amn("HELLO",0,(azK)azI.MODULE$,0.05f),"Normal",(aEO)aFC.MODULE$,null);
        draws.clear(); naLine.invoke(null,storyOwner,asciiPage,sn,16,160,new aAJ(new amr.d("HELLO"),Integer.valueOf(0)));
        check(draws.size()==1&&draws.get(0)[3].equals("default")&&(Integer)draws.get(0)[1]==16,"REAL Na pure ASCII untouched");
        refused=false; draws.clear(); try { StoryFont12.drawStory(Id.MODULE$,sn,false,twenty+"中",16,160,twenty+"中"); } catch(IllegalArgumentException expected) { refused=true; }
        check(refused&&draws.isEmpty(),"oversize line fails before drawing beyond original canvas");
        final byte[] looseTamper=fontBytes.clone(); looseTamper[looseTamper.length-1]^=1;
        apQ.e=(apO)java.lang.reflect.Proxy.newProxyInstance(StoryFont12Test.class.getClassLoader(),new Class<?>[]{apO.class},(p,m,a)->new CpuFile(looseTamper));
        CpuResources invalid=allocate(CpuResources.class); invalid.fonts=(aFh)azQ.MODULE$.a().a((aEO)aFC.MODULE$); invalid.region=resources.region;
        refused=false; try { StoryFont12.register(invalid); } catch(IllegalStateException expected) { refused=true; }
        check(refused&&invalid.fonts.e("story12").g()&&invalid.regionReads==0,"actual loose FileHandle SHA drift refuses BEFORE font/region/map allocation");
    }
    public static void main(String[] args) throws Exception {
        if(args.length==2&&args[0].equals("--cpu")) { cpu(Paths.get(args[1])); System.out.println("STORY12_CPU_OK assertions="+assertions+" (real Yg/jo/Na/FNT; GL/clip/game/save NOT run)"); return; }
        if(args.length==2&&args[0].equals("--preflight")) { patch(Paths.get(args[1])); System.out.println("STORY12_PREFLIGHT_OK assertions="+assertions); return; }
        if(args.length!=4) throw new IllegalArgumentException("original.jar helpers assets NEW-test.jar | --cpu runtime-font-dir | --preflight original.jar");
        Map<String,ClassNode> nodes=patch(Paths.get(args[0])); writeJar(nodes,Paths.get(args[1]),Paths.get(args[2]),Paths.get(args[3]));
        System.out.println("STORY12_PATCH_OK assertions="+assertions+"; run fresh JVM --cpu with test JAR first");
    }
}
