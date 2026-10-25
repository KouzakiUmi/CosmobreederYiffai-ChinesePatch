package PRG;

import cosmoloc.layout.FontAccess;
import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.security.MessageDigest;
import java.security.Permission;
import java.util.*;

/** Test-only fixture. No game entry point, textures, save service or runtime patch. */
public final class SaveDrawingProbe {
    static sun.misc.Unsafe unsafe;
    static arp font;
    static final List<Object> scenarios = new ArrayList<Object>();
    static final Set<String> executed = new TreeSet<String>();
    static final List<String> denied = new ArrayList<String>();
    static Path output;
    static Map<String,Object> current;
    static List<Object> calls;
    static int checks;

    /** ONLY s() is substituted: original s() calls Mg -> Hi (save service) on every access. */
    public static final class FixtureMenu extends Mf {
        aEO<Me> slots;
        private FixtureMenu() { super(null, 0); throw new AssertionError("never construct"); }
        @Override public aEO<Me> s() { return slots; }
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 4) throw new IllegalArgumentException("candidate.jar bbc2.fnt bbc2-cjk-10.png output-directory");
        Path jar = Paths.get(args[0]).toRealPath();
        Path fnt = Paths.get(args[1]).toRealPath();
        Path png = Paths.get(args[2]).toRealPath();
        output = Paths.get(args[3]).toRealPath();
        Path allowedOutput = Paths.get("localization/work/layout-drawing-probe").toRealPath();
        if (!output.equals(allowedOutput)) throw new IllegalArgumentException("output must be exclusive probe directory");
        String loaded = Paths.get(Mf.class.getProtectionDomain().getCodeSource().getLocation().toURI()).toRealPath().toString();
        check(loaded.equals(jar.toString()) && loaded.endsWith(".jar"), "real game classes must load from candidate JAR");
        Field singleton = sun.misc.Unsafe.class.getDeclaredField("theUnsafe"); singleton.setAccessible(true);
        unsafe = (sun.misc.Unsafe) singleton.get(null);
        Constructor<aqX> file = aqX.class.getDeclaredConstructor(String.class, apO.a.class); file.setAccessible(true);
        arp.a data = new arp.a(file.newInstance(fnt.toString(), null), false);
        font = allocate(arp.class); put(font, arp.class, "a", data);
        Map<String,Object> identity = map("role", "default", "fnt_sha256", sha(fnt), "png_sha256", sha(png),
            "ascent", data.k, "padLeft", data.h, "scaleX", data.o, "scaleY", data.p, "lineHeight", data.i);
        String jarSha = sha(jar);
        final String jre = Paths.get(System.getProperty("java.home")).toAbsolutePath().normalize().toString();
        // Defense-in-depth: only JRE, exact candidate/font inputs and this test directory may be read.
        if (System.getSecurityManager() != null) throw new IllegalStateException("never replace an existing security manager");
        if (Files.isSymbolicLink(output)) throw new IllegalStateException("output must not be a symlink");
        System.setSecurityManager(new SecurityManager() {
            @Override public void checkPermission(Permission p) {
                if (p instanceof java.nio.file.LinkPermission) refuse("link creation");
                if (p instanceof RuntimePermission && (p.getName().startsWith("exitVM") || p.getName().equals("setSecurityManager")
                        || p.getName().startsWith("loadLibrary.") || p.getName().equals("shutdownHooks"))) refuse(p.toString());
            }
            String normalized(String p) { return Paths.get(p).toAbsolutePath().normalize().toString(); }
            boolean inOutput(String p) { return normalized(p).startsWith(output.toString() + File.separator) || normalized(p).equals(output.toString()); }
            @Override public void checkRead(String p) {
                String n = normalized(p);
                if (!(n.equals(jar.toString()) || n.equals(fnt.toString()) || n.equals(png.toString()) || n.startsWith(jre + File.separator) || inOutput(p))) refuse("read:" + p);
            }
            @Override public void checkWrite(String p) { if (!inOutput(p)) refuse("write:" + p); }
            @Override public void checkDelete(String p) { refuse("delete:" + p); }
            @Override public void checkExec(String p) { refuse("exec:" + p); }
            @Override public void checkLink(String p) { refuse("native:" + p); }
            @Override public void checkConnect(String h, int p) { refuse("network:" + h); }
            @Override public void checkListen(int p) { refuse("listen"); }
            @Override public void checkAccept(String h, int p) { refuse("accept"); }
            @Override public void checkWrite(FileDescriptor fd) { if(fd!=FileDescriptor.out && fd!=FileDescriptor.err) refuse("unbound write fd"); }
            @Override public void checkRead(FileDescriptor fd) { if(fd!=FileDescriptor.in) refuse("unbound read fd"); }
            void refuse(String p) { denied.add(p); throw new SecurityException(p); }
        });
        final SecurityManager guard=System.getSecurityManager();
        guardReject(()->guard.checkRead("C:/SteamLibrary/steamapps/common/Cosmobreeder Yiffai/cosmo.sav"));
        guardReject(()->guard.checkWrite("C:/SteamLibrary/steamapps/common/Cosmobreeder Yiffai/cosmo.sav"));
        guardReject(()->guard.checkWrite(output.getParent().resolve("forbidden-write").toString()));
        guardReject(()->guard.checkExec("probe-never-executed"));
        guardReject(()->guard.checkConnect("127.0.0.1",1));
        guardReject(()->guard.checkLink("probe-never-loaded"));
        guardReject(()->guard.checkPermission(new RuntimePermission("setSecurityManager")));
        guardReject(()->guard.checkPermission(new RuntimePermission("shutdownHooks")));
        final List<String> guardSelfTest=new ArrayList<String>(denied); denied.clear();
        // Original formatter's jA initializer stringifies aga via XK's normally boot-populated registry.
        // Empty REAL vectors are an explicit test fixture, not a game bootstrap or fake formatter.
        XK.MODULE$.a(aJB.MODULE$.h().d()); XK.MODULE$.b(aJB.MODULE$.h().d());
        XK.MODULE$.c(aJB.MODULE$.h().d()); XK.MODULE$.d(aJB.MODULE$.h().d());
        SN sn = recording();
        FixtureMenu menu = allocate(FixtureMenu.class);
        Iu selector = new Iu(menu, new aAR(-7,-6), null, 0, false);
        selector.a(true);
        put(menu, Mf.class, "e", selector); put(menu, Mf.class, "h", Mo.MODULE$);
        String[] labels = {"输入姓名", "删除存档", "卡片图鉴", "怪物图鉴"};
        for (int i=0;i<4;i++) put(menu, Mf.class, new String[]{"k","l","m","n"}[i], action(labels[i],24,94-16*i));
        LY first = occupied(menu, 0, "宇宙育种探索先锋", 255);
        LY mixed = occupied(menu, 2, "宇宙AB探索CD", 170);
        LX empty = new LX(3,18,1);
        menu.slots = list(first,empty,mixed);
        aAJ<String,String> originalRows = first.m();
        executed.add("PRG.LY.m() actual formatter");
        check(originalRows.a().contains("LVL025 TRY999"), "actual original level25 and TRY999");
        check(originalRows.a().endsWith("7FFF") && originalRows.e().endsWith("FFFF"), "actual original 8hex not a date");
        check(first.n().e()==8, "eight synthetic flags retained");
        check(menu.R().e()==7 && menu.Q().e()==0, "original Mo normal R7/Q0");
        check(!SaveMenuLayout.prototypeEnabled(), "default prototype off");
        for (int index : new int[]{0,1,2,3,4,5,6}) {
            frame(menu,sn,"normal-off-"+index,false,index,index<3?index:0,0f,null);
            frame(menu,sn,"normal-on-"+index,true,index,index<3?index:0,0f,null);
        }
        // Real LV R/Q: target2 only plus IG background, two action buttons.
        LV lv = allocate(LV.class);
        put(lv,LV.class,"a",2); put(lv,LV.class,"b",menu);
        final Method caption=LV.class.getDeclaredMethod("a",SN.class);
        if(!Modifier.isStatic(caption.getModifiers()) || caption.getReturnType()!=void.class) throw new AssertionError("exact LV caption descriptor");
        put(lv,LV.class,"d",new IG(s -> { try { caption.invoke(null,s); } catch(ReflectiveOperationException e) { throw new IllegalStateException("real LV caption",e); } return aKd.a; }));
        put(lv,LV.class,"e",action("取消",32,78)); put(lv,LV.class,"f",action("删除",32,62));
        put(menu,Mf.class,"h",lv);
        check(menu.R().e()==2 && menu.Q().e()==2 && menu.Q().m(0)==mixed, "original LV Q retains deletion target only plus IG");
        executed.add("PRG.LV.a(Mf)/b(Mf), PRG.LW target filter");
        float visible=0, hidden=0;
        for(int t=0;t<20;t++) if(Id.MODULE$.a(t,5.0)) hidden=t; else visible=t;
        check(Id.MODULE$.a(hidden,5.0) && !Id.MODULE$.a(visible,5.0),"both actual blink phases");
        for(int index=0;index<2;index++) {
            frame(menu,sn,"delete-off-visible-"+index,false,index,2,visible,null);
            frame(menu,sn,"delete-on-visible-"+index,true,index,2,visible,null);
            frame(menu,sn,"delete-on-hidden-"+index,true,index,2,hidden,null);
        }
        // Error must travel through real Mf.b finally; subsequent direct LX must be original/unfiltered.
        put(menu,Mf.class,"h",Mo.MODULE$);
        LY tooLong=occupied(menu,0,"宇宙育种探索先锋宇",255);
        menu.slots=list(tooLong,empty,mixed);
        frame(menu,sn,"name-nine-cjk-overflow",true,0,0,0f,"Save candidate field overflow");
        calls=new ArrayList<Object>(); current=map("id","after-error-direct-LX","prototype",true,"selected_index",null,"selected_slot",1,"status","PASS","calls",calls);
        scenarios.add(current); empty.b(sn);
        check(calls.size()>2 && !hasText("[无数据]"),"Mf finally cleared candidate context after overflow");
        SaveMenuLayout.disablePrototype();
        check(denied.isEmpty(),"no forbidden IO/native/process attempt");
        Map<String,Object> root=map("schema_version",1,"width",256,"height",224,"font",identity,
            "candidate_jar_sha256",jarSha,"class_source",loaded,"coordinates","raw SN y-up; quads screenTop derived at height224; bounds are candidates NOT actual clip",
            "fixture_boundary","Only FixtureMenu.s is overridden. Mf/LY/LV/arp constructors bypassed with test-only Unsafe; LY.m/b, LX.b, Mf.b,R/Q, LV title callback, arr CPU glyph runs and Iu original methods actually execute. XK uses synthetic empty real registry vectors; FI/Fr contain empty real collections so original LY.m uses SORTIE 000% fallback. IA labels are synthetic fixtures, not game localization verification.",
            "original_methods_executed",new ArrayList<String>(executed),"checks_passed",checks,"guard_active",System.getSecurityManager()==guard,
            "guard_self_test_expected_rejections",guardSelfTest,"positive_scenario_denied_operations",denied.size(),"forbidden_attempts",denied,"scenarios",scenarios);
        Path temporary=output.resolve("save-drawing-recording.pending.json"), target=output.resolve("save-drawing-recording.json");
        if(!temporary.toAbsolutePath().normalize().getParent().equals(output) || !target.toAbsolutePath().normalize().getParent().equals(output))
            throw new IllegalStateException("verified output targets changed");
        Files.write(temporary,json(root).getBytes(StandardCharsets.UTF_8));
        Files.move(temporary,target,StandardCopyOption.ATOMIC_MOVE,StandardCopyOption.REPLACE_EXISTING);
        System.out.println("SaveDrawingProbe PASS checks="+checks+" scenarios="+scenarios.size()+" output=save-drawing-recording.json");
    }

    static LY occupied(Mf parent,int id,String name,int flags) throws Exception {
        FI fi = new FI(azQ.MODULE$.b().d(),azQ.MODULE$.b().d(),azQ.MODULE$.b().d(),azQ.MODULE$.b().d(),azQ.MODULE$.a().a(),azQ.MODULE$.a().a());
        Fr fr = allocate(Fr.class); put(fr,Fr.class,"e",azQ.MODULE$.a().a());
        GB gb = new GB(name,RN.a.MODULE$,none(),2147483647.0,0.0,999,fi,fr,null,list(),none());
        FM fm = new FM(id,gb);
        kB level = allocate(kB.class); put(level,kB.class,"c",Integer.MAX_VALUE);
        LY slot=allocate(LY.class);
        put(slot,LY.class,"a",3); put(slot,LY.class,"b",21-id*3); put(slot,LY.class,"c",fm);
        put(slot,LY.class,"d",new aAw<Mf>(parent)); put(slot,LY.class,"f",gb); put(slot,LY.class,"g",level);
        String[] names={"Arrow","Star","Triangle","Waves","Circle","Cross","Square","Heart"};
        aEO<aAJ<String,Object>> symbols=list();
        for(int i=7;i>=0;i--) symbols=symbols.b(new aAJ<String,Object>(names[i],Boolean.valueOf((flags&(1<<i))!=0)));
        put(slot,LY.class,"h",symbols);
        return slot;
    }
    static IA action(String text,int x,int y) {
        SL label=new SL(text,"probe-only");
        return new IA(x,y,label,()->label,null,"default",IB.MODULE$.b());
    }
    static void frame(FixtureMenu menu,SN sn,String id,boolean on,int selected,int slot,float time,String expectedError) {
        if(on) SaveMenuLayout.configurePrototype(); else SaveMenuLayout.disablePrototype();
        menu.e().b(new aAw<Object>(Integer.valueOf(selected))); menu.e().a(time);
        calls=new ArrayList<Object>();
        current=map("id",id,"prototype",on,"selected_index",selected,"selected_slot",slot,"time",time,
            "mode",menu.m().getClass().getName(),"calls",calls,"expected_error",expectedError);
        scenarios.add(current);
        try {
            menu.b(sn); current.put("status","PASS");
            check(expectedError==null,"expected overflow must fail");
        } catch(IllegalStateException e) {
            current.put("status",expectedError!=null&&e.getMessage().contains(expectedError)?"EXPECTED_REJECTION":"FAIL");
            current.put("error",e.toString());
            if(expectedError==null || !e.getMessage().contains(expectedError)) throw e;
            checks++;
        }
        if(expectedError==null) {
            if(on) check(countResource("BlackFill")==1,"one candidate panel");
            else check(countResource("BlackFill")==0,"off leaves original panel untouched");
            if(on && menu.m() instanceof Mo && slot==1) check(hasText("[无数据]"),"empty actual LX hook");
            if(on && menu.m() instanceof Mo && slot!=1) {
                check(hasText(slot==0?"宇宙育种探索先锋":"宇宙AB探索CD"),"full original LY hook preserves raw name");
                check(countPrefix("ClassicHUDZenerSymbols")== (slot==0?8:4),"exact flag image count");
            }
            check(calls.size()>0,"real drawing emitted calls");
        }
    }
    static SN recording() {
        return (SN)Proxy.newProxyInstance(SaveDrawingProbe.class.getClassLoader(),new Class<?>[]{SN.class,FontAccess.class},(p,m,a)->{
            if(m.getName().equals("cosmo$layoutFont")) return font;
            if(m.getDeclaringClass()==Object.class) {
                if(m.getName().equals("hashCode")) return System.identityHashCode(p);
                if(m.getName().equals("equals")) return p==a[0];
                return "RecordingSN";
            }
            if(m.getName().equals("b") && m.getParameterCount()==0) return "default";
            if(m.getReturnType()==void.class) {
                Map<String,Object> call=map("scenario",current.get("id"),"selected_slot",current.get("selected_slot"),
                    "method",m.toGenericString(),"args",a==null?Collections.emptyList():Arrays.asList(a));
                List<String> stack=new ArrayList<String>();
                for(StackTraceElement f:Thread.currentThread().getStackTrace()) if(f.getClassName().startsWith("PRG.") && !f.getClassName().startsWith("PRG.SaveDrawingProbe")) {
                    String method=f.getClassName()+"."+f.getMethodName(); stack.add(method); executed.add(method);
                }
                call.put("original_methods",stack);
                if(m.getName().equals("a") && a!=null && a.length>=3 && a[0] instanceof String) {
                    if(a.length==4 && a[3] instanceof String) {
                        call.put("kind","text"); call.put("text",a[0]); call.put("x",a[1]); call.put("y",a[2]); call.put("font",a[3]);
                        quads(call,(String)a[0],(Integer)a[1],(Integer)a[2]);
                    } else if(a.length==3 || a.length==5) {
                        String name=(String)a[0]; call.put("kind",a.length==5?"rect":"image"); call.put("name",name); call.put("x",a[1]); call.put("y",a[2]);
                        int w=a.length==5?(Integer)a[3]:name.equals("CosmoSaveMenuBG")?256:8;
                        int h=a.length==5?(Integer)a[4]:name.equals("CosmoSaveMenuBG")?224:8;
                        call.put("width",w); call.put("height",h);
                        call.put("bounds_candidate",map("left",a[1],"bottom",a[2],"width",w,"height",h,"screenTop",224-(Integer)a[2]-h,"basis",a.length==5?"raw SN dimensions":"asset candidate dimensions; not clip"));
                    } else call.put("kind","other");
                } else call.put("kind","other");
                calls.add(call); return null;
            }
            // Never silently return fake resources or allow unhandled rendering branches.
            throw new AssertionError("Unhandled RecordingSN request: "+m);
        });
    }
    static void quads(Map<String,Object> call,String text,int x,int y) {
        List<Object> quads=new ArrayList<Object>(); double pen=x;
        double left=Double.POSITIVE_INFINITY,top=left,right=-left,bottom=-left;
        // Execute the ORIGINAL CPU glyph-run builder: no texture/cache/GL methods are invoked.
        arr layout=new arr();
        layout.a(font,text,0,text.length(),new ara(1,1,1,1),0,8,false,null);
        int count=0;
        for(int r=0;r<layout.a.b;r++) {
            arr.a run=layout.a.a(r); pen=x+run.c;
            for(int i=0;i<run.a.b;i++) {
                arp.b g=run.a.a(i); pen+=run.b.a[i];
                check(count<text.length() && g.a==text.charAt(count),"original CPU arr glyph identity");
                double qx=Math.round(pen+g.j), qt=224-Math.round(y+font.a.k+run.d+g.k+g.e);
                quads.add(map("codepoint",g.a,"srcX",g.b,"srcY",g.c,"page",g.o,"width",g.d,"height",g.e,"x",qx,"screenTop",qt,
                    "original_arr_advance",run.b.a[i],"original_arr_run_x",run.c,"original_arr_run_y",run.d));
                if(g.d>0 && g.e>0) { left=Math.min(left,qx); top=Math.min(top,qt); right=Math.max(right,qx+g.d); bottom=Math.max(bottom,qt+g.e); }
                count++;
            }
        }
        check(count==text.length(),"original CPU arr retained every recorded code unit");
        executed.add("PRG.arr.a(arp,CharSequence,int,int,ara,float,int,boolean,String) original CPU glyph layout");
        call.put("quads",quads);
        call.put("bounds_candidate",left==Double.POSITIVE_INFINITY?null:map("left",left,"top",top,"right",right,"bottom",bottom,"basis","original arr CPU glyph runs/advances + arq quad formula; not GL/clip"));
    }
    static int countResource(String name) { int n=0; for(Object o:calls) if(name.equals(((Map<?,?>)o).get("name"))) n++; return n; }
    static int countPrefix(String name) { int n=0; for(Object o:calls) { Object v=((Map<?,?>)o).get("name"); if(v instanceof String && ((String)v).startsWith(name)) n++; } return n; }
    static boolean hasText(String text) { for(Object o:calls) if(text.equals(((Map<?,?>)o).get("text"))) return true; return false; }
    @SuppressWarnings("unchecked") static <T> azK<T> none(){return (azK<T>)(Object)azI.MODULE$;}
    @SafeVarargs @SuppressWarnings("unchecked") static <T> aEO<T> list(T... items){aEO<T> r=(aEO<T>)(Object)aFC.MODULE$;for(int i=items.length-1;i>=0;i--)r=r.b(items[i]);return r;}
    static <T>T allocate(Class<T> type)throws Exception{return type.cast(unsafe.allocateInstance(type));}
    static void put(Object o,Class<?> owner,String name,Object value)throws Exception {Field f=owner.getDeclaredField(name);f.setAccessible(true);f.set(o,value);}
    static void guardReject(Runnable operation) { try { operation.run(); } catch(SecurityException expected) { checks++; return; } throw new AssertionError("guard negative test allowed forbidden operation"); }
    static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);checks++;}
    static String sha(Path p)throws Exception {MessageDigest d=MessageDigest.getInstance("SHA-256");try(InputStream in=Files.newInputStream(p)){byte[]b=new byte[8192];for(int n;(n=in.read(b))>=0;)d.update(b,0,n);}StringBuilder s=new StringBuilder();for(byte b:d.digest())s.append(String.format("%02x",b&255));return s.toString();}
    static Map<String,Object> map(Object... pairs){Map<String,Object> m=new LinkedHashMap<String,Object>();for(int i=0;i<pairs.length;i+=2)m.put((String)pairs[i],pairs[i+1]);return m;}
    static String json(Object o){
        if(o==null)return "null"; if(o instanceof Number || o instanceof Boolean)return o.toString();
        if(o instanceof Map){StringBuilder s=new StringBuilder("{");for(Map.Entry<?,?>e:((Map<?,?>)o).entrySet()){if(s.length()>1)s.append(',');s.append(json(e.getKey())).append(':').append(json(e.getValue()));}return s.append('}').toString();}
        if(o instanceof Iterable){StringBuilder s=new StringBuilder("[");for(Object v:(Iterable<?>)o){if(s.length()>1)s.append(',');s.append(json(v));}return s.append(']').toString();}
        String v=o.toString();StringBuilder s=new StringBuilder("\"");for(int i=0;i<v.length();i++){char c=v.charAt(i);if(c=='"'||c=='\\')s.append('\\').append(c);else if(c<32)s.append(String.format("\\u%04x",(int)c));else s.append(c);}return s.append('"').toString();
    }
}
