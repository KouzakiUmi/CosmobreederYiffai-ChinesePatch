import PRG.*;
import cosmoloc.layout.*;
import java.lang.reflect.*;
import java.util.*;

/** Component-owned r27-only test fixture. No dependency on mutable layout test sources. */
@SuppressWarnings({"rawtypes", "unchecked"})
final class VsnRuntimeAssertions {
    static long checks;
    static int renderedPages, manualOverflow, autoOverflow;
    static PixelLayout.Metrics metrics, storyMetrics;
    static final amX META=new amX(null,Ol.MODULE$,Om.MODULE$,null);
    static final Method CALLBACK;
    static {try {CALLBACK=jo.class.getDeclaredMethod("a",jo.class,String.class,azK.class,amn.class,int.class,String.class,boolean.class);}
            catch(Exception e){throw new AssertionError(e);}}
    static final class Draw {
        final String text,role; final int x,y;
        Draw(String t,int x,int y,String r){text=t;this.x=x;this.y=y;role=r;}
    }
    static final List<Draw> draws=new ArrayList<Draw>();
    static final List<String> order=new ArrayList<String>();
    static final SN RECORD=(SN)Proxy.newProxyInstance(VsnRuntimeAssertions.class.getClassLoader(),new Class<?>[]{SN.class},(p,m,a)->{
        if(m.getName().equals("b")&&m.getParameterCount()==0)return "default";
        if(m.getName().equals("a")&&m.getParameterCount()==4&&a[0] instanceof String){draws.add(new Draw((String)a[0],(Integer)a[1],(Integer)a[2],(String)a[3]));order.add("text");}
        if(m.getName().equals("a")&&m.getParameterCount()==5&&"WhiteFill".equals(a[0]))order.add("hint");
        if(m.getReturnType()==boolean.class)return false;
        if(m.getReturnType()==int.class)return 0;
        return null;
    });
    static aEO parse(String root,String script)throws Exception {
        Class<?> t=Class.forName("sun.misc.Unsafe");Field f=t.getDeclaredField("theUnsafe");f.setAccessible(true);Object u=f.get(null);
        amS.a parser=(amS.a)t.getMethod("allocateInstance",Class.class).invoke(u,amS.a.class);
        long off=(Long)t.getMethod("objectFieldOffset",Field.class).invoke(u,amS.a.class.getDeclaredField("a"));
        t.getMethod("putObject",Object.class,long.class,Object.class).invoke(u,parser,off,root);
        auK input=auL.MODULE$.a(script,(azz<String,auI>)(s->new auC(s)));
        auG result=ava.MODULE$.a(input,(azz<auN<Object>,auN<aEO<amZ>>>)(s->parser.E(s)),ava.MODULE$.a(),ava.MODULE$.b(),ava.MODULE$.c());
        return (aEO)result.a().e();
    }
    static aEO empty(){return aFC.MODULE$;}
    static anh state(double time,azK active,aEO pending){return new anh(null,time,active,pending,empty(),null,true,null,null,empty(),(azK)(Object)azI.MODULE$);}
    static anh change(anh s,double time,azK active){return s.a(s.o(),time,active,s.t(),s.u(),s.v(),s.w(),s.x(),s.y(),s.p(),s.q());}
    static String inkOnly(String s){return s.replace("<p>","").replace(" ","").replace("\r","").replace("\n","");}
    static void run(amW command,String text,String root)throws Exception {
        List<DialogueGrid.Page> expected=SubtitleLayout.pages(text,28);
        boolean auto=command instanceof amH;
        if(expected.size()>1){if(auto)autoOverflow++;else manualOverflow++;}
        final int[] events={0};
        amW sentinel=(s,m)->{events[0]++;return change(s,s.e(),new aAw("tail"));};
        aEO tail=new aEg(sentinel,empty());
        anh initial=state(100.0,azI.MODULE$,tail);
        anh result=command.a(initial,META);
        if(expected.size()==1)check(result.t()==tail,"one-page original continuation identity "+root);
        check(result.p()==initial.p(),"event list identity");eq(result.u(),initial.u(),"history identity");
        StringBuilder recovered=new StringBuilder();
        for(DialogueGrid.Page page:expected){
            amG active=(amG)result.f().f();amn animation=active.a();
            eq(animation.a(),page.grid,"real command/continuation exact grid "+root);
            String style=auto?((amH)command).f():((anp)command).e();
            eq(active.f(),style,"role retained");
            if(auto)eq(active.e().f(),Double.valueOf(result.e()+((amH)command).e()),"auto delay unchanged");
            else check(active.e()==(Object)azI.MODULE$,"every continuation remains manual");
            display(result,active,false);
            if(style.equals("Fox"))display(result,active,true);
            for(String line:page.lines)recovered.append(line);
            check(!animation.c(animation.e()),"initially incomplete");check(animation.c(animation.i()),"completes");
            eq(animation.a(animation.i()+1),animation.a(),"completed real mask");
            amn skipped=animation.a(animation.a(),animation.e(),new aAw(100.01),animation.g());
            int terminal=animation.a().length();while(terminal>0&&animation.a().charAt(terminal-1)==' ')terminal--;
            eq(skipped.a(100.02,true),terminal,"skip reaches last original source position "+root);
            eq(skipped.a(101.0),animation.a(),"skip full text");
            draws.clear();CALLBACK.invoke(null,new jo(result,28,false,RECORD,16,54,Ol.MODULE$,null),active.f(),active.e(),skipped,skipped.a(101.0,true),skipped.a(101.0),true);
            eq(draws.size(),3,"skip emits all source rows");
            for(int row=0;row<3;row++)eq(draws.get(row).text,animation.a().substring(row*28,(row+1)*28),"skip no final-char loss");
            check(events[0]==0,"next original event not premature");
            result=change(result,result.e()+10,azI.MODULE$).a(META);
            renderedPages++;
        }
        eq(events[0],1,"next original event exactly once after final page");
        eq(inkOnly(recovered.toString()),inkOnly(text),"all reviewed text conserved across every page "+root);
    }
    static void display(anh state,amG active,boolean readableFox)throws Exception {
        amn a=active.a();jo renderer=new jo(state,28,readableFox,RECORD,16,54,Ol.MODULE$,null);
        for(int r=0;r<=84;r++){
            String mask=amw.MODULE$.a(a.a(),r);eq(mask.length(),84,"original animation length");
            for(int i=0;i<84;i++)check(mask.charAt(i)==(i<r?a.a().charAt(i):' '),"real reveal prefix");
            draws.clear();CALLBACK.invoke(null,renderer,active.f(),active.e(),a,r,mask,true);
            eq(draws.size(),3,"real jo three rows");
            for(int row=0;row<3;row++){
                Draw d=draws.get(row);eq(d.text,mask.substring(row*28,(row+1)*28),"every revealed source row");
                boolean pattern=active.f().equals("HardFox")||(active.f().equals("Fox")&&!readableFox);
                boolean cjk=StoryFont12.uses12(a.a())&&!pattern;
                eq(d.role,pattern?"dingbats":cjk?StoryFont12.ROLE:"default","frozen role selection");
                eq(d.x,cjk?8:16,"native story/default anchor");eq(d.y,54-16*row,"16px line step");
                if(!pattern)ink(d);
            }
        }
    }
    static void ink(Draw d){
        PixelLayout.Metrics selected=StoryFont12.ROLE.equals(d.role)?storyMetrics:metrics;
        int width=StoryFont12.ROLE.equals(d.role)?240:220;double x=d.x;int previous=-1;
        for(int i=0;i<d.text.length();){int cp=d.text.codePointAt(i);PixelLayout.Glyph g=selected.glyph(cp);
            check(g!=null,"real pinned font contains "+cp);
            if(previous!=-1)x+=selected.kerning(previous,cp);
            if(g.width>0&&g.height>0)check(x+g.xOffset>=d.x&&x+g.xOffset+g.width<=d.x+width,"ink inside real width");
            x+=g.xAdvance;previous=cp;i+=Character.charCount(cp);}
    }
    static void tail()throws Exception {
        String grid=SubtitleLayout.pages("原尾事件与提示",28).get(0).grid;
        amn animation=amo.MODULE$.a(grid,100.0);
        anh late=state(200.025,new aAw(new amG(animation,(azK)(Object)azI.MODULE$,"default")),empty());
        ZJ events=(ZJ)Proxy.newProxyInstance(VsnRuntimeAssertions.class.getClassLoader(),new Class<?>[]{ZJ.class},(p,m,a)->{order.add("event");return null;});
        jo renderer=new jo(late,28,false,RECORD,16,54,Ol.MODULE$,events);
        order.clear();CALLBACK.invoke(null,renderer,"default",azI.MODULE$,animation,84,grid,false);
        check(order.contains("hint")&&order.indexOf("text")<order.indexOf("event")&&order.indexOf("event")<order.indexOf("hint"),"text event hint order");
        order.clear();CALLBACK.invoke(null,renderer,"default",azI.MODULE$,animation,84,grid,true);
        check(!order.contains("event"),"done suppresses duplicate event");
    }
    static void check(boolean b,String label){checks++;if(!b)throw new AssertionError(label);}
    static void eq(Object a,Object b,String label){check(Objects.equals(a,b),label+": ["+a+"] != ["+b+"]");}
}
