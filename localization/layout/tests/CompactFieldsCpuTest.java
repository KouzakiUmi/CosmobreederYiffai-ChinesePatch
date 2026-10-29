package PRG;
import java.io.*;
import java.lang.reflect.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.security.Permission;
import java.util.*;
import java.util.jar.*;
import cosmoloc.layout.FontAccess;

/** Actual patched consumers -> original arr/arq, synthetic state, no constructors
 * for game/save owners. Extends frozen evidence utility without changing it. */
@SuppressWarnings({"unchecked","rawtypes","removal"})
public final class CompactFieldsCpuTest {
    static int checks;static void check(boolean b,String s){checks++;if(!b)throw new AssertionError(s);}
    static String unescape(String s){return s.replace("\\n","\n").replace("\\r","\r").replace("\\t","\t").replace("\\\\","\\");}
    static SN sn(){final SN base=CpuEvidence.sn();return(SN)Proxy.newProxyInstance(CompactFieldsCpuTest.class.getClassLoader(),new Class[]{SN.class,FontAccess.class},(p,m,a)->{
        if(m.getName().equals("c")&&m.getParameterCount()==0)return "default";
        if(m.getName().equals("a")&&a!=null&&a.length==4&&a[1] instanceof Float){base.a((String)a[0],(Integer)a[2],(Integer)a[3]);return null;}
        if(m.getName().equals("a")&&a!=null&&a.length==5&&a[3] instanceof aBa){base.a((String)a[0],(Integer)a[1],(Integer)a[2],(String)a[4]);aBa color=(aBa)a[3];((Map)CpuEvidence.calls.get(CpuEvidence.calls.size()-1)).put("color_rgba",Arrays.asList(color.a(),color.e(),color.f(),color.g()));return null;}
        return m.invoke(base,a);
    });}
    static Lb description(String s){Lb w=new Lb(CpuEvidence.supplier(136),CpuEvidence.supplier(22),CpuEvidence.supplier(new amr.d(s)));ItemFont8.registerDescription(w);return w;}
    static void bg(SN sn,String name){sn.a(name,0,0);}
    static String joined(){StringBuilder b=new StringBuilder();for(Object o:CpuEvidence.calls){Map c=(Map)o;if("text".equals(c.get("kind")))b.append(c.get("text"));}return b.toString();}
    public static void main(String[] args)throws Exception{
        final Path jar=Paths.get(args[0]).toRealPath(),overlay=Paths.get(args[1]).toRealPath(),out=Paths.get(args[2]).toRealPath();
        final Path r28=Paths.get("localization/optimization/r28").toRealPath();
        final Path integrationTests=r28.resolve("integration/tests");
        boolean componentOutput=out.equals(r28.resolve("compact"));
        boolean freshRunOutput=out.startsWith(integrationTests)
                && integrationTests.relativize(out).getNameCount()==2
                && out.getFileName().toString().equals("compact");
        check(componentOutput||freshRunOutput,"exclusive component or integration/tests/<run>/compact output");
        check(Paths.get(LY.class.getProtectionDomain().getCodeSource().getLocation().toURI()).toRealPath().equals(overlay),"real final LY class source");
        Field u=sun.misc.Unsafe.class.getDeclaredField("theUnsafe");u.setAccessible(true);CpuEvidence.unsafe=(sun.misc.Unsafe)u.get(null);
        Map<String,Object> identities=new LinkedHashMap<String,Object>();
        try(JarFile z=new JarFile(jar.toFile())){for(String[] e:new String[][]{{"default","bbc2.fnt"},{"classic","classic.fnt"}}){byte[] b=CpuEvidence.bytes(z.getInputStream(z.getJarEntry(e[1])));CpuEvidence.fonts.put(e[0],new CpuEvidence.CpuFont(b));identities.put(e[0],CpuEvidence.map("entry",e[1],"sha256",CpuEvidence.sha(b)));}}
        StringBuilder fixed=new StringBuilder();for(int i=32;i<127;i++)fixed.append((char)i);CpuEvidence.fonts.get("classic").a(fixed);
        final String jre=Paths.get(System.getProperty("java.home")).toRealPath().toString();final List<String> denied=new ArrayList<String>();
        // Preload paths/classes by source roots; read permissions never include
        // game-data/save directories. This is a tripwire, not an OS sandbox.
        final Path evidence=Paths.get("docs/font-layout-audit-20261025/simulation/classes").toRealPath();
        System.setSecurityManager(new SecurityManager(){
            String n(String p){return Paths.get(p).toAbsolutePath().normalize().toString();}
            boolean under(String s,Path p){return s.equals(p.toString())||s.startsWith(p.toString()+File.separator);}
            void no(String s){denied.add(s);throw new SecurityException(s);}
            @Override public void checkRead(String p){String s=n(p);if(!s.equals(jar.toString())&&!s.equals(overlay.toString())&&!under(s,out)&&!under(s,evidence)&&!s.startsWith(jre+File.separator))no("read:"+p);}
            @Override public void checkWrite(String p){if(!under(n(p),out))no("write:"+p);}
            @Override public void checkDelete(String p){no("delete:"+p);}
            @Override public void checkExec(String p){no("exec:"+p);}
            @Override public void checkLink(String p){no("native:"+p);}
            @Override public void checkConnect(String h,int p){no("network");}
            @Override public void checkPermission(Permission p){if(p instanceof RuntimePermission&&(p.getName().equals("setSecurityManager")||p.getName().startsWith("loadLibrary.")||p.getName().equals("shutdownHooks")))no(p.toString());}
        });
        XK.MODULE$.a(aJB.MODULE$.h().d());XK.MODULE$.b(aJB.MODULE$.h().d());XK.MODULE$.c(aJB.MODULE$.h().d());XK.MODULE$.d(aJB.MODULE$.h().d());
        SN sn=sn();String eight="宇宙育种探索先锋";
        CpuEvidence.begin("save-three-slots","Actual final LY.b, original formatter, three synthetic slots pitch24; original Iu cursor. No Mf/save constructors.");bg(sn,"CosmoSaveMenuBG");
        for(int i=0;i<3;i++){LY slot=CpuEvidence.occupied(eight);CpuEvidence.put(slot,LY.class,"b",21-3*i);slot.b(sn);Iu cursor=CpuEvidence.allocate(Iu.class);CpuEvidence.put(cursor,Iu.class,"b",new aAJ(-7,-6));cursor.a(true);cursor.a(sn,slot,.05f);}
        Mc owner=CpuEvidence.allocate(Mc.class);Ma ma=CpuEvidence.allocate(Ma.class);ma.a(.05f); // real Ma.a(float) / f(), no owner constructor
        CpuEvidence.put(owner,Mc.class,"b",RN.a.MODULE$);CpuEvidence.put(owner,Mc.class,"e",ma);
        for(String name:new String[]{eight,"宇宙育种探索先","AB宇宙CD","ABCDEFGH",""}){
            CpuEvidence.put(owner,Mc.class,"f",name);
            CpuEvidence.begin("name-"+name.length()+"-"+(name.contains("宇")?"cjk":"ascii"),"Actual final Mb.b; immutable 64px field, gender x88, neighbouring x104; synthetic raw name.");bg(sn,"CosmoNameEntryMenuBG");new Mb(3,21,0,owner).b(sn);
            check(owner.m().equals(name),"render never mutates stored input");
        }
        // Real final Mn normal and highlighted paths, unchanged 8x8 highlight.
        Mn button=new Mn(24,128,'宇',owner);
        CpuEvidence.begin("letter-normal","Actual final Mn.b, synthetic CJK letter.");button.b(sn);List<Object> normal=new ArrayList<Object>(CpuEvidence.calls);
        CpuEvidence.begin("letter-selected","Actual final Mn.a, same eight-cell white fill plus classic8 coloured repaint.");button.a(sn,null);
        List<Object> selected=new ArrayList<Object>(CpuEvidence.calls);
        check(selected.size()==2,"highlight background plus text");check(((Map)normal.get(0)).get("quads").equals(((Map)selected.get(1)).get("quads")),"normal/selected exact same actual vertices");
        List<String> corpus=Files.readAllLines(out.resolve("item-corpus.tsv"),StandardCharsets.UTF_8);List<Object> corpusReport=new ArrayList<Object>();
        for(String line:corpus){String[] v=line.split("\t",-1);String text=unescape(v[3]);
            String actualName=unescape(v[2]);
            for(int nameY:new int[]{174,150,126,102,62})for(boolean equipped:new boolean[]{false,true}){
                String shown=equipped?aDJ.MODULE$.a(aDJ.MODULE$.b(actualName,8),8,' ')+"+":actualName;
                CpuEvidence.begin("item-name-"+v[0]+"-"+v[1]+"-"+nameY+"-"+equipped,"Frozen actual item name, final Lg.b; five proven Le y outputs. Equipped display uses exact original aDJ cut8/pad8/+ transform; no item action or stored name change.");bg(sn,"CosmoItemMenuBG");
                new Lg(CpuEvidence.supplier(136),CpuEvidence.supplier(nameY),CpuEvidence.supplier(new amr.d("ARMS"))).b(sn);
                Lg name=new Lg(CpuEvidence.supplier(176),CpuEvidence.supplier(nameY),CpuEvidence.supplier(new amr.d(shown)));ItemFont8.registerName(name);name.b(sn);
                check(joined().equals("ARMS"+shown),"formal dictionary name retained in rendered selected-name supplier");
            }
            Lb w=description(text);CpuEvidence.begin("item-corpus-"+v[0]+"-"+v[1],"Frozen "+v[0]+" dictionary item description, actual final Lb.b full supplier before legacy q14.");bg(sn,"CosmoItemMenuBG");w.b(sn);
            List<Object> calls=CpuEvidence.calls;String joined=joined();int count=0;String role="";for(Object o:calls){Map c=(Map)o;if("text".equals(c.get("kind"))){count++;role=(String)c.get("font");}}
            String original=text.replace("|","").replace("\n","").replace("\r","");
            String[] fullSmall=ItemFont8.wrap(CpuEvidence.fonts.get("classic"),text,112);
            int pages=fullSmall.length>3?(fullSmall.length+1)/2:1;
            if(pages>1){
                StringBuilder all=new StringBuilder();
                for(int page=0;page<pages;page++){
                    if(page>0){w.a(Math.max(8f,Math.min(20f,text.length()*0.35f/pages))+.001f);CpuEvidence.begin("item-corpus-"+v[0]+"-"+v[1]+"-page-"+page,"Actual final Lb.a(float) and draw complete overheight source.");bg(sn,"CosmoItemMenuBG");w.b(sn);}
                    // Use the minimum guaranteed 8s dwell below for this shipped
                    // short overflow. Each page's actual content must be intact.
                    String content=joined();String suffix=(page+1)+"/"+pages;
                    if(page>0&&!content.endsWith(suffix))throw new AssertionError("corpus overflow dwell expectation "+v[1]+content);
                    check(content.endsWith(suffix),"visible page counter");all.append(content.substring(0,content.length()-suffix.length()));
                }
                check(all.toString().equals(original),"paginated corpus full conservation "+v[0]+v[1]);
            }else check(joined.equals(original),"static corpus full conservation "+v[0]+v[1]);
            check(count<=3,"each visible corpus page fits actual slot");
            corpusReport.add(CpuEvidence.map("variant",v[0],"key",v[1],"lines",fullSmall.length,"pages",pages,"role",role,"text",text));
        }
        // Full long-description cycle, through real patched Lb.a(float), with
        // page-one reset after source changes and no premature page transition.
        String longText=eight+eight+eight+eight+eight+eight+eight+eight;
        Lb longWidget=description(longText);Set<String> pages=new LinkedHashSet<String>();
        String[] expected=ItemFont8.wrap(CpuEvidence.fonts.get("classic"),longText,112);int pageCount=(expected.length+1)/2;
        for(int p=0;p<pageCount;p++){CpuEvidence.begin("item-overheight-page-"+p,"Actual final Lb update/draw; >3 lines only, 8..20s dwell; complete labelled page cycle.");bg(sn,"CosmoItemMenuBG");if(p>0)longWidget.a(8.01f);longWidget.b(sn);String all=joined();pages.add(all);check(all.endsWith((p+1)+"/"+pageCount),"page progression "+p);}
        check(pages.size()==pageCount,"all long pages reachable");
        longWidget.a(8.01f);CpuEvidence.begin("item-overheight-loop","Actual final update wraps to page1.");longWidget.b(sn);check(joined().endsWith("1/"+pageCount),"page cycle complete");
        longWidget.a(1f);CpuEvidence.begin("item-selection-reset","Different full source resets page clock in same registered widget.");ItemFont8.drawDescription(longWidget,sn,"宇宙");check(joined().equals("宇宙"),"source change resets without input side effect");
        // Actual Ld42/aag/aab/Le supplier geometry; no apr/game constructors.
        Le le=CpuEvidence.allocate(Le.class);aag selector=CpuEvidence.allocate(aag.class);CpuEvidence.put(le,Le.class,"d",selector);CpuEvidence.put(selector,aag.class,"a",le);
        aEO<Integer> ys=CpuEvidence.list();int[] rows={21,18,15,12,7};for(int i=4;i>=0;i--)ys=ys.b((Integer)Le.class.getDeclaredMethod("a",int.class).invoke(null,rows[i]));CpuEvidence.put(le,Le.class,"q",ys);CpuEvidence.put(le,Le.class,"r",136);
        final List<int[]> positions=new ArrayList<int[]>();aCg mapped=(aCg)Ld.MODULE$.n().a((azz)(t->{try{aBa tuple=(aBa)t;int x=(Integer)tuple.f(),y=(Integer)tuple.g();Lc icon=CpuEvidence.allocate(Lc.class);CpuEvidence.put(icon,Lc.class,"a",x);CpuEvidence.put(icon,Lc.class,"b",y);CpuEvidence.put(icon,Lc.class,"c",(azz)(apr->CpuEvidence.none()));positions.add(new int[]{x,y});return icon;}catch(Exception e){throw new RuntimeException(e);}}));
        aEO<Lc> icons=mapped.g();CpuEvidence.put(le,Le.class,"w",icons);check(icons.e()==42,"real42 table");String[] labels={"ARMS","HEAD","BODY","SPCL","USE"};
        for(int i=0;i<42;i++){selector.b(new aAw<Object>(i));int y=(Integer)Le.class.getDeclaredMethod("a",Le.class).invoke(null,le);CpuEvidence.begin("item-selector-"+i,"Actual Ld42 -> aag/aab -> Le y supplier -> final Lg; real empty Lc draw; conservative 16x16 icon boxes checked by pixel replay.");bg(sn,"CosmoItemMenuBG");
            for(int j=0;j<5;j++)((Lg)Le.class.getDeclaredMethod("a",Le.class,aAJ.class).invoke(null,le,new aAJ(new amr.d(labels[j]),ys.m(j)))).b(sn);
            Lg name=new Lg(CpuEvidence.supplier(176),CpuEvidence.supplier(y),CpuEvidence.supplier(new amr.d("三线圈     +")));ItemFont8.registerName(name);name.b(sn);
            for(int j=0;j<42;j++)icons.m(j).b(sn);
        }
        Lb bound=new Lb(CpuEvidence.supplier(136),CpuEvidence.supplier(22),CpuEvidence.supplier(new amr.d(longText)));ItemFont8.registerDescription(bound,le);
        selector.b(new aAw<Object>(0));CpuEvidence.begin("item-owner-first","Real selected-object identity resets overflow clock.");bound.b(sn);String first=joined();
        bound.a(7.99f);CpuEvidence.begin("item-owner-dwell","No transition before full eight-second dwell.");bound.b(sn);check(joined().equals(first),"minimum dwell held");
        bound.a(.03f);CpuEvidence.begin("item-owner-next","Original widget update crosses dwell boundary.");bound.b(sn);check(joined().endsWith("2/"+pageCount),"elapsed second page");
        selector.b(new aAw<Object>(1));CpuEvidence.begin("item-owner-same-source-reset","Two different selected original Lc objects, identical description, reset to page1.");bound.b(sn);check(joined().equals(first),"selection identity reset even when full source unchanged");
        arp body=CpuEvidence.fonts.get("default");
        for(String sample:new String[]{eight+"，"+eight+"。","ALPHA BETA GAMMA DELTA","COMMUNICATE AND DETECT SECRETS!"})for(int limit:new int[]{79,80,81,111,112,113}){
            String[] wrapped=ItemFont8.wrap(body,sample,limit);StringBuilder retained=new StringBuilder();
            for(String row:wrapped){check(ItemFont8.width(body,row)<=limit,"exact measured boundary");check(row.isEmpty()||"，。！？；：、）】》".indexOf(row.charAt(0))<0,"no added prohibited line start");retained.append(row);}
            check(retained.toString().equals(sample),"wrap retains English spaces and CJK punctuation");
        }
        check(denied.isEmpty(),"forbidden attempts zero");
        Map<String,Object> root=CpuEvidence.map("status","FINAL_CLASS_CPU_ONLY_NOT_GAME_SCREENSHOT","jar_sha256",CpuEvidence.sha(Files.readAllBytes(jar)),"overlay_sha256",CpuEvidence.sha(Files.readAllBytes(overlay)),"fonts",identities,"scenarios",CpuEvidence.scenarios,"vertices",CpuEvidence.vertices,"guard_active",true,"forbidden_attempts",denied,"game_started",false,"save_accessed",false,"corpus",corpusReport,"corpus_input_sha256",CpuEvidence.sha(Files.readAllBytes(out.resolve("item-corpus.tsv"))),"icon_position_source","actual Ld.n table in item-selector scenarios","assertions",checks,"fixture_limits","Synthetic name/save owners; no constructors or save services; no full parent clip or GPU/shader/CRT/input. Original Iu geometry retained. Mn highlight intentionally under text. Lc IconEmpty real draws plus conservative full16px icon-rectangle exclusion, not equipped icon action tests.");
        Files.write(out.resolve("cpu-recording.json"),CpuEvidence.json(root).getBytes(StandardCharsets.UTF_8));
        System.out.println("COMPACT_CPU_OK scenarios="+CpuEvidence.scenarios.size()+" vertices="+CpuEvidence.vertices+" assertions="+checks+" forbidden_attempts="+denied.size());
    }
}
