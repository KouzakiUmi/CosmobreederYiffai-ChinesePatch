import PRG.*;
import cosmoloc.layout.FontAccess;
import java.io.*;
import java.lang.reflect.*;
import java.nio.file.*;
import java.util.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** CPU only: actual patched scene row methods and original arr/arq vertices. */
@SuppressWarnings({"rawtypes","unchecked"})
public final class SceneTextTest {
    static int checks,vertices,corpus;
    static final List<Map<String,Object>> records=new ArrayList<Map<String,Object>>();
    static String json(Object value) {
        if(value==null)return "null";
        if(value instanceof Number||value instanceof Boolean)return value.toString();
        if(value instanceof Map){StringBuilder b=new StringBuilder("{");for(Object v:((Map)value).entrySet()){Map.Entry e=(Map.Entry)v;if(b.length()>1)b.append(',');b.append(json(e.getKey())).append(':').append(json(e.getValue()));}return b.append('}').toString();}
        if(value instanceof Iterable){StringBuilder b=new StringBuilder("[");for(Object e:(Iterable)value){if(b.length()>1)b.append(',');b.append(json(e));}return b.append(']').toString();}
        StringBuilder b=new StringBuilder("\"");for(char c:value.toString().toCharArray()){if(c=='\"'||c=='\\')b.append('\\').append(c);else if(c<32)b.append(String.format("\\u%04x",(int)c));else b.append(c);}return b.append('\"').toString();
    }
    static final Map<String,CpuFont> fonts=new HashMap<String,CpuFont>();
    static final List<Object[]> draws=new ArrayList<Object[]>();
    static int forbidden;
    static void guard(String[] inputs) {
        final List<Path> allowed=new ArrayList<Path>();
        for(String entry:System.getProperty("java.class.path").split(java.util.regex.Pattern.quote(File.pathSeparator)))allowed.add(Paths.get(entry).toAbsolutePath().normalize());
        for(String input:inputs)allowed.add(Paths.get(input).toAbsolutePath().normalize());
        allowed.add(Paths.get(System.getProperty("java.home")).toAbsolutePath().normalize());
        final String output=System.getProperty("scenes.report");
        System.setSecurityManager(new SecurityManager() {
            void refuse(String operation){forbidden++;throw new SecurityException("CPU scene fixture refused "+operation);}
            public void checkRead(String name){Path p=Paths.get(name).toAbsolutePath().normalize();for(Path root:allowed)if(p.equals(root)||p.startsWith(root))return;refuse("read "+name);}
            public void checkWrite(String name){if(output==null||!Paths.get(name).toAbsolutePath().normalize().equals(Paths.get(output).toAbsolutePath().normalize()))refuse("write "+name);}
            public void checkDelete(String name){refuse("delete");}public void checkExec(String cmd){refuse("exec");}
            public void checkLink(String name){refuse("native library");}public void checkConnect(String host,int port){refuse("network");}public void checkListen(int port){refuse("listen");}
            public void checkPermission(java.security.Permission p){if(p instanceof RuntimePermission&&(p.getName().equals("setSecurityManager")||p.getName().startsWith("loadLibrary.")||p.getName().equals("shutdownHooks")))refuse(p.getName());}
        });
    }
    static final class CpuFile extends aqX {
        final byte[] content;CpuFile(byte[] b){content=b;this.a=new File("CPU.fnt");}
        public InputStream e(){return new ByteArrayInputStream(content);}
        public aqX d(){return this;}public aqX b(String ignored){return this;}
    }
    static final class CpuFont extends arp {
        CpuFont(byte[] b){super(new arp.a(new CpuFile(b),false),new arI(),false);}
        protected void a(arp.a data) { }
    }
    static final SN RECORD=(SN)Proxy.newProxyInstance(SceneTextTest.class.getClassLoader(),new Class[]{SN.class,FontAccess.class},(p,m,a)->{
        if(m.getName().equals("cosmo$layoutFont"))return fonts.get(a[0]);
        if((m.getName().equals("b")||m.getName().equals("c"))&&m.getParameterCount()==0)return "default";
        if(m.getName().equals("a")&&a!=null&&(a.length==4||a.length==5)&&a[0] instanceof String&&a[a.length-1] instanceof String){draws.add(a.clone());quads(a);}
        if(m.getReturnType()==int.class)return 0;if(m.getReturnType()==boolean.class)return false;return null;
    });
    static void check(boolean b,String message){checks++;if(!b)throw new AssertionError(message);}
    static void same(Object a,Object b,String message){check(Objects.equals(a,b),message+": "+a+" != "+b);}
    static String repeat(String s,int n){StringBuilder out=new StringBuilder();while(n-->0)out.append(s);return out.toString();}
    static String visible(String text){return text.replace(" ","").replace("|","").replace("$","").replace("\n","").replace("\r","");}
    static Object field(Object o,Class<?> c,String name)throws Exception{Field f=c.getDeclaredField(name);f.setAccessible(true);return f.get(o);}
    static void quads(Object[] draw)throws Exception {
        String text=(String)draw[0];arp font=fonts.get(draw[draw.length-1]);
        arr layout=new arr();layout.a(font,text,0,text.length(),new ara(1,1,1,1),0,8,false,null);
        arq cache=new arq(font,true);cache.a(layout,(Integer)draw[1],(Integer)draw[2]);
        float[][] pages=(float[][])field(cache,arq.class,"k");int[] counts=(int[])field(cache,arq.class,"l");
        int glyphs=0;for(int n:counts)glyphs+=n/20;
        same(glyphs,text.length(),"real arr/arq retains every BMP glyph");vertices+=glyphs*4;
        for(int page=0;page<pages.length;page++)for(int n=0;n<counts[page];n+=20){
            float left=pages[page][n],right=pages[page][n+10];
            check(left>=-1&&right<=257,"actual CPU quad stays in logical canvas");
        }
    }
    static void gates(Path original)throws Exception {
        Map<String,ClassNode> nodes=new LinkedHashMap<String,ClassNode>();
        try(java.util.jar.JarFile jar=new java.util.jar.JarFile(original.toFile())) {
            for(String key:SceneTextPatch.INPUT_SHA256.keySet()) {
                ClassNode c=new ClassNode(Opcodes.ASM8);
                new ClassReader(jar.getInputStream(jar.getJarEntry(key+".class"))).accept(c,ClassReader.EXPAND_FRAMES);nodes.put(key,c);
            }
        }
        ClassNode kc=nodes.get("PRG/Kc");kc.methods.get(kc.methods.size()-1).instructions.insert(new InsnNode(Opcodes.NOP));
        ClassWriter w=new ClassWriter(0);nodes.get("PRG/Ew").accept(w);byte[] before=w.toByteArray();
        boolean refused=false;try{SceneTextPatch.apply(nodes);}catch(IllegalStateException expected){refused=true;}
        check(refused,"last class tamper refuses");w=new ClassWriter(0);nodes.get("PRG/Ew").accept(w);
        check(Arrays.equals(before,w.toByteArray()),"late pin failure does not partially mutate earlier Ew");
    }
    public static void main(String[] args)throws Exception {
        boolean candidate=args.length==5&&args[0].equals("--candidate");
        if(candidate)args=Arrays.copyOfRange(args,1,args.length);
        if(args.length!=4)throw new IllegalArgumentException("[--candidate] jar font-dir dictionary-sfw.json dictionary-nsfw.json");
        System.setOut(new PrintStream(System.out,true,"UTF-8"));
        if(!candidate)gates(Paths.get(args[0]));Path dir=Paths.get(args[1]);
        fonts.put("default",new CpuFont(Files.readAllBytes(dir.resolve("bbc2.fnt"))));
        fonts.put("classic",new CpuFont(Files.readAllBytes(dir.resolve("classic.fnt"))));
        StringBuilder ascii=new StringBuilder();for(char c=32;c<127;c++)ascii.append(c);fonts.get("classic").a(ascii);
        guard(args);
        XK.MODULE$.a(aJB.MODULE$.h().d());XK.MODULE$.b(aJB.MODULE$.h().d());XK.MODULE$.c(aJB.MODULE$.h().d());XK.MODULE$.d(aJB.MODULE$.h().d());
        // Verify actual patched synthetic methods, not a reimplementation of their callers.
        Method ew=Ew.class.getMethod("a",SN.class,int.class,aAJ.class);
        for(int row=0;row<2;row++){
            draws.clear();ew.invoke(null,RECORD,2,new aAJ(new amr.d("中文混排"),Integer.valueOf(row)));
            same(draws.size(),1,"real Ew row draw");same(draws.get(0)[2],110-row*8,"real Ew placeholder consumer retains original anchor");
        }
        Method card=Jm.class.getMethod("a",Jm.class,SN.class,int.class,aAJ.class);
        Jm owner=EndingReportLayoutTest.allocate(Jm.class);EndingReportLayoutTest.put(owner,"h",0);
        draws.clear();card.invoke(null,owner,RECORD,120,new aAJ(new amr.d("中文卡牌"),Integer.valueOf(166)));
        same(draws.get(0)[3],"classic","real Jm constrained 8px row role");
        if(candidate) same(Paths.get(Jm.class.getProtectionDomain().getCodeSource().getLocation().toURI()).toRealPath(),Paths.get(args[0]).toRealPath(),"real Jm loaded from final candidate");
        else check(Jm.class.getProtectionDomain().getCodeSource().getLocation().toString().contains("targets"),"real Jm loaded from scene overlay");
        ka achievement=(ka)Proxy.newProxyInstance(SceneTextTest.class.getClassLoader(),new Class[]{ka.class},(p,m,a)->{
            if(m.getName().equals("a"))return "CPU";if(m.getReturnType()==boolean.class)return false;return null;
        });
        SH sh=EndingReportLayoutTest.allocate(SH.class);EndingReportLayoutTest.put(sh,"b",(azz<String,SL>)(key->new SL("中文成就",key)));
        Method announce=kn.class.getMethod("a",ka.class,SH.class,SN.class,double.class);
        draws.clear();announce.invoke(null,achievement,sh,RECORD,0.0);
        same(draws.size(),2,"real kn heading and localized achievement draw");same(draws.get(1)[0],"[中文成就]","real kn brackets retained");same(draws.get(1)[4],"classic","real kn role");
        for(String label:new String[]{"中文地名","ABC中文DEF","TELEPORTAL","中"}) {
            draws.clear();SceneText.mapDraw(RECORD,label,999,206,"default");Object[] d=draws.get(0);
            arr a=new arr();a.a(fonts.get("default"),label,0,label.length(),new ara(1,1,1,1),0,8,false,null);
            check(Math.abs(((Integer)d[1]-((arp.a)field(fonts.get("default"),arp.class,"a")).h)+a.d/2-128)<=1,"actual glyph-layout center within one pixel");
        }
        for(String text:new String[]{repeat("中",44),"A"+repeat("中",20)+"，"+repeat("中",10),"中文|第二行"}) {
            String grid=SceneText.breedFormat(amw.MODULE$,text,Ol.MODULE$,NW.MODULE$,false,RECORD);
            same(grid.length(),56,"Ew exactly two fully consumed blocks");same(visible(grid),visible(text),"Ew full source conservation");
            for(int row=0;row<2;row++) {draws.clear();SceneText.breedDraw(RECORD,grid.substring(row*28,row*28+28),16,78-row*8,"default");}
        }
        draws.clear();SceneText.dataName(RECORD,"败北",24,46,"default");
        same(draws.get(0)[3],"classic","data-book name uses compact8 at original eight-pixel row pitch");
        same(draws.get(0)[1],24,"data-book name x unchanged");same(draws.get(0)[2],46,"data-book name y unchanged");
        draws.clear();SceneText.dataName(RECORD,"----",24,46,"default");
        same(draws.get(0)[3],"default","unrevealed ASCII data-book names unchanged");
        boolean rejected=false;try{SceneText.breedFormat(amw.MODULE$,repeat("中",60),Ol.MODULE$,NW.MODULE$,false,RECORD);}catch(IllegalArgumentException expected){rejected=true;}
        check(rejected,"unknown overheight refuses instead of losing tail");
        for(int mode=2;mode<4;mode++) {
            Map<String,String> dictionary=EndingReportLayoutTest.json(new String(Files.readAllBytes(Paths.get(args[mode])),"UTF-8"));
            for(Map.Entry<String,String> e:dictionary.entrySet()) {
                String k=e.getKey(),v=e.getValue(),grid=null;
                if(k.startsWith("ui.breeding.")&&(k.contains(".affinity.")||k.contains(".needs."))) {
                    draws.clear();
                    if(k.contains(".affinity."))SceneText.breedAffinity(amw.MODULE$,v,Ol.MODULE$,NW.MODULE$,false,RECORD);
                    else SceneText.breedNeeds(amw.MODULE$,v,Ol.MODULE$,NW.MODULE$,false,RECORD);
                    StringBuilder actual=new StringBuilder();for(Object[] d:draws)actual.append(d[0]);
                    same(visible(actual.toString()),visible(v),"actual breed corpus reaches draw "+k);corpus++;
                    Map<String,Object> record=new LinkedHashMap<String,Object>();record.put("variant",mode==2?"sfw":"nsfw");record.put("key",k);record.put("source",v);record.put("status","complete_cpu_draw");
                    List<Object> rendered=new ArrayList<Object>();for(Object[] d:draws)rendered.add(Arrays.asList(d[0],d[1],d[2],d[d.length-1]));record.put("draws_text_x_y_role",rendered);records.add(record);
                    continue;
                }
                else if(k.startsWith("navmap.")&&!k.endsWith(".left")&&!k.endsWith(".right")) {
                    draws.clear();SceneText.mapDraw(RECORD,v,0,206,"default");same(draws.get(0)[0],v,"map label source unchanged "+k);corpus++;continue;
                }
                else if(k.startsWith("ui.card.")&&k.endsWith(".name")) {
                    draws.clear();SceneText.cardDraw(RECORD,v,120,174,"default");same(draws.get(0)[0],v,"card title unchanged "+k);corpus++;continue;
                }
                else if(k.startsWith("ui.card.")&&k.contains(".desc."))
                    grid=SceneText.cardFormat(amw.MODULE$,v,NV.MODULE$,k.endsWith("Back")?NT.MODULE$:NU.MODULE$,true);
                else if(k.startsWith("ui.achievement_popup."))
                    grid=SceneText.achievementFormat(amw.MODULE$,v,Oi.MODULE$,Oa.MODULE$,false);
                if(grid!=null) {
                    String expected=k.startsWith("ui.card.")?ams.MODULE$.a(amw.MODULE$.a(v)):v;
                    same(visible(grid),visible(expected),"actual corpus source retained "+k);corpus++;
                }
            }
        }
        String text=repeat("中",15)+"（中文），中文……结尾";
        String grid=SceneText.fixedGrid(text,16,4,false);
        same(visible(grid),text,"Chinese punctuation conserves all source");
        for(int at=0;at<grid.length();at+=16){String row=grid.substring(at,at+16).trim();if(!row.isEmpty()){check("，。）】！？".indexOf(row.charAt(0))<0,"no forbidden line start");check("（【".indexOf(row.charAt(row.length()-1))<0,"no forbidden line end");}}
        check(forbidden==0,"no game/native/network/save path attempts under CPU guard");
        String report=System.getProperty("scenes.report");if(report!=null)Files.write(Paths.get(report),json(records).getBytes("UTF-8"));
        System.out.println("PASS SceneText checks="+checks+" actualCpuVertices="+vertices+" twoVariantCorpusFields="+corpus+"; real Ew/Jm rows, arr/arq, atomic pin negative; no full scene/input/GL/CRT claim");
    }
}
