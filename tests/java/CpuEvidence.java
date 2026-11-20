package PRG;

import cosmoloc.layout.FontAccess;
import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.security.*;
import java.util.*;
import java.util.jar.*;

/** Test-only: final r27 consumers -> original arr -> original arq CPU vertices.
 * No Main/GameMain, texture constructor, GL, Steam, Hi/Mg/save service or deployment.
 */
@SuppressWarnings({"unchecked","rawtypes","removal"})
public final class CpuEvidence {
 static sun.misc.Unsafe unsafe;
 static final Map<String,CpuFont> fonts=new LinkedHashMap<String,CpuFont>();
 static final List<Object> scenarios=new ArrayList<Object>();
 static List<Object> calls;
 static Path out,jar;
 static int vertices;
 static final List<String> denials=new ArrayList<String>();
 public static final class CpuFile extends aqX {
  final byte[] content;
  CpuFile(byte[] bytes){super();content=bytes;this.a=new File("CPU-only.fnt");}
  @Override public InputStream e(){return new ByteArrayInputStream(content);}
  @Override public aqX d(){return this;}
  @Override public aqX b(String child){return this;}
 }
 public static final class CpuFont extends arp {
  final arp.a metrics;
  CpuFont(byte[] bytes){this(new arp.a(new CpuFile(bytes),false));}
  CpuFont(arp.a data){super(data,new arI(),false);metrics=data;}
  @Override protected void a(arp.a data){/* skip texture/UV initialization only */}
 }
 static <T>T allocate(Class<T> c)throws Exception{return (T)unsafe.allocateInstance(c);}
 static void put(Object o,Class<?> c,String n,Object v)throws Exception{Field f=c.getDeclaredField(n);f.setAccessible(true);f.set(o,v);}
 static Object field(Object o,Class<?> c,String n)throws Exception{Field f=c.getDeclaredField(n);f.setAccessible(true);return f.get(o);}
 static byte[] bytes(InputStream in)throws Exception{try(InputStream i=in;ByteArrayOutputStream o=new ByteArrayOutputStream()){byte[]b=new byte[8192];for(int n;(n=i.read(b))>=0;)o.write(b,0,n);return o.toByteArray();}}
 static String sha(byte[] b)throws Exception{StringBuilder s=new StringBuilder();for(byte x:MessageDigest.getInstance("SHA-256").digest(b))s.append(String.format("%02x",x&255));return s.toString();}
 static Map<String,Object> map(Object...p){Map<String,Object>r=new LinkedHashMap<String,Object>();for(int i=0;i<p.length;i+=2)r.put((String)p[i],p[i+1]);return r;}
 static String json(Object o){if(o==null)return"null";if(o instanceof Number||o instanceof Boolean)return o.toString();if(o instanceof Map){StringBuilder s=new StringBuilder("{");for(Object eo:((Map)o).entrySet()){Map.Entry e=(Map.Entry)eo;if(s.length()>1)s.append(',');s.append(json(e.getKey())).append(':').append(json(e.getValue()));}return s.append('}').toString();}if(o instanceof Iterable){StringBuilder s=new StringBuilder("[");for(Object e:(Iterable)o){if(s.length()>1)s.append(',');s.append(json(e));}return s.append(']').toString();}String v=o.toString();StringBuilder s=new StringBuilder("\"");for(int i=0;i<v.length();i++){char c=v.charAt(i);if(c=='\"'||c=='\\')s.append('\\').append(c);else if(c<32)s.append(String.format("\\u%04x",(int)c));else s.append(c);}return s.append('"').toString();}
 @SafeVarargs static <T>aEO<T> list(T...items){aEO<T>r=(aEO<T>)(Object)aFC.MODULE$;for(int i=items.length-1;i>=0;i--)r=r.b(items[i]);return r;}
 static <T>azK<T> none(){return(azK<T>)(Object)azI.MODULE$;}
 static azy supplier(final Object v){return (azy)Proxy.newProxyInstance(CpuEvidence.class.getClassLoader(),new Class[]{azy.class},(p,m,a)->{if(m.getName().startsWith("apply"))return v;if(m.getName().equals("toString"))return"CPU fixture supplier";return null;});}
 static void begin(String id,String provenance){calls=new ArrayList<Object>();scenarios.add(map("id",id,"provenance",provenance,"calls",calls));}
 static SN sn(){return(SN)Proxy.newProxyInstance(CpuEvidence.class.getClassLoader(),new Class[]{SN.class,FontAccess.class},(p,m,a)->{
  if(m.getName().equals("cosmo$layoutFont"))return fonts.get(a[0]);
  if(m.getDeclaringClass()==Object.class){if(m.getName().equals("hashCode"))return System.identityHashCode(p);if(m.getName().equals("equals"))return p==a[0];return"CPU SN";}
  if(m.getName().equals("b")&&m.getParameterCount()==0)return"default";
  if(m.getReturnType()!=void.class)throw new AssertionError("Unexpected SN request "+m);
  List<String>stack=new ArrayList<String>();for(StackTraceElement f:Thread.currentThread().getStackTrace())if(f.getClassName().startsWith("PRG.")&&!f.getClassName().startsWith("PRG.CpuEvidence"))stack.add(f.getClassName()+"."+f.getMethodName());
  Map<String,Object>call=map("method",m.toGenericString(),"stack",stack);
  if(m.getName().equals("a")&&a!=null&&a.length==4&&a[0] instanceof String&&a[3] instanceof String){call.putAll(map("kind","text","text",a[0],"x",a[1],"y",a[2],"font",a[3]));recordQuads(call,(String)a[0],(Integer)a[1],(Integer)a[2],fonts.get(a[3]));}
  else if(m.getName().equals("a")&&a!=null&&(a.length==3||a.length==5)&&a[0] instanceof String){call.putAll(map("kind",a.length==3?"image":"rect","name",a[0],"x",a[1],"y",a[2],"width",a.length==5?a[3]:null,"height",a.length==5?a[4]:null));}
  else throw new AssertionError("Unsupported SN draw "+m);
  calls.add(call);return null;
 });}
 static void recordQuads(Map<String,Object>call,String text,int x,int y,CpuFont font)throws Exception{
  if(font==null)throw new AssertionError("Missing CPU font");
  arr layout=new arr();layout.a(font,text,0,text.length(),new ara(1,1,1,1),0,8,false,null);
  arq cache=new arq(font,true);cache.a(layout,x,y);
  float[][]pages=(float[][])field(cache,arq.class,"k");int[]lengths=(int[])field(cache,arq.class,"l");
  List<Object>quads=new ArrayList<Object>();int ordinal=0;
  for(int r=0;r<layout.a.b;r++){arr.a run=layout.a.a(r);for(int i=0;i<run.a.b;i++){
   arp.b g=run.a.a(i);int k=ordinal*20;float[]v=pages[g.o];if(k+20>lengths[g.o])throw new AssertionError("Vertex count");
   float left=Math.min(v[k],v[k+10]),right=Math.max(v[k],v[k+10]),bottom=Math.min(v[k+1],v[k+11]),top=Math.max(v[k+1],v[k+11]);
   if(g.a!=text.charAt(ordinal))throw new AssertionError("Real glyph identity");
   List<Object>xy=new ArrayList<Object>();for(int n=0;n<20;n+=5)xy.add(Arrays.asList(v[k+n],v[k+n+1]));
   quads.add(map("codepoint",g.a,"srcX",g.b,"srcY",g.c,"width",g.d,"height",g.e,"page",g.o,"x",left,"screenTop",224-top,"right",right,"screenBottom",224-bottom,"arr_advance",run.b.a[i],"arr_run_x",run.c,"arr_run_y",run.d,"vertices_y_up",xy));ordinal++;vertices+=4;
  }}
  if(ordinal!=text.length()||lengths[0]!=20*ordinal)throw new AssertionError("Whole glyph run retained");
  call.put("quads",quads);call.put("layout_width",layout.d);call.put("position_source","ACTUAL r27 arq.a(arr,float,float) vertex array; not a copied coordinate formula");
 }
 static LY occupied(String name)throws Exception{
  FI fi=new FI(azQ.MODULE$.b().d(),azQ.MODULE$.b().d(),azQ.MODULE$.b().d(),azQ.MODULE$.b().d(),azQ.MODULE$.a().a(),azQ.MODULE$.a().a());
  Fr fr=allocate(Fr.class);put(fr,Fr.class,"e",azQ.MODULE$.a().a());
  GB gb=new GB(name,RN.a.MODULE$,none(),2147483647.0,0.0,999,fi,fr,null,list(),none());FM fm=new FM(0,gb);kB level=allocate(kB.class);put(level,kB.class,"c",Integer.MAX_VALUE);
  LY slot=allocate(LY.class);put(slot,LY.class,"a",3);put(slot,LY.class,"b",21);put(slot,LY.class,"c",fm);put(slot,LY.class,"d",none());put(slot,LY.class,"f",gb);put(slot,LY.class,"g",level);put(slot,LY.class,"h",list());return slot;
 }
 public static void main(String[]args)throws Exception{
  if(args.length!=2)throw new IllegalArgumentException("r27.jar simulation-dir");jar=Paths.get(args[0]).toRealPath();out=Paths.get(args[1]).toRealPath();
  if(!out.equals(Paths.get("docs/font-layout-audit-20261025/simulation").toRealPath()))throw new IllegalArgumentException("Exclusive simulation output");
  String loaded=Paths.get(Id.class.getProtectionDomain().getCodeSource().getLocation().toURI()).toRealPath().toString();if(!loaded.equals(jar.toString()))throw new AssertionError("Class identity");
  Field f=sun.misc.Unsafe.class.getDeclaredField("theUnsafe");f.setAccessible(true);unsafe=(sun.misc.Unsafe)f.get(null);
  Map<String,Object>identities=new LinkedHashMap<String,Object>();
  try(JarFile z=new JarFile(jar.toFile())){for(String[]e:new String[][]{{"default","bbc2.fnt"},{"classic","classic.fnt"},{"story12","story12.fnt"}}){byte[]b=bytes(z.getInputStream(z.getJarEntry(e[1])));CpuFont font=new CpuFont(b);fonts.put(e[0],font);identities.put(e[0],map("entry",e[1],"sha256",sha(b),"ascent",font.metrics.k,"padLeft",font.metrics.h,"lineHeight",font.metrics.i));}}
  StringBuilder ascii=new StringBuilder();for(int c=32;c<127;c++)ascii.append((char)c);fonts.get("classic").a(ascii);
  String jarSha=sha(Files.readAllBytes(jar));String jre=Paths.get(System.getProperty("java.home")).toRealPath().toString();
  if(System.getSecurityManager()!=null)throw new AssertionError("Existing manager");
  System.setSecurityManager(new SecurityManager(){
   String norm(String p){return Paths.get(p).toAbsolutePath().normalize().toString();}
   boolean allowedOutput(String p){String n=norm(p);return n.equals(out.toString())||n.startsWith(out.toString()+File.separator);}
   void refuse(String s){denials.add(s);throw new SecurityException(s);}
   @Override public void checkRead(String p){String n=norm(p);if(!n.equals(jar.toString())&&!n.startsWith(jre+File.separator)&&!allowedOutput(p))refuse("read:"+p);}
   @Override public void checkWrite(String p){if(!allowedOutput(p))refuse("write:"+p);}
   @Override public void checkDelete(String p){refuse("delete:"+p);}
   @Override public void checkExec(String p){refuse("exec:"+p);}
   @Override public void checkLink(String p){refuse("native:"+p);}
   @Override public void checkConnect(String h,int p){refuse("network");}
   @Override public void checkListen(int p){refuse("listen");}
   @Override public void checkAccept(String h,int p){refuse("accept");}
   @Override public void checkPermission(Permission p){if(p instanceof RuntimePermission&&(p.getName().equals("setSecurityManager")||p.getName().startsWith("loadLibrary.")||p.getName().equals("shutdownHooks")))refuse(p.toString());}
  });
  XK.MODULE$.a(aJB.MODULE$.h().d());XK.MODULE$.b(aJB.MODULE$.h().d());XK.MODULE$.c(aJB.MODULE$.h().d());XK.MODULE$.d(aJB.MODULE$.h().d());
  SN sn=sn();String name="宇宙育种探索先锋";
  begin("save-original-eight-cjk","Actual r27 LY.m/b -> Id; Unsafe synthetic slot; no parent or save service. Background anchor replayed from Mf.b, not full Mf frame.");sn.a("CosmoSaveMenuBG",0,0);LY slot=occupied(name);slot.b(sn);
  begin("name-original-eight-cjk","Actual r27 Mb.b -> Id. Mc/Ma constructors NOT called; synthetic name/RN/time fields; normal row3,21 from Mg.");sn.a("CosmoNameEntryMenuBG",0,0);Mc mc=allocate(Mc.class);Ma ma=allocate(Ma.class);put(mc,Mc.class,"f",name);put(mc,Mc.class,"b",RN.a.MODULE$);put(mc,Mc.class,"e",ma);new Mb(3,21,0,mc).b(sn);
  begin("item-classic8-selected","Actual registered r27 Lg.b/Lb.b -> ItemFont8 -> LayoutBridge; source anchors x176/y70 (selected row fixture), x136/y22. Category default10 remains separate.");sn.a("CosmoItemMenuBG",0,0);
  Lg lg=new Lg(supplier(176),supplier(70),supplier(new amr.d("三线圈     +")));ItemFont8.registerName(lg);lg.b(sn);
  Lb lb=new Lb(supplier(136),supplier(22),supplier(new amr.d("宇宙育种探索先锋宇宙育种探索先锋宇宙育种探索先锋宇宙育种")));ItemFont8.registerDescription(lb);lb.b(sn);
  begin("item-category-default10","Actual unregistered r27 category Lg.b -> default10 at original category x56/y62.");sn.a("CosmoItemMenuBG",0,0);new Lg(supplier(56),supplier(62),supplier(new amr.d("装备"))).b(sn);
  begin("story12-full-width-control","Actual r27 StoryFont12.drawStory -> SN -> original arr/arq, twenty 12px Han; no manual glyph positions.");String twenty="宇宙育种探索先锋宇宙育种探索先锋宇宙育种";if(twenty.length()!=20)throw new AssertionError();StoryFont12.drawStory(Id.MODULE$,sn,false,twenty,16,160,twenty);
  begin("default10-whole-line-control","Actual r27 Id boolean whole-line overload -> default10 -> arr/arq; same eight-Han text with native advance10, unlike Id fixed8 overload.");Id.MODULE$.a(sn,false,name,24,174);
  if(!denials.isEmpty())throw new AssertionError("Forbidden attempts "+denials);
  Map<String,Object>root=map("status","CPU_ONLY_NOT_GAME_SCREENSHOT","jar",jar.toString(),"jar_sha256",jarSha,"class_source",loaded,"fonts",identities,"scenarios",scenarios,"vertices",vertices,"guard_active",true,"forbidden_attempts",denials,"game_started",false,"gl_started",false,"save_accessed",false,"crt_verified",false,"coordinate_plane","256x224, SN y-up; screenTop=224-max(actual arq quad Y)","fixture_limits","No LY/Mc/Ma game constructors. Empty real XK/FI/Fr collections force original SORTIE 000% fallback. Background SN calls replay proven original anchors; does not execute full parent UI/clip. No atlas UV upload; CPU position vertices actual, source rectangles original FNT glyphs.");
  Files.write(out.resolve("cpu-recording.json"),json(root).getBytes(StandardCharsets.UTF_8));System.out.println("CPU_EVIDENCE_OK scenarios="+scenarios.size()+" actual_vertices="+vertices+" forbidden_attempts="+denials.size());
 }
}
