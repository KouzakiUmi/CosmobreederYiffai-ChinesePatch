import PRG.*;
import cosmoloc.layout.DialogueGrid;
import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;

/** Actual parser -> anp -> amn/amw -> jo callback -> Id/SN -> arr/FNT.
 * No Main, GL, texture/resource construction or game/save IO. CPU fonts use
 * their genuine FNT parser, overriding ONLY the texture upload hook.
 * CLI: vsn.tsv dingbats.fnt story12.fnt bbc2.fnt [expected-census.properties]
 * Four arguments enforce frozen r27 census. Candidate builds MUST provide
 * independent expected commands/han_commands/han properties as argument five;
 * optional before_blank can seal the candidate's pre-fix blank count as well.
 * Run with freshly compiled helpers FIRST, then the matching candidate JAR;
 * StoryFont12.FONT_SHA256 must match that candidate's explicitly staged pin.
 */
@SuppressWarnings({"rawtypes","unchecked"})
public final class PatternSymbolsTest {
    static long checks, frames, arrRuns, glyphs;
    static int commands, hanCommands, han, beforeBlank, afterBlank, pages;
    static final List<Draw> draws = new ArrayList<Draw>();
    static final Map<String,CpuFont> fonts = new HashMap<String,CpuFont>();
    static final Method CALLBACK;
    static { try { CALLBACK=jo.class.getMethod("a",jo.class,String.class,azK.class,amn.class,int.class,String.class,boolean.class); }
             catch(Exception e) { throw new AssertionError(e); } }
    static final class Draw {
        final String text,role; final int x,y;
        Draw(Object[] a) { text=(String)a[0];x=(Integer)a[1];y=(Integer)a[2];role=(String)a[3]; }
    }
    static final SN REC=(SN)Proxy.newProxyInstance(PatternSymbolsTest.class.getClassLoader(),new Class[]{SN.class},(p,m,a)->{
        if(m.getName().equals("b")&&m.getParameterCount()==0)return "default";
        if(m.getName().equals("a")&&a!=null&&a.length==4&&a[0] instanceof String)draws.add(new Draw(a));
        if(m.getReturnType()==boolean.class)return false;
        if(m.getReturnType()==int.class)return 0;
        if(m.getReturnType()==float.class)return 0f;
        return null;
    });
    static void check(boolean v,String why) { checks++; if(!v)throw new AssertionError(why); }
    static String sha(byte[] b)throws Exception {
        StringBuilder s=new StringBuilder();for(byte v:MessageDigest.getInstance("SHA-256").digest(b))s.append(String.format("%02x",v&255));return s.toString();
    }
    public static final class CpuFile extends aqX {
        CpuFile(Path p) { super();a=p.toFile(); }
        @Override public InputStream e() { try{return new FileInputStream(a);}catch(IOException e){throw new UncheckedIOException(e);} }
        @Override public aqX d(){return new CpuFile(a.toPath().toAbsolutePath().getParent());}
        @Override public aqX b(String child){return new CpuFile(a.toPath().resolve(child));}
    }
    public static final class CpuFont extends arp {
        final arp.a data;
        CpuFont(Path p){this(new arp.a(new CpuFile(p),false));}
        CpuFont(arp.a d){super(d,new arI(),false);data=d;}
        @Override protected void a(arp.a d){/* NEVER execute texture loading. */}
    }
    static Object unsafe()throws Exception {
        Field f=Class.forName("sun.misc.Unsafe").getDeclaredField("theUnsafe");f.setAccessible(true);return f.get(null);
    }
    static aEO parse(String root,String script)throws Exception {
        Object u=unsafe();Class<?> t=u.getClass();
        amS.a parser=(amS.a)t.getMethod("allocateInstance",Class.class).invoke(u,amS.a.class);
        Field source=amS.a.class.getDeclaredField("a");long off=(Long)t.getMethod("objectFieldOffset",Field.class).invoke(u,source);
        t.getMethod("putObject",Object.class,long.class,Object.class).invoke(u,parser,off,root);
        auK input=auL.MODULE$.a(script,(azz<String,auI>)(s->new auC(s)));
        auG result=ava.MODULE$.a(input,(azz<auN<Object>,auN<aEO<amZ>>>)(s->parser.E(s)),ava.MODULE$.a(),ava.MODULE$.b(),ava.MODULE$.c());
        return (aEO)result.a().e();
    }
    static aEO empty(){return aFC.MODULE$;}
    static anh state(double time,azK active,aEO pending){return new anh(null,time,active,pending,empty(),null,true,null,null,empty(),(azK)azI.MODULE$);}
    static final amX META=new amX(null,Ol.MODULE$,Om.MODULE$,null);
    static String oracle(String s) {
        // Independent arithmetic oracle; also ensures no current/full-page indexing.
        StringBuilder b=new StringBuilder();
        for(char c:s.toCharArray()) {
            if(c==' '||c=='\n'||c=='\r'||c=='\t'||(c>=33&&c<=126)||(c>=160&&c<=255))b.append(c);
            else if(Character.isWhitespace(c)||Character.isSpaceChar(c))b.append(' ');
            else {int n=(c^(c>>8))%52;b.append((char)(n<26?'A'+n:'a'+n-26));}
        }
        return b.toString();
    }
    static int inkCount(String s,CpuFont f) {
        int count=0;for(char c:s.toCharArray()){arp.b g=f.data.a(c);if(c!=' '&&g!=null&&g.d>0&&g.e>0)count++;}return count;
    }
    static final class Rect {
        final int cp; final float x,y;final int w,h;
        Rect(int cp,float x,float y,int w,int h){this.cp=cp;this.x=x;this.y=y;this.w=w;this.h=h;}
    }
    static List<Rect> layout(Draw d) {
        CpuFont f=fonts.get(d.role);check(f!=null,"known actual font");
        arr a=new arr();a.a(f,d.text,0,d.text.length(),new ara(1,1,1,1),0,8,false,null);arrRuns++;
        List<Rect> rects=new ArrayList<Rect>();
        for(int r=0;r<a.a.b;r++) {
            arr.a run=a.a.a(r);float x=run.c+d.x;
            for(int i=0;i<run.a.b;i++) {
                x+=run.b.a[i];arp.b g=run.a.a(i);
                if(g.a==' '||g.d==0||g.e==0)continue;
                check(f.data.a((char)g.a)==g,"direct actual glyph, never missingGlyph");
                float left=x+g.j,top=d.y+run.d+g.k;
                check(left>=0&&left+g.d<=256,"actual arr horizontal ink inside logical256");
                check(top>=0&&top+g.e<=256,"actual arr vertical ink inside logical256");
                rects.add(new Rect(g.a,left,top,g.d,g.e));glyphs++;
            }
        }
        check(rects.size()==inkCount(d.text,f),"actual arr visible quads equal exact visible glyphs");
        return rects;
    }
    static void compare(List<Rect> prefix,List<Rect> full) {
        check(prefix.size()<=full.size(),"no future symbols");
        for(int i=0;i<prefix.size();i++) {
            Rect a=prefix.get(i),b=full.get(i);
            check(a.cp==b.cp&&a.x==b.x&&a.y==b.y&&a.w==b.w&&a.h==b.h,"real arr revealed ink has stable final geometry");
        }
    }
    static void display(anh state,amG active,boolean readable)throws Exception {
        amn animation=active.a();String full=animation.a();String style=active.f();
        boolean pattern=style.equals("HardFox")||(style.equals("Fox")&&!readable);
        boolean story=StoryFont12.uses12(full)&&!pattern;
        jo owner=new jo(state,28,readable,REC,16,54,Ol.MODULE$,null);
        List<List<Rect>> finalRects=new ArrayList<List<Rect>>();
        draws.clear();CALLBACK.invoke(null,owner,style,active.e(),animation,84,full,true);
        check(draws.size()==3,"real jo final rows");
        for(Draw d:draws)finalRects.add(layout(d));
        for(int step=0;step<=84;step++) {
            String mask=amw.MODULE$.a(full,step);check(mask.length()==84,"original mask cells");
            draws.clear();CALLBACK.invoke(null,owner,style,active.e(),animation,step,mask,true);frames++;
            check(draws.size()==3,"real jo original3 rows");
            for(int row=0;row<3;row++) {
                Draw d=draws.get(row);String source=mask.substring(row*28,(row+1)*28);
                check(d.role.equals(pattern?"dingbats":story?"story12":"default"),"original language gate");
                check(d.x==(story?8:16)&&d.y==54-16*row,"original pattern/English anchor; native12 anchor; 16px step");
                check(d.text.equals(pattern?oracle(source):source),"ONLY current revealed mask transformed");
                check(d.text.length()==28,"one UTF16 unit one original reveal cell");
                int expected=0;
                for(int i=0;i<28;i++) {
                    char c=source.charAt(i),out=d.text.charAt(i);
                    if(c==' ')check(out==' ',"padding/future cells never reveal ink");
                    else {expected++;check(fonts.get(d.role).data.a(out)!=null,"every source nonblank has exact selected glyph");}
                }
                List<Rect> actual=layout(d);check(actual.size()==expected,"every revealed nonblank emits visible glyph quad");
                compare(actual,finalRects.get(row));
            }
            check(animation.a().equals(full),"no source/amn mutation");
        }
        // Actual amn time progression and skip must feed the same completed mask.
        check(animation.a(animation.i()+1).equals(full),"actual amn completion");
        amn skipped=animation.a(full,animation.e(),new aAw(100.01),animation.g());
        check(skipped.a(101).equals(full),"actual amn skip completion");
    }
    static void run(anp command,String label,boolean counted)throws Exception {
        String text=ams.MODULE$.a(command.a(),amr.i.MODULE$.a());String style=command.e();
        List<DialogueGrid.Page> expected=SubtitleLayout.pages(text,28);
        if(counted){commands++;int hc=0;for(char c:text.toCharArray())if(Character.UnicodeScript.of(c)==Character.UnicodeScript.HAN)hc++;
            if(hc>0){hanCommands++;han+=hc;int old=0,now=0;for(DialogueGrid.Page p:expected){old+=inkCount(p.grid,fonts.get("dingbats"));now+=inkCount(PatternSymbols.encodeMask(p.grid),fonts.get("dingbats"));}
                if(old==0)beforeBlank++;if(now==0)afterBlank++;}}
        anh result=command.a(state(100,azI.MODULE$,empty()),META);
        for(DialogueGrid.Page p:expected) {
            amG active=(amG)result.f().f();pages++;
            check(active.f().equals(style),"actual parser role retained "+label);
            check(active.a().a().equals(SubtitleLayout.animationGrid(p.grid,28)),"real command entry formatted grid");
            display(result,active,false);display(result,active,true);
            result=result.a(result.o(),result.r()+10,(azK)azI.MODULE$,result.t(),result.u(),result.v(),result.w(),result.x(),result.y(),result.p(),result.q()).a(META);
        }
        check(ams.MODULE$.a(command.a(),amr.i.MODULE$.a()).equals(text),"Chinese source identity not replaced");
    }
    public static void main(String[] args)throws Exception {
        check(args.length==4||args.length==5,"CLI manifest dingbats story12 bbc2 [expected-census.properties]");
        Properties census=new Properties();
        if(args.length==5) {
            try(Reader r=Files.newBufferedReader(Paths.get(args[4]),StandardCharsets.UTF_8)){census.load(r);}
            for(String key:new String[]{"commands","han_commands","han"})check(census.getProperty(key)!=null,"candidate census requires "+key);
        } else {
            census.setProperty("commands","544");census.setProperty("han_commands","268");
            census.setProperty("han","4735");census.setProperty("before_blank","230");
        }
        check(sha(Files.readAllBytes(Paths.get(args[1]))).equals(PatternSymbols.DINGBATS_SHA256),"actual frozen dingbats SHA");
        check(sha(Files.readAllBytes(Paths.get(args[2]))).equals(StoryFont12.FONT_SHA256),"actual frozen story12 SHA");
        fonts.put("dingbats",new CpuFont(Paths.get(args[1])));fonts.put("story12",new CpuFont(Paths.get(args[2])));fonts.put("default",new CpuFont(Paths.get(args[3])));
        CpuFont ding=fonts.get("dingbats");
        for(int cp=0;cp<=65535;cp++) {
            String source=String.valueOf((char)cp),encoded=PatternSymbols.encodeMask(source);
            check(encoded.equals(oracle(source))&&encoded.length()==1,"exhaustive UTF16 deterministic encoding");
            if(!Character.isWhitespace(cp)&&!Character.isSpaceChar(cp)) {
                arp.b g=ding.data.a(encoded.charAt(0));check(g!=null&&g.d>0&&g.e>0&&g.l==8,"all nonblank units map to original visible advance8 glyph");
            }
        }
        String english="Hello, brave hero! [ASCII] 0123456789";
        check(PatternSymbols.encodeMask(english)==english,"pure ASCII returns SAME reference/bytes");
        for(String row:Files.readAllLines(Paths.get(args[0]),StandardCharsets.UTF_8)) {
            String[] fields=row.split("\t");aEO parsed=parse(fields[1],new String(Files.readAllBytes(Paths.get(fields[2])),StandardCharsets.UTF_8));
            for(aEO rest=parsed;!rest.b();rest=(aEO)rest.E())if(rest.s() instanceof anp) {
                anp c=(anp)rest.s();if(c.e().equals("Fox")||c.e().equals("HardFox"))run(c,fields[0]+"/"+fields[1],true);
            }
        }
        String[] cases={"勇敢的英雄啊，感谢你救出我，证明了你的勇气。", "……，。！？“”‘’——·「」", english,"ASCII first row\n中文第二行\n，。……", "    中文<p>下一段",repeat("中",141)};
        for(String style:new String[]{"Fox","HardFox","Normal"})for(int i=0;i<cases.length;i++) {
            aEO parsed=parse("synthetic-"+style+"-"+i,"lang("+style+"): "+cases[i].replace("\n"," ")+"\n");
            run((anp)parsed.s(),"synthetic-"+style+"-"+i,false);
        }
        check(commands==Integer.parseInt(census.getProperty("commands"))&&hanCommands==Integer.parseInt(census.getProperty("han_commands"))
              &&han==Integer.parseInt(census.getProperty("han")),"independent expected language census");
        if(census.getProperty("before_blank")!=null)check(beforeBlank==Integer.parseInt(census.getProperty("before_blank")),"expected pre-fix blank count");
        check(commands>0&&hanCommands>0&&afterBlank==0,"nonempty tested language corpus; no blank encoded Han commands");
        System.out.println("PATTERN_CPU_OK checks="+checks+" commands="+commands+" han_commands="+hanCommands+" han="+han+" before_blank="+beforeBlank+" after_blank="+afterBlank+" pages="+pages+" frames="+frames+" real_arr_runs="+arrRuns+" visible_glyph_quads="+glyphs+" census="+(args.length==5?"candidate-expected":"frozen-r27")+"; actual parser/anp/amn/amw/jo/Id/arr, both readability states, all85 reveal positions; no game/GL/clip/CRT");
    }
    static String repeat(String s,int n){StringBuilder b=new StringBuilder();while(n-->0)b.append(s);return b.toString();}
}
