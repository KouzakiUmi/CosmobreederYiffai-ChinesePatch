import PRG.*;
import cosmoloc.layout.*;
import java.net.*;
import java.lang.reflect.*;
import java.io.*;
import java.util.*;

/** Strict source-index/geometry regression, plus side-by-side frozen amn oracle. */
@SuppressWarnings({"rawtypes","unchecked"})
public final class CoreRegression {
 static long checks; static int oldLosses, pages;
 static void ok(boolean b,String s){checks++;if(!b)throw new AssertionError(s);}
 static void eq(Object a,Object b,String s){ok(Objects.equals(a,b),s+": ["+a+"] != ["+b+"]");}
 static String strip(String s){return s.replace("<p>","").replace("\r","").replace("\n","").replace("\u2028","").replace("\u2029","");}
 static aEO one(Object x){return new aEg(x,(aEO)aFC.MODULE$);}
 public static void main(String[] args)throws Exception {
  Locale locale=Locale.getDefault();
  try(URLClassLoader old=new URLClassLoader(new URL[]{new File(args[0]).toURI().toURL()},null)) {
   Class<?> amoOld=old.loadClass("PRG.amo"), amnOld=old.loadClass("PRG.amn");
   Object factory=amoOld.getField("MODULE$").get(null);
   Method make=amoOld.getMethod("a",String.class,double.class);
   Method index=amnOld.getMethod("a",double.class,boolean.class), end=amnOld.getMethod("i");
   Method shown=amnOld.getMethod("a",double.class);
   String[] texts={" 中","\n中文这","\n   中\n文","  中文缩进。","\n\n中文最后字", "\n\n\n中文下一行", "中文<p>AAAAAAAAAAAAAAAAAAAAAAAAAAAA，结束", "中文——英文 WORDS AND LONGWORDS终。", "甲……文——这---丁...字"};
   PixelLayout.Metrics ten;try(InputStream in=CoreRegression.class.getResourceAsStream("/bbc2.fnt")){ten=DialogueWrap.readMetrics(in);}
   try { ten.glyph(0x10ffff); throw new AssertionError("unsupported glyph silently accepted"); }
   catch(IllegalArgumentException expected) { checks++; }
   for(String text:texts) for(int q:new int[]{12,20,28}) {
    PixelLayout.Metrics metrics=q==28?StoryFont12.metrics():ten; double width=q==12?80:q==20?150:240;
    List<DialogueGrid.Page> expected=q==28?DialogueWrap.storyPages(text):DialogueWrap.pages(text,q,width,metrics);
    aEO formatted=q==28?DialogueWrap.story(one(new aAJ(new amr.h(text,"core"),"normal"))):DialogueWrap.radio(one(new aAZ(new amr.h(text,"core"),"actor",new aAw("normal"))),q==12?NY.MODULE$:Ob.MODULE$,Om.MODULE$,new SA(null,null,ignored->(azz<amr.d,amr.d>)(x->x),null));
    eq(formatted.length(),expected.size(),"real formatter page count");
    StringBuilder recovered=new StringBuilder();int p=0;
    for(aEO rest=formatted;!rest.b();rest=(aEO)rest.E(),p++) {
     Object tuple=rest.s();String grid=q==28?((amr.d)((aAJ)tuple).a()).a():((amr.d)((aAZ)tuple).a()).a();pages++;
     eq(grid,expected.get(p).grid,"no shifting/deleting indentation or blank rows");
     eq(grid.length(),q*3,"legacy shape");
     for(String line:expected.get(p).lines) {
      recovered.append(line);ok(line.length()<=q,"UTF16 budget");
      PixelLayout.Plan plan=PixelLayout.layout(line,metrics,new PixelLayout.Profile(new PixelLayout.Rect(0,0,width,48),16,PixelLayout.Insets.NONE));
      ok(!plan.overflow,"pixel budget");
      ok(!line.equals("，"),"no artificial lone comma line");
     }
     Object before=make.invoke(factory,grid,100.0);amn after=amo.MODULE$.a(grid,100.0);
     eq(after.i(),end.invoke(before),"exact original completion time");
     for(int tick=0;tick<q*3+1;tick++) {
      double time=100.0+tick*after.g()+0.000001;
      if(time<after.i()) {
       eq(after.a(time,true),index.invoke(before,time,true),"intermediate source index unchanged");
       eq(after.a(time),shown.invoke(before,time),"intermediate mask unchanged");
      }
     }
     eq(after.a(1e9),grid,"natural completion contains final ink and original whitespace");
     if(!grid.equals(shown.invoke(before,1e9)))oldLosses++;
     amn skip=after.a(grid,100.0,new aAw(100.01),after.g());
     eq(skip.a(100.02),grid,"skip completion contains all source ink");
     eq(SubtitleLayout.animationGrid(grid,q),grid,"VSN grid identity");
    }
    eq(recovered.toString(),strip(text).toUpperCase(locale),"source text and spaces exact conservation");
   }
   ok(oldLosses>=10,"frozen real amn reproduces leading-space terminal losses");
   for(int q:new int[]{12,20,28})for(int n=1;n<=100;n++) {
    String text=repeat("A",n)+"，中文……最——尾";
    PixelLayout.Metrics m=q==28?StoryFont12.metrics():ten;int width=q==12?80:q==20?150:240;
    StringBuilder joined=new StringBuilder();
    for(DialogueGrid.Page p:DialogueGrid.formatCapped(text,m,q,3,width))for(String line:p.lines){joined.append(line);ok(!line.equals("，"),"capped punctuation attached");ok(line.length()<=q,"cap");}
    eq(joined.toString(),text,"stress conservation");
   }
   for(String atomic:new String[]{"……","——","...","--"}) {
    String text="甲文"+atomic+"中文";
    PixelLayout.Plan plan=PixelLayout.layout(text,StoryFont12.metrics(),new PixelLayout.Profile("atomic","core",new PixelLayout.Rect(0,0,240,1000),16,PixelLayout.Insets.NONE,3));
    for(PixelLayout.Line line:plan.lines) for(PixelLayout.Unit u:line.units) if(u.display.start==2)eq(text.substring(u.display.start,u.display.end),atomic,"atomic dash/ellipsis run");
   }
  }
  eq(Locale.getDefault(),locale,"default Locale never modified");
  System.out.println("PASS CoreRegression checks="+checks+" pages="+pages+" frozen_amn_terminal_losses="+oldLosses+"; exact spaces, blank rows, original timeline/intermediate masks, skip, punctuation, atomic units");
 }
 static String repeat(String s,int n){StringBuilder b=new StringBuilder();while(n-->0)b.append(s);return b.toString();}
}
