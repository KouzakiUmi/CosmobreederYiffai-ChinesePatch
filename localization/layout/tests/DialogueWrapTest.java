import PRG.*;
import cosmoloc.layout.*;
import java.io.*;
import java.lang.reflect.*;
import java.util.*;

/** Java 8 isolated tests. No Main/Hi/GL, install, or save access. */
@SuppressWarnings({"rawtypes", "unchecked"})
public final class DialogueWrapTest {
    static int checks;
    static PixelLayout.Metrics metrics, storyMetrics;
    static final String HAN = "这是超光速航行与先进赛博机器人技术的时代。";
    static final Method OLD_RADIO, OLD_SA, OLD_STORY;
    static {
        try {
            OLD_RADIO = JR.class.getDeclaredMethod("a", amq.class, amv.class, aAZ.class);
            OLD_SA = JR.class.getDeclaredMethod("a", SA.class, aAZ.class);
            OLD_STORY = Nb.class.getDeclaredMethod("a", aAJ.class);
        } catch (Exception e) { throw new ExceptionInInitializerError(e); }
    }
    public static void main(String[] args) throws Exception {
        try (InputStream in = new FileInputStream(args[0])) { metrics = DialogueWrap.readMetrics(in); }
        storyMetrics = StoryFont12.metrics();
        eq(storyMetrics.glyph('这').xAdvance,12.0,"real story12 Han advance");
        eq(storyMetrics.glyph('A').xAdvance,8.0,"story12 preserves original ASCII advance");
        fontAndGrid();
        englishAndNarrow();
        chineseAndVariables();
        finalTranslation();
        locales();
        patchedEntryPoints();
        storyFontAndDraw();
        if(args.length>1) storyJoins(args[1]);
        System.out.println("PASS DialogueWrap " + checks + " assertions: pinned real FNT, real amw baselines, CJK pixel/grid/conservation, single full SA, locale uppercase, real amn masks/completion, patched JR/Nb entrypoints");
    }
    static void fontAndGrid() throws Exception {
        eq(metrics.glyph('这').xAdvance, 10.0, "real Han advance");
        eq(metrics.glyph('A').xAdvance, 8.0, "real ASCII advance");
        eq(metrics.glyph(' ').xAdvance, 8.0, "real space advance");
        try { DialogueWrap.readMetrics(new ByteArrayInputStream(new byte[]{1})); throw new AssertionError("font pin accepted"); }
        catch (IOException expected) { checks++; }
        for (int q : new int[]{12,20,28}) {
            int cap = q == 12 ? 8 : q == 20 ? 15 : 20;
            String full = repeat("这", cap * 8 + 1);
            PixelLayout.Metrics selected = q == 28 ? storyMetrics : metrics;
            double width = cap * (q == 28 ? 12 : 10);
            List<DialogueGrid.Page> pages = DialogueWrap.pages(full, q, width, selected);
            StringBuilder complete = new StringBuilder();
            for (DialogueGrid.Page page : pages) {
                eq(page.grid.length(), q * 3, "strict original grid");
                check(!page.grid.contains("-"), "no inserted hyphen");
                eq(page.grid.toUpperCase(), page.grid, "consumer uppercase cannot expand grid");
                for (String line : page.lines) {
                    complete.append(line);
                    check(line.length() <= cap, "15/20 Han cap");
                    PixelLayout.Plan p = PixelLayout.layout(line, selected, new PixelLayout.Profile(
                        new PixelLayout.Rect(0,0,width,100),16,PixelLayout.Insets.NONE));
                    check(!p.overflow && p.inkBounds.width() <= width, "actual role-specific FNT ink bound");
                }
                animation(page.grid);
            }
            eq(complete.toString(), full, "CJK full conservation");
        }
        List<DialogueGrid.Page> paragraphs = DialogueWrap.pages("这是<p>时代",20,150,metrics);
        eq(paragraphs.size(),2,"paragraphs retain formatter boundary");
        eq(paragraphs.get(0).lines.get(0),"这是","paragraph one");
        eq(paragraphs.get(1).lines.get(0),"时代","paragraph two");
        List<DialogueGrid.Page> linebreaks = DialogueWrap.pages("这是\r\n时代",20,150,metrics);
        eq(linebreaks.get(0).lines.get(0),"这是","CRLF first line");
        eq(linebreaks.get(0).lines.get(1),"时代","CRLF second line");
    }
    static void englishAndNarrow() throws Exception {
        String[] english = {"Hello world.", "A rather long English conversation with enough words to span several original rows and multiple original pages.",
            "antidisestablishmentarianism", "one<p>two", "", "lowercase i and mixed English"};
        for (String text : english) {
            aAZ tuple = radioTuple(text);
            for (amq q : new amq[]{Ob.MODULE$, NY.MODULE$}) {
                int[] calls = {0};
                SA sa = sa(x -> { calls[0]++; return x; });
                aEO expected = oldRadio(tuple,q,Om.MODULE$,sa);
                int expectedCalls = calls[0]; calls[0]=0;
                aEO actual = DialogueWrap.radio(list(tuple),q,Om.MODULE$,sa);
                eq(actual,expected,"real three-argument amw exact English/narrow pages");
                eq(calls[0],expectedCalls,"English/narrow original SA call count");
            }
            aAJ pair = new aAJ(new amr.h(text,"fixture"),new String("expression"));
            aEO expected = (aEO)OLD_STORY.invoke(null,pair);
            eq(DialogueWrap.story(list(pair)),expected,"real story English pages unchanged");
        }
        aAZ chinese = radioTuple(repeat("这",80));
        int[] n = {0}; SA narrowSA = sa(x -> { n[0]++; return x; });
        aEO narrow = DialogueWrap.radio(list(chinese),NY.MODULE$,Om.MODULE$,narrowSA);
        verifyRadio(narrow,chinese,repeat("这",80),12);
        eq(n[0],1,"Continue q12 applies SA once to the complete CJK tuple");
        amq unknown12 = new amq(){public int a(){return 12;}};
        eq(DialogueWrap.radio(list(chinese),unknown12,Om.MODULE$,narrowSA),
            oldRadio(chinese,unknown12,Om.MODULE$,narrowSA),"unknown q12 remains exactly legacy");
        amq unknown20 = new amq(){public int a(){return 20;}};
        eq(DialogueWrap.radio(list(chinese),unknown20,Om.MODULE$,narrowSA),
            oldRadio(chinese,unknown20,Om.MODULE$,narrowSA),"unknown numeric-equivalent profile remains legacy");
        check(DialogueWrap.radio(empty(),Ob.MODULE$,Om.MODULE$,narrowSA) == aFC.MODULE$,"empty radio list identity");
        check(DialogueWrap.story(empty()) == aFC.MODULE$,"empty story list identity");
    }
    static void chineseAndVariables() throws Exception {
        aAZ tuple = radioTuple(repeat(HAN,4));
        int[] calls={0};
        aEO radio = DialogueWrap.radio(list(tuple),Ob.MODULE$,Om.MODULE$,sa(x -> {calls[0]++;return x;}));
        eq(calls[0],1,"CJK SA once for entire tuple, never per new page");
        verifyRadio(radio,tuple,repeat(HAN,4),20);
        String variables = "@DerekChipReport@ZoneName@EmuButtons@BOYPC@GIRLPC";
        String[] keys={"@DerekChipReport","@ZoneName","@EmuButtons","@BOYPC","@GIRLPC"};
        calls[0]=0;
        SA replacement = sa(x -> {
            calls[0]++;
            eq(x.a(),variables,"SA receives complete unwrapped variable string");
            String value=x.a();
            for(String key:keys)value=value.replace(key,repeat("这",31));
            return new amr.d(value);
        });
        aAZ dynamic=radioTuple(variables);
        aEO expanded=DialogueWrap.radio(list(dynamic),Ob.MODULE$,Om.MODULE$,replacement);
        eq(calls[0],1,"dynamic final-CJK full replacement once");
        verifyRadio(expanded,dynamic,repeat("这",155),20);
        calls[0]=0;
        String report=repeat("IT LOOKS LIKE THERE IS ONE CHIP LEFT IN THE NEXT ZONE. ",4).trim();
        SA asciiReport=sa(x->{calls[0]++;return new amr.d(x.a().replace("@DerekChipReport",report));});
        aEO asciiPages=DialogueWrap.radio(list(radioTuple("@DerekChipReport")),Ob.MODULE$,Om.MODULE$,asciiReport);
        eq(calls[0],1,"ASCII dynamic report also transforms exactly once before wrapping");
        check(asciiPages.length()>1,"long ASCII replacement becomes real pages, not an overflowing single old page");
        StringBuilder asciiRecovered=new StringBuilder();
        for(aEO rest=asciiPages;!rest.b();rest=(aEO)rest.E()) {
            String grid=((amr.d)((aAZ)rest.s()).a()).a();eq(grid.length(),60,"ASCII variable original 20x3 grid");
            for(int row=0;row<3;row++) {
                String line=grid.substring(row*20,(row+1)*20).trim();
                PixelLayout.Plan measured=PixelLayout.layout(line,metrics,new PixelLayout.Profile(new PixelLayout.Rect(0,0,150,32),16,PixelLayout.Insets.NONE));
                check(!measured.overflow,"ASCII variable line actual width <=150");asciiRecovered.append(line);
            }
        }
        eq(asciiRecovered.toString().replace(" ",""),report.replace(" ",""),"ASCII expanded report text conserved without hyphens");
        aAJ storyTuple=new aAJ(new amr.h(repeat(HAN,4),"fixture"),new String("expression"));
        aEO story=DialogueWrap.story(list(storyTuple));
        StringBuilder text=new StringBuilder();
        for(aEO rest=story;!rest.b();rest=(aEO)rest.E()) {
            aAJ page=(aAJ)rest.s(); check(page.e()==storyTuple.e(),"story expression identity");
            String grid=((amr.d)page.a()).a();eq(grid.length(),84,"story original 28x3");
            for(int i=0;i<3;i++)text.append(grid.substring(i*28,(i+1)*28).trim());
        }
        eq(text.toString(),repeat(HAN,4),"story full content across pages");
        // Adjacent source tuples remain distinct, including a legitimate empty string.
        aEO separate=DialogueWrap.story(list(new aAJ(new amr.h("这是","1"),"x"),new aAJ(new amr.h("时代","2"),"y")));
        eq(separate.length(),2,"no inferred adjacent join");
    }
    static void verifyRadio(aEO pages,aAZ tuple,String expected,int q) {
        StringBuilder full=new StringBuilder();
        for(aEO rest=pages;!rest.b();rest=(aEO)rest.E()) {
            aAZ page=(aAZ)rest.s();
            check(page.e()==tuple.e(),"actor identity");check(page.f()==tuple.f(),"expression identity");
            String grid=((amr.d)page.a()).a();eq(grid.length(),q*3,"radio original 20x3");
            for(int row=0;row<3;row++) {
                String line=grid.substring(row*q,(row+1)*q).trim();
                check(line.length()<=(q==12?8:15),"verified caller conservative 8/15 Han cap");
                PixelLayout.Plan measured=PixelLayout.layout(line,metrics,new PixelLayout.Profile(new PixelLayout.Rect(0,0,q==12?80:150,32),16,PixelLayout.Insets.NONE));
                check(!measured.overflow,"verified caller actual 80/150px cap");full.append(line);
            }
        }
        eq(full.toString(),expected,"radio full conservation after actual SA");
        check(((aEO)((aEg)lastList(pages)).E()).b(),"last page has empty remainder");
    }
    static aEO lastList(aEO pages) { while(!((aEO)pages.E()).b())pages=(aEO)pages.E();return pages; }
    static void animation(String grid) {
        amn animated=amo.MODULE$.a(grid,100.0);
        for(int r=0;r<=grid.length();r++) {
            String mask=amw.MODULE$.a(grid,r);
            eq(mask.length(),grid.length(),"real amw mask retains exact grid length");
            for(int i=0;i<grid.length();i++)eq(mask.charAt(i),i<r?grid.charAt(i):' ',"real reveal mask");
        }
        check(!animated.c(100.0),"real amn initially incomplete");
        check(animated.c(animated.i()),"real amn original completion deadline");
        eq(animated.a(animated.i()+1),grid,"real amn complete masked text");
        amn skipped=animated.a(grid,animated.e(),new aAw<Object>(100.01),animated.g());
        eq(skipped.a(100.02,true),grid.trim().length(),"real amn skip completes through nonpadding");
    }
    static void finalTranslation() throws Exception {
        Field mode=Tc.class.getDeclaredField("a");mode.setAccessible(true);
        Object saved=mode.get(null);
        try {
            mode.set(null,Tb.MODULE$);
            // With an empty isolated dictionary, Tc's documented bytecode fallback is the key,
            // NOT h.a(). This distinguishes actual final-text resolution from raw source wrapping.
            aAZ tuple=new aAZ(new amr.h("English source must not display","这是"),"actor",new aAw<String>("expr"));
            aEO result=DialogueWrap.radio(list(tuple),Ob.MODULE$,Om.MODULE$,sa(x->x));
            eq(((amr.d)((aAZ)result.s()).a()).a().trim(),"这是","radio consumes actual Tc final resolution");
            aEO story=DialogueWrap.story(list(new aAJ(new amr.h("English source must not display","时代"),"expr")));
            eq(((amr.d)((aAJ)story.s()).a()).a().trim(),"时代","story consumes actual Tc final resolution");
        } finally {mode.set(null,saved);}
    }
    static void locales() {
        Locale old=Locale.getDefault();
        PixelLayout.Metrics fixture=new PixelLayout.Metrics(){
            public PixelLayout.Glyph glyph(int cp){return new PixelLayout.Glyph(cp<128?8:10,0,0,cp==32?0:cp<128?8:10,10);}
            public double kerning(int a,int b){return 0;}
        };
        try {
            for(Locale locale:new Locale[]{Locale.ENGLISH,new Locale("tr","TR"),new Locale("lt","LT")}) {
                Locale.setDefault(locale);
                String mixed="这straße iıİi\u0307时代";
                List<DialogueGrid.Page> pages=DialogueWrap.pages(mixed,20,150,fixture);
                StringBuilder joined=new StringBuilder();
                for(DialogueGrid.Page page:pages) {
                    eq(page.grid,page.grid.toUpperCase(),"same-locale post-uppercase exact identity "+locale);
                    for(String line:page.lines)joined.append(line);
                }
                eq(joined.toString(),mixed.toUpperCase(locale),"uppercase expansion measured before wrap "+locale);
                // The production FNT also covers sharp-s AFTER expansion. Turkish dotted-I
                // itself is absent from this exact font, hence the separate metrics fixture above.
                String real="这straße I时代";
                StringBuilder realJoined=new StringBuilder();
                for(DialogueGrid.Page page:DialogueWrap.pages(real,20,150,metrics)) {
                    eq(page.grid,page.grid.toUpperCase(),"actual font locale grid identity "+locale);
                    for(String line:page.lines)realJoined.append(line);
                }
                eq(realJoined.toString(),real.toUpperCase(locale),"actual font sharp-s expansion "+locale);
            }
        } finally { Locale.setDefault(old); }
    }
    static final class FixtureVisited extends abF {
        int visits;
        FixtureVisited(){super((ST)Proxy.newProxyInstance(DialogueWrapTest.class.getClassLoader(),new Class<?>[]{ST.class},(p,m,a)->null),()->null);}
        public void d(String key){visits++;}
    }
    static final class FixtureEvents extends abN {
        int events;
        FixtureEvents(){super(null,null);}
        public void a(afp event){events++;}
    }
    static final class FixtureState extends apr {
        final SA sa;
        final FixtureVisited visited=new FixtureVisited();
        final FixtureEvents events=new FixtureEvents();
        FixtureState(SA sa){super(1,1);this.sa=sa;}
        public <A> A a(apt<A> key){
            if(key==SB.MODULE$.a())return (A)sa;
            if(key==abG.MODULE$.a())return (A)visited;
            if(key==abO.MODULE$.a())return (A)events;
            throw new AssertionError("unexpected subsystem lookup");
        }
    }
    static void patchedEntryPoints() throws Exception {
        int[] calls={0};SA sa=sa(x->{calls[0]++;return x;});
        FixtureState state=new FixtureState(sa);
        afD.n line=new afD.n(0,"Actor","expression",repeat(HAN,4));
        afD.g dialogue=new afD.g("fixture","entry",null,(aEO)list(line,new afD.f(0,new afp(null))));
        aAJ result=JR.MODULE$.a(dialogue,Ob.MODULE$,Om.MODULE$,state);
        check(((aEO)result.a()).length()>1,"actual patched JR main emits CJK pages");
        aEO deferred=(aEO)result.e();
        eq(deferred.length(),1,"actual JR retains nonempty deferred event list");
        eq(state.events.events,0,"JR return does not eagerly execute deferred event");
        ((azy)deferred.s()).apply();
        eq(state.events.events,1,"original JR deferred closure executes actual event once");
        eq(calls[0],1,"actual patched JR performs full SA once");
        MG role=new MG(){};
        Na.a story=Nb.MODULE$.a(dialogue,role,100.0,(a,b)->aKd.a,state);
        eq(story.a().a().length(),84,"actual patched Nb constructs original 28x3 amn");
        check(story.g()==role,"actual Nb MG identity");
        eq(state.events.events,2,"actual Nb executes its original event list once");
        eq(state.visited.visits,1,"actual Nb retains original visited-state update");
        check(story.f().length()>0,"actual Nb original next-page list");
        aEO pages=story.f();
        while(!pages.b()) {
            aAJ page=(aAJ)pages.s();
            amn next=amo.MODULE$.a(((amr.d)page.a()).a(),200.0);
            check(next.c(next.i()),"next-page real amn completion");
            pages=(aEO)pages.E();
        }
        check(pages==aFC.MODULE$,"actual Nb empty remaining-page terminal");
    }
    static void storyFontAndDraw() throws Exception {
        // Same-locale uppercase remains original behavior. The sealed default10
        // and story12 fonts do not promise Turkish dotted-I coverage: reject it
        // explicitly rather than silently substituting or changing user locale.
        try { storyMetrics.glyph(0x130); throw new AssertionError("unexpected dotted-I font scope"); }
        catch(IllegalArgumentException expected) { checks++; }
        for(String value:new String[]{"[3P组织]已成为推动太空探索的一股重要力量。",
            "毕竟，谁又能说清遥远的未知星球上潜藏着什么危险……", "ASCII FIRST\n中文第二行\n，。……", "……，。！？", "这AAAAAAAAAAAAAAAAAAAAAAAAAAAA"}) {
            aAJ input=new aAJ(new amr.h(value,"story12-fixture"),"expression");
            aEO actual=DialogueWrap.story(list(input));
            List<DialogueGrid.Page> expected=DialogueWrap.storyPages(value);
            eq(actual.length(),expected.size(),"story12 measured before original pagination");
            int index=0;
            for(aEO rest=actual;!rest.b();rest=(aEO)rest.E()) {
                aAJ page=(aAJ)rest.s();String grid=((amr.d)page.a()).a();
                eq(grid,expected.get(index++).grid,"actual story adapter uses 12px/240px");
                check(page.e()==input.e(),"story12 expression reference unchanged");
                storyDraw(grid);
            }
        }
    }
    static void storyJoins(String path) throws Exception {
        int count=0;
        for(String row:java.nio.file.Files.readAllLines(java.nio.file.Paths.get(path),java.nio.charset.StandardCharsets.UTF_8)) {
            String[] fields=row.split("\t",2);
            String value=new String(Base64.getDecoder().decode(fields[1]),java.nio.charset.StandardCharsets.UTF_8);
            aEO pages=DialogueWrap.story(list(new aAJ(new amr.h(value,fields[0]),"expression")));
            for(aEO rest=pages;!rest.b();rest=(aEO)rest.E())storyDraw(((amr.d)((aAJ)rest.s()).a()).a());
            count++;
        }
        eq(count,956,"all current joined source records actually laid out and drawn");
    }
    static void storyDraw(String grid) throws Exception {
        amn animation=amo.MODULE$.a(grid,100.0);
        boolean cjk=StoryFont12.uses12(grid);
        PixelLayout.Metrics selected=cjk?storyMetrics:metrics;
        int x=cjk?8:16;double width=cjk?240:224;
        List<Object[]> draws=new ArrayList<Object[]>();
        SN sn=(SN)Proxy.newProxyInstance(DialogueWrapTest.class.getClassLoader(),new Class<?>[]{SN.class},(p,m,a)->{
            if(m.getName().equals("b")&&m.getParameterCount()==0)return "default";
            if(m.getName().equals("a")&&m.getParameterCount()==4&&a[0] instanceof String)draws.add(a);
            if(m.getReturnType()==boolean.class)return false;
            if(m.getReturnType()==int.class)return 0;
            return null;
        });
        Na renderer=new Na(null);
        Na.a state=new Na.a(animation,"expression",empty(),new MG(){});
        Method callback=Na.class.getDeclaredMethod("a",Na.class,int.class,Na.a.class,SN.class,
            int.class,int.class,boolean.class,double.class,amn.class,int.class,String.class,boolean.class);
        for(int reveal=0;reveal<=84;reveal++) {
            String mask=amw.MODULE$.a(grid,reveal);draws.clear();
            callback.invoke(null,renderer,28,state,sn,16,54,false,100.0,animation,reveal,mask,true);
            eq(draws.size(),3,"real Na callback retains three original rows");
            for(int row=0;row<3;row++) {
                Object[] draw=draws.get(row);String text=(String)draw[0];
                eq(text,mask.substring(row*28,(row+1)*28).toUpperCase(),"actual Na source row");
                eq(draw[1],x,"Na story12 x8 / legacy x16");eq(draw[2],54-row*16,"Na line step unchanged");
                eq(draw[3],cjk?StoryFont12.ROLE:"default","Na role stable from full page, not ASCII-only reveal prefix");
                double pen=x;int previous=-1;
                for(int at=0;at<text.length();) {
                    int cp=text.codePointAt(at);PixelLayout.Glyph glyph=selected.glyph(cp);
                    if(previous!=-1)pen+=selected.kerning(previous,cp);
                    if(glyph.width>0&&glyph.height>0)check(pen+glyph.xOffset>=x&&pen+glyph.xOffset+glyph.width<=x+width
                        &&pen+glyph.xOffset+glyph.width<=256,"actual Na role-font ink bound");
                    pen+=glyph.xAdvance;previous=cp;at+=Character.charCount(cp);
                }
            }
        }
        check(animation.c(animation.i()),"story12 original completion deadline");
        eq(animation.a(1e9),grid,"story12 no terminal mask ink lost");
        amn skipped=animation.a(grid,animation.e(),new aAw<Object>(100.01),animation.g());
        eq(skipped.a(101.0),grid,"story12 original copy/skip source preserved");
    }
    static SA sa(azz<amr.d,amr.d> op){return new SA(null,null,ignored->op,null);}
    static aAZ radioTuple(String text){return new aAZ(new amr.h(text,"fixture"),new String("actor"),new aAw<String>("expression"));}
    static aEO oldRadio(aAZ tuple,amq q,amv h,SA sa) throws Exception {
        aEO old=(aEO)OLD_RADIO.invoke(null,q,h,tuple);List<Object> values=new ArrayList<Object>();
        for(aEO rest=old;!rest.b();rest=(aEO)rest.E())values.add(OLD_SA.invoke(null,sa,rest.s()));
        return list(values.toArray());
    }
    static aEO empty(){return (aEO)aFC.MODULE$;}
    static aEO list(Object... values){aEO out=empty();for(int i=values.length-1;i>=0;i--)out=new aEg(values[i],out);return out;}
    static String repeat(String s,int count){StringBuilder b=new StringBuilder();while(count-->0)b.append(s);return b.toString();}
    static void check(boolean yes,String label){checks++;if(!yes)throw new AssertionError(label);}
    static void eq(Object a,Object b,String label){check(Objects.equals(a,b),label+": "+a+" != "+b);}
}
