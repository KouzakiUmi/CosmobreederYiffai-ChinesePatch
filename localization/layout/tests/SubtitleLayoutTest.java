import PRG.*;
import cosmoloc.layout.*;
import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/** Original-JRE integration fixture. Exact-entry patched game JAR only; no Main/GL. */
@SuppressWarnings({"rawtypes", "unchecked"})
public final class SubtitleLayoutTest {
    static long checks;
    static int commands, renderedPages, manualOverflow, autoOverflow;
    static PixelLayout.Metrics metrics, storyMetrics;
    static final amX META = new amX(null, Ol.MODULE$, Om.MODULE$, null);
    static final Method CALLBACK;
    static { try { CALLBACK = jo.class.getDeclaredMethod("a", jo.class, String.class, azK.class,
        amn.class, int.class, String.class, boolean.class); } catch (Exception e) { throw new AssertionError(e); } }
    static final class Draw {
        String text,role; int x,y;
        Draw(String text,int x,int y,String role){this.text=text;this.x=x;this.y=y;this.role=role;}
    }
    static final List<Draw> draws = new ArrayList<Draw>();
    static final List<String> order = new ArrayList<String>();
    static final SN SN_RECORD = (SN)Proxy.newProxyInstance(SubtitleLayoutTest.class.getClassLoader(),
        new Class<?>[]{SN.class}, (proxy, method, a) -> {
            if (method.getName().equals("b") && method.getParameterCount()==0) return "default";
            if (method.getName().equals("a") && method.getParameterCount()==4 && a[0] instanceof String) {
                draws.add(new Draw((String)a[0],(Integer)a[1],(Integer)a[2],(String)a[3])); order.add("text");
            }
            if (method.getName().equals("a") && method.getParameterCount()==5 && "WhiteFill".equals(a[0])) order.add("hint");
            if (method.getReturnType()==boolean.class)return false;
            if (method.getReturnType()==int.class)return 0;
            return null;
        });
    public static void main(String[] args) throws Exception {
        try(InputStream in=new FileInputStream(args[0])) {metrics=DialogueWrap.readMetrics(in);}
        eq(metrics.glyph('这').xAdvance,10.0,"pinned actual Han advance");
        eq(metrics.glyph('A').xAdvance,8.0,"pinned actual ASCII advance");
        storyMetrics=StoryFont12.metrics();
        eq(storyMetrics.glyph('这').xAdvance,12.0,"real story12 Han advance");
        eq(storyMetrics.glyph('，').xAdvance,12.0,"real story12 Chinese punctuation advance");
        eq(storyMetrics.glyph('A').xAdvance,8.0,"story12 retains original ASCII advance");
        eq(SubtitleLayout.LINE_WIDTH,240,"20 real 12px CJK cells");
        eq(SubtitleLayout.LEGACY_LINE_WIDTH,220,"pure ASCII caption width unchanged");
        List<DialogueGrid.Page> exact20=SubtitleLayout.pages(repeat("这",20),28);
        eq(exact20.size(),1,"20-Han caption is one original logical page");
        eq(exact20.get(0).lines.get(0),repeat("这",20),"20 actual 12px Han fit one 240px row");
        check(exact20.get(0).lines.get(1).isEmpty(),"exact20 has no tail row");
        check(SubtitleLayout.pages(repeat("这",21),28).get(0).lines.get(0).length()<=20,"21st Han wraps within 240px");
        String legalMixed29="这AAAAAAAAAAAAAAAAAAAAAAAAAAAA";
        try { DialogueGrid.format(legalMixed29,storyMetrics,28,3,240); throw new AssertionError("legacy UTF16 contract changed"); }
        catch(IllegalArgumentException expected) { checks++; }
        run(new anp(new amr.h(legalMixed29,"utf16-cap"),"default"),legalMixed29,"synthetic/legal-236px-29UTF16");
        pictureCase("[3P组织]已成为推动太空探索的一股重要力量。");
        pictureCase("毕竟，谁又能说清遥远的未知星球上潜藏着什么危险……");
        Set<String> roots=new TreeSet<String>(); int scripts=0;
        for(String row:Files.readAllLines(Paths.get(args[1]),StandardCharsets.UTF_8)) {
            String[] f=row.split("\t"); scripts++; roots.add(f[0]+"/"+f[1]);
            aEO parsed=parse(f[1],new String(Files.readAllBytes(Paths.get(f[2])),StandardCharsets.UTF_8));
            for(aEO rest=parsed;!rest.b();rest=(aEO)rest.E()) {
                Object command=rest.s();
                if(command instanceof amH) run((amH)command,ams.MODULE$.a(((amH)command).a(),amr.i.MODULE$.a()),f[0]+"/"+f[1]);
                if(command instanceof anp) run((anp)command,ams.MODULE$.a(((anp)command).a(),amr.i.MODULE$.a()),f[0]+"/"+f[1]);
            }
        }
        check(roots.contains("nsfw/ClassicPreTitle"),"real NSFW opening included");
        for(String role:new String[]{"f","m"}) {
            for(String area:new String[]{"0","A","B","C","E"})
                check(roots.contains("nsfw/"+role+"_GameOverArea"+area),"entire game-over resource included "+role+area);
            for(String ending:new String[]{"Good","Bad"})check(roots.contains("nsfw/"+role+"_Ending"+ending),"entire ending included");
        }
        // Future/dynamic >3-line fixtures: actual patched entries and actual queue consumer.
        run(new anp(new amr.h(repeat("这",141),"manual-long"),"default"),repeat("这",141),"synthetic/manual");
        run(new amH(new amr.h(repeat("这",141),"auto-long"),8.0,"default"),repeat("这",141),"synthetic/auto");
        run(new anp(new amr.h("lowerCase i Astro<p>这是|原文边界","semantics"),"default"),"lowerCase i Astro<p>这是|原文边界","synthetic/semantics");
        run(new anp(new amr.h("\n   原动画 trim 边界<p>下一段|保留","leading"),"default"),"\n   原动画 trim 边界<p>下一段|保留","synthetic/leading");
        String mixedRows="ASCII only row\n中文第二行\n，。……";
        run(new anp(new amr.h(mixedRows,"mixed-role"),"default"),mixedRows,"synthetic/stable-role");
        run(new anp(new amr.h("……，。！？","punctuation-only"),"default"),"……，。！？","synthetic/punctuation-only");
        tail();
        System.out.println("PASS SubtitleLayout checks="+checks+" scripts="+scripts+" commands="+commands+
            " actualJoPages="+renderedPages+" manualOverflow="+manualOverflow+" autoOverflow="+autoOverflow+
            "; real amH/anp + amn masks/skip/completion + anh queue + jo/Id/SN + SHA-pinned FNT ink; no GL/clip/CRT claim");
    }
    static void pictureCase(String text)throws Exception {
        List<DialogueGrid.Page> pages=SubtitleLayout.pages(text,28);
        eq(pages.size(),1,"picture sentence retains one logical page");
        check(!pages.get(0).lines.get(0).isEmpty() && !pages.get(0).lines.get(1).isEmpty()
            && pages.get(0).lines.get(2).isEmpty(),"picture sentence wraps naturally to two 12px rows");
        run(new amH(new amr.h(text,"picture-case"),8.0,"default"),text,"exact-user-picture");
    }
    static aEO parse(String root,String script)throws Exception {
        Class<?> type=Class.forName("sun.misc.Unsafe");
        Field f=type.getDeclaredField("theUnsafe");f.setAccessible(true);Object unsafe=f.get(null);
        amS.a parser=(amS.a)type.getMethod("allocateInstance",Class.class).invoke(unsafe,amS.a.class);
        Field source=amS.a.class.getDeclaredField("a");
        long offset=(Long)type.getMethod("objectFieldOffset",Field.class).invoke(unsafe,source);
        type.getMethod("putObject",Object.class,long.class,Object.class).invoke(unsafe,parser,offset,root);
        auK input=auL.MODULE$.a(script,(azz<String,auI>)(s->new auC(s)));
        auG result=ava.MODULE$.a(input,(azz<auN<Object>,auN<aEO<amZ>>>)(s->parser.E(s)),ava.MODULE$.a(),ava.MODULE$.b(),ava.MODULE$.c());
        return (aEO)result.a().e();
    }
    static anh state(double time,azK active,aEO pending) {
        return new anh(null,time,active,pending,empty(),null,true,null,null,empty(),(azK)(Object)azI.MODULE$);
    }
    static anh change(anh s,double time,azK active) {
        return s.a(s.o(),time,active,s.t(),s.u(),s.v(),s.w(),s.x(),s.y(),s.p(),s.q());
    }
    static void run(amW command,String text,String root)throws Exception {
        commands++;
        List<DialogueGrid.Page> expected=SubtitleLayout.pages(text,28);
        boolean auto=command instanceof amH;
        if(expected.size()>1){if(auto)autoOverflow++;else manualOverflow++;}
        final int[] tailCount={0};
        amW sentinel=(s,m)->{tailCount[0]++;return change(s,s.e(),new aAw("tail"));};
        aEO originalTail=new aEg(sentinel,empty());
        anh initial=state(100.0,azI.MODULE$,originalTail);
        anh result=command.a(initial,META); // Patched REAL entry, not helper-only test.
        if(expected.size()==1)check(result.t()==originalTail,"one-page original pending identity "+root);
        eq(result.u(),initial.u(),"history preserved");check(result.p()==initial.p(),"event list identity");
        StringBuilder recovered=new StringBuilder();
        for(int i=0;i<expected.size();i++) {
            amG active=(amG)result.f().f(); amn animation=active.a();
            eq(animation.a(),SubtitleLayout.animationGrid(expected.get(i).grid,28),"actual entry/continuation grid "+root);
            check(animation.a().trim().isEmpty() || animation.a().charAt(0)!=' ',"no leading-padding amn trim-index truncation");
            eq(animation.a().replace(" ",""),expected.get(i).grid.replace(" ",""),"actual animation preserves every source ink character");
            eq(active.f(),auto?((amH)command).f():((anp)command).e(),"original style");
            if(auto)eq(active.e().f(),Double.valueOf(result.e()+((amH)command).e()),"original auto delay per page");
            else check(active.e()==(Object)azI.MODULE$,"manual continuation retains manual wait");
            display(result,active,expected.get(i));
            if(active.f().equals("Fox"))display(result,active,expected.get(i),true);
            renderedPages++;
            for(String line:expected.get(i).lines)recovered.append(line);
            check(!animation.c(animation.e()),"real amn initially incomplete");
            check(animation.c(animation.i()),"real amn original completion");
            eq(animation.a(animation.i()+1),animation.a(),"real completed mask");
            amn skipped=animation.a(animation.a(),animation.e(),new aAw(100.01),animation.g());
            eq(skipped.a(100.02,true),animation.a().trim().length(),"original amn skip completion");
            eq(skipped.a(101.0),animation.a(),"original skipped amn full mask");
            draws.clear();
            CALLBACK.invoke(null,new jo(result,28,false,SN_RECORD,16,54,Ol.MODULE$,null),active.f(),
                active.e(),skipped,skipped.a(101.0,true),skipped.a(101.0),true);
            eq(draws.size(),3,"real copied/skip amn reaches jo");
            for(int row=0;row<3;row++)eq(draws.get(row).text,animation.a().substring(row*28,(row+1)*28),"skip frame exact source row");
            check(tailCount[0]==0,"no premature original tail event");
            // Original anh drains remaining amW only after active state clears.
            result=change(result,result.e()+10,azI.MODULE$).a(META);
        }
        eq(tailCount[0],1,"original tail executes exactly once after final page");
        eq(recovered.toString().replace(" ",""),text.replace("<p>","").replace(" ","").replace("\r","").replace("\n",""),"all source conserved "+root);
    }
    static void display(anh state,amG active,DialogueGrid.Page page)throws Exception {display(state,active,page,false);}
    static void display(anh state,amG active,DialogueGrid.Page page,boolean readableFox)throws Exception {
        amn animation=active.a();jo renderer=new jo(state,28,readableFox,SN_RECORD,16,54,Ol.MODULE$,null);
        // Exercise EVERY original reveal position through the REAL callback, not a width-only proxy.
        for(int r=0;r<=84;r++) {
            String mask=amw.MODULE$.a(animation.a(),r);
            eq(mask.length(),84,"real mask original length");
            for(int j=0;j<84;j++)check(mask.charAt(j)==(j<r?animation.a().charAt(j):' '),"original reveal semantics");
            draws.clear(); CALLBACK.invoke(null,renderer,active.f(),active.e(),animation,r,mask,true);
            eq(draws.size(),3,"real jo emits original three SN rows");
            for(int row=0;row<3;row++) {
                Draw draw=draws.get(row);eq(draw.text,mask.substring(row*28,(row+1)*28),"actual source row");
                boolean pattern=active.f().equals("HardFox") || (active.f().equals("Fox") && !readableFox);
                boolean cjk=StoryFont12.uses12(animation.a()) && !pattern;
                eq(draw.role,pattern?"dingbats":cjk?StoryFont12.ROLE:"default","font role follows full animation, never current mask row");
                eq(draw.x,cjk?8:16,"story12 x8 / pure ASCII or dingbats legacy x16");
                eq(draw.y,54-16*row,"real jo unchanged line step");
                // Patterns deliberately retain the ORIGINAL dingbats font; do
                // not pretend default10 or story12 describes its symbol ink.
                if(!pattern)ink(draw);
            }
        }
    }
    static void ink(Draw draw) {
        PixelLayout.Metrics selected=StoryFont12.ROLE.equals(draw.role)?storyMetrics:metrics;
        int width=StoryFont12.ROLE.equals(draw.role)?SubtitleLayout.LINE_WIDTH:SubtitleLayout.LEGACY_LINE_WIDTH;
        double x=draw.x;int previous=-1;
        for(int at=0;at<draw.text.length();) {
            int cp=draw.text.codePointAt(at);PixelLayout.Glyph g=selected.glyph(cp);
            if(previous!=-1)x+=selected.kerning(previous,cp);
            if(g.width>0 && g.height>0) {
                check(x+g.xOffset>=draw.x && x+g.xOffset+g.width<=draw.x+width,"actual role-specific FNT ink inside 240px CJK / 220px legacy");
                check(x+g.xOffset>=0 && x+g.xOffset+g.width<=256,"actual FNT ink inside logical256 horizontal");
                check(draw.y-g.yOffset-g.height>=0 && draw.y+g.yOffset+g.height<=256,"FNT ink both vertical conventions inside logical256");
            }
            x+=g.xAdvance;previous=cp;at+=Character.charCount(cp);
        }
    }
    static void tail()throws Exception {
        String grid=SubtitleLayout.pages("原尾事件与提示",28).get(0).grid;
        amn animation=amo.MODULE$.a(grid,100.0);
        anh late=state(200.025,new aAw(new amG(animation,(azK)(Object)azI.MODULE$,"default")),empty());
        ZJ events=(ZJ)Proxy.newProxyInstance(SubtitleLayoutTest.class.getClassLoader(),new Class<?>[]{ZJ.class},(p,m,a)->{order.add("event");return null;});
        jo renderer=new jo(late,28,false,SN_RECORD,16,54,Ol.MODULE$,events);
        order.clear();CALLBACK.invoke(null,renderer,"default",azI.MODULE$,animation,84,grid,false);
        check(order.contains("hint") && order.indexOf("text")<order.indexOf("event") && order.indexOf("event")<order.indexOf("hint"),"real jo text -> untouched event -> hint");
        order.clear();CALLBACK.invoke(null,renderer,"default",azI.MODULE$,animation,84,grid,true);
        check(!order.contains("event"),"real callback done suppresses original event");
    }
    static aEO empty(){return aFC.MODULE$;}
    static String repeat(String s,int n){StringBuilder out=new StringBuilder();while(n-->0)out.append(s);return out.toString();}
    static void check(boolean value,String label){checks++;if(!value)throw new AssertionError(label);}
    static void eq(Object a,Object b,String label){check(Objects.equals(a,b),label+": ["+a+"] != ["+b+"]");}
}
