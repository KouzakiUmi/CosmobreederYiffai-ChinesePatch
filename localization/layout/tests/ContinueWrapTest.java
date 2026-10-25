import PRG.*;
import cosmoloc.layout.*;
import java.io.*;
import java.lang.reflect.*;
import java.util.*;

/** Isolated original-JRE fixture. Actual Kk -> Kl -> patched JR and original Kk
 * draw/advance execute; SN only records calls. No Kh constructor, Hi, Main or GL. */
@SuppressWarnings({"rawtypes", "unchecked"})
public final class ContinueWrapTest {
    static int checks;
    static PixelLayout.Metrics metrics;
    static final int X=104, Y=206;
    static final String MAUSER="别担心，这只是机器人，不过……我们还会再次出发。";
    public static void main(String[] args) throws Exception {
        if(args.length!=1)throw new IllegalArgumentException("ContinueWrapTest pinned-bbc2.fnt");
        try(InputStream in=new FileInputStream(args[0])){metrics=DialogueWrap.readMetrics(in);}
        originalCallerEvidence();
        run(MAUSER,MAUSER);
        // Actual merged DefeatHints.Generic.map (DJ8d38a565f016814174ef):
        // raw80px page2 starts with " NAVIGATE" and original amn loses the final '!'.
        String mapHint="要是需要找路，就从你的 P.A.W. 菜单里打开 NAVIGATE 子菜单！";
        run(mapHint,mapHint);
        String variable="@DerekChipReport@ZoneName@EmuButtons@BOYPC@GIRLPC";
        String expanded=repeat(MAUSER,5);
        run(variable,expanded);
        run("@DerekChipReport",repeat("It looks like there is one chip left in the next zone. ",5).trim());
        System.out.println("PASS ContinueWrap "+checks+" assertions: actual Kh option/caller CP, NY/Om, Kk->Kl->JR, 80px, 12x3 grid, SN x104/y206/190/174, real reveal/skip/pages/final JI, original entry event once");
    }
    static void originalCallerEvidence() throws Exception {
        CP kh=new CP("PRG/Kh"), kl=new CP("PRG/Kl"), kk=new CP("PRG/Kk");
        check(kh.string("ui.defeated.retry") && kh.string("ui.defeated.end") && kh.string("ui.defeated.debrief"),"Kh actual three Continue/defeat option keys");
        check(kh.string("ClassicGameOverSpectrogram") && kh.string("CosmoGameOverBGSpawn"),"Kh actual game-over screen assets, not inferred from screenshot");
        check(kh.method("PRG/Kk","<init>","(LPRG/Kh;)V"),"Kh owns original Kk");
        check(kh.method("PRG/Kk","a","(LPRG/afD$g;DLPRG/apr;)V"),"Kh passes dialogue into Kk");
        check(kh.method("PRG/Kk","a","(LPRG/SN;IIDZLPRG/apr;)V"),"Kh draws through original Kk");
        check(kk.method("PRG/Kl","a","(LPRG/afD$g;DLPRG/azA;LPRG/apr;)LPRG/JQ$a;"),"Kk original initial caller is Kl");
        check(kl.field("PRG/NY","MODULE$","LPRG/NY;"),"Kl uses actual NY singleton, never a mock numeric12");
        check(kl.method("PRG/JR","a","(LPRG/afD$g;LPRG/amq;LPRG/amv;LPRG/apr;)LPRG/aAJ;"),"Kl calls the patched original JR descriptor");
        check(kk.field("PRG/NY","MODULE$","LPRG/NY;"),"Kk original draw also cuts at NY");
        eq(NY.MODULE$.a(),12,"original NY cut");
        check(JR.MODULE$.b()==Om.MODULE$,"original JR rows singleton is Om");
        eq(Om.MODULE$.a(),3,"original three rows");
        eq(It.MODULE$.a(13),X,"original Kh caller horizontal coordinate");
        eq(It.MODULE$.b(25),Y,"original Kh caller vertical coordinate");
    }
    static void run(String source,String replacement) throws Exception {
        int[] substitutions={0};
        SA sa=new SA(null,null,ignored -> (azz<amr.d,amr.d>)(value -> {
            substitutions[0]++;
            eq(value.a(),source,"SA receives entire pre-wrap source, not one old page");
            String result=value.a();
            if(source.startsWith("@")) {
                // Same String.replace contract as the real five-variable function;
                // the expansion is intentionally much longer than any original page.
                String[] vars={"@DerekChipReport","@ZoneName","@EmuButtons","@BOYPC","@GIRLPC"};
                for(String variable:vars)result=result.replace(variable,variable.equals("@DerekChipReport")?replacement:"");
            }
            return new amr.d(result);
        }),null);
        DialogueWrapTest.FixtureState state=new DialogueWrapTest.FixtureState(sa);
        String actor=new String("Mauser"), expression=new String("default");
        afD.g dialogue=new afD.g("DefeatHints","ContinueFixture",null,(aEO)list(
            new afD.n(0,actor,expression,source),new afD.f(0,new afp(null))));
        // Does NOT construct Kh: only Kk's incomplete unsuppressed sound branch needs it.
        Kk controller=new Kk(null);
        controller.a(dialogue,100.0,state);
        eq(substitutions[0],1,"actual Kl/JR complete SA exactly once");
        eq(state.events.events,1,"original Kl executes script event once on entry");
        eq(state.visited.visits,1,"original Kl visited bookkeeping once on entry");
        JQ.a first=controller.a().f();
        check(first.e()==actor,"initial actor reference survives original caller");
        azK expr=first.f();
        eq(expr.f(),expression,"expression value survives original caller");
        int expectedPages=1+first.h().length();
        check(expectedPages>=1,"sample produces a complete original page");
        if(source.startsWith("@"))check(expectedPages>1,"long substitutions paginate instead of truncating");
        StringBuilder recovered=new StringBuilder();
        int finalSignals=0;
        for(int pageIndex=0;pageIndex<expectedPages;pageIndex++) {
            JQ.a page=controller.a().f();
            check(page.e()==actor,"actor identity across original next-page transitions");
            check(page.f()==expr,"expression tuple identity across original next-page transitions");
            eq(page.h().length(),expectedPages-pageIndex-1,"original remaining-page count");
            String grid=page.a().a();
            eq(grid.length(),36,"Continue retains original NY12 x Om3 serialization");
            check(!grid.contains("-"),"no synthetic hyphen in final pages");
            for(int row=0;row<3;row++) {
                String line=rtrim(grid.substring(row*12,(row+1)*12));
                recovered.append(line);
                bound(line);
                check(line.codePoints().filter(cp -> Character.UnicodeScript.of(cp)==Character.UnicodeScript.HAN).count()<=8,"at most eight Han per Continue row; mixed ASCII remains pixel-measured");
            }
            amn animated=page.a();
            for(int tick=0;tick<=36;tick++) {
                double time=animated.e()+tick*animated.g()+0.00001;
                int reveal=animated.a(time,true);
                String masked=amw.MODULE$.a(grid,reveal);
                eq(animated.a(time),masked,"real amn reveal agrees with original amw mask");
                draw(controller,state,page,time,masked);
            }
            // Original button timing: first press after .2s completes animation,
            // second press after its completion+.2s advances or yields terminal JI.
            double click=animated.e()+0.21;
            JP skipped=controller.a(true,click,state);
            check(skipped==JH.MODULE$,"original first click skips, never completes dialogue");
            JQ.a skipPage=controller.a().f();
            eq(skipPage.a().a(),grid,"skip preserves full serialized page");
            check(skipPage.a()!=animated,"real amn skip copy is retained");
            eq(skipPage.h().length(),page.h().length(),"skip cannot consume a next page");
            check(skipPage.a().c(click+0.001),"real skip deadline completes animation");
            draw(controller,state,skipPage,click+0.001,grid);
            JP next=controller.a(true,click+0.21,state);
            if(pageIndex+1==expectedPages) {
                check(next==JI.MODULE$,"only terminal advance produces original final JI");finalSignals++;
                check(controller.a().f().h().b(),"terminal page has normal empty remainder");
            } else check(next==JH.MODULE$,"nonterminal advance retains original JH");
            eq(substitutions[0],1,"no page/skip performs a second SA");
            eq(state.events.events,1,"original event remains once throughout every page and final signal");
            eq(state.visited.visits,1,"no repeated visited effects during paging");
        }
        eq(finalSignals,1,"one terminal signal while consuming the original session");
        eq(recovered.toString().replace(" ",""),replacement.toUpperCase().replace(" ",""),"complete final replacement conserved across all pages");
    }
    static void draw(Kk controller,apr state,JQ.a page,double time,String expectedMask) {
        List<Draw> draws=new ArrayList<Draw>();
        SN sn=(SN)Proxy.newProxyInstance(ContinueWrapTest.class.getClassLoader(),new Class<?>[]{SN.class},(proxy,method,args)->{
            if(method.getName().equals("b") && method.getParameterCount()==0)return "default";
            if(method.getName().equals("a") && Arrays.equals(method.getParameterTypes(),new Class<?>[]{String.class,int.class,int.class,String.class})) {
                draws.add(new Draw((String)args[0],(Integer)args[1],(Integer)args[2]));return null;
            }
            if(method.getReturnType()==boolean.class)return false;
            if(method.getReturnType()==int.class)return 0;
            return null;
        });
        controller.a(sn,X,Y,time,true,state);
        eq(draws.size(),4,"actual Kk emits three NY-cut body rows plus actor label");
        for(int row=0;row<3;row++) {
            Draw drawn=draws.get(row);
            eq(drawn.text,expectedMask.substring(row*12,(row+1)*12).toUpperCase(),"actual Kk row is original uppercase mask");
            eq(drawn.x,X,"original Continue body x; no radio +72 offset");
            eq(drawn.y,Y-row*16,"actual original row spacing is sixteen");
            bound(rtrim(drawn.text));
            check(drawn.x+80<=256,"original 256px logical canvas contains Continue x+80 budget");
        }
        eq(draws.get(3).text,"[MAUSER]","original actor label remains intact");
        eq(draws.get(3).x,X,"original actor x");eq(draws.get(3).y,Y+8,"original actor y");
    }
    static void bound(String line) {
        PixelLayout.Plan p=PixelLayout.layout(line,metrics,new PixelLayout.Profile(new PixelLayout.Rect(0,0,80,48),16,PixelLayout.Insets.NONE));
        check(!p.overflow && p.inkBounds.width()<=80,"actual pinned glyph/kerning line fits80px");
        check(X+p.inkBounds.right<=X+80,"actual rightmost ink cannot exceed original x+80");
    }
    static final class Draw {
        final String text;final int x,y;
        Draw(String text,int x,int y){this.text=text;this.x=x;this.y=y;}
    }
    static final class CP {
        final Object[] cp;final int[] tags;
        CP(String name) throws IOException {
            try(DataInputStream in=new DataInputStream(ContinueWrapTest.class.getResourceAsStream("/"+name+".class"))) {
                if(in.readInt()!=0xcafebabe)throw new IOException("class magic");
                in.readUnsignedShort();eq(in.readUnsignedShort(),52,"original game class major52");
                int count=in.readUnsignedShort();cp=new Object[count];tags=new int[count];
                for(int i=1;i<count;i++) {
                    int tag=tags[i]=in.readUnsignedByte();
                    switch(tag) {
                        case 1:cp[i]=in.readUTF();break;
                        case 3:case 4:in.readInt();break;
                        case 5:case 6:in.readLong();i++;break;
                        case 7:case 8:case 16:case 19:case 20:cp[i]=in.readUnsignedShort();break;
                        case 9:case 10:case 11:case 12:case 17:case 18:cp[i]=new int[]{in.readUnsignedShort(),in.readUnsignedShort()};break;
                        case 15:in.readUnsignedByte();in.readUnsignedShort();break;
                        default:throw new IOException("CP tag "+tag);
                    }
                }
            }
        }
        boolean string(String text){for(int i=1;i<cp.length;i++)if(tags[i]==8 && text.equals(cp[(Integer)cp[i]]))return true;return false;}
        boolean method(String owner,String name,String desc){return ref(10,owner,name,desc)||ref(11,owner,name,desc);}
        boolean field(String owner,String name,String desc){return ref(9,owner,name,desc);}
        boolean ref(int tag,String owner,String name,String desc) {
            for(int i=1;i<cp.length;i++)if(tags[i]==tag) {
                int[] r=(int[])cp[i], nat=(int[])cp[r[1]];
                if(owner.equals(cp[(Integer)cp[r[0]]]) && name.equals(cp[nat[0]]) && desc.equals(cp[nat[1]]))return true;
            }
            return false;
        }
    }
    static String rtrim(String text){int end=text.length();while(end>0 && text.charAt(end-1)==' ')end--;return text.substring(0,end);}
    static aEO list(Object...values){aEO out=aFC.MODULE$;for(int i=values.length-1;i>=0;i--)out=new aEg(values[i],out);return out;}
    static String repeat(String s,int n){StringBuilder out=new StringBuilder();while(n-->0)out.append(s);return out.toString();}
    static void check(boolean yes,String label){checks++;if(!yes)throw new AssertionError(label);}
    static void eq(Object a,Object b,String label){check(Objects.equals(a,b),label+": "+a+" != "+b);}
}
