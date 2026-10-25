import PRG.*;
import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.regex.*;

/** Original-JRE integration: patched real Kr/Ks/Kc, actual final dictionary/font; no Main/GL. */
@SuppressWarnings({"rawtypes","unchecked"})
public final class EndingReportLayoutTest {
    static int checks, fields, descriptions;
    static Map<String,String> dictionary;
    static final Map<Integer,int[]> glyphs=new HashMap<Integer,int[]>();
    static final List<Draw> draws=new ArrayList<Draw>();
    static final aBa BASE=new aBa(1f,1f,1f,1f), FLASH=new aBa(1f,0f,0f,1f);
    static final class Draw {
        final String text,role;final int x,y;final Object colour;
        Draw(Object[] a){text=(String)a[0];x=(Integer)a[1];y=(Integer)a[2];colour=a.length==5?a[3]:null;role=(String)a[a.length-1];}
    }
    static final SN RECORD=(SN)Proxy.newProxyInstance(EndingReportLayoutTest.class.getClassLoader(),new Class<?>[]{SN.class},(p,m,a)->{
        if((m.getName().equals("b")||m.getName().equals("c"))&&m.getParameterCount()==0)return "default";
        if(m.getName().equals("a")&&a!=null&&(a.length==4||a.length==5)&&a[0] instanceof String&&a[a.length-1] instanceof String)draws.add(new Draw(a));
        if(m.getReturnType()==boolean.class)return false;if(m.getReturnType()==int.class)return 0;return null;
    });
    static final class Selector extends Iu {
        private static final long serialVersionUID=1L;
        azK selected;
        private Selector(){super(null,null,null,0,false);}
        @Override public azK a(){return selected;}
    }
    public static void main(String[] args)throws Exception {
        System.setOut(new PrintStream(System.out,true,"UTF-8"));
        if(args.length!=2)throw new IllegalArgumentException("classic.fnt final-dat av-dictionary.json (UTF-8 JSON)");
        byte[] font=Files.readAllBytes(Paths.get(args[0]));eq(hash(font),EndingReportLayout.FONT_SHA256,"actual classic font SHA");readFont(new String(font,StandardCharsets.UTF_8));
        dictionary=json(new String(Files.readAllBytes(Paths.get(args[1])),StandardCharsets.UTF_8));
        for(char ch:new char[]{'中','文','我','游','戏'}){int[] g=glyphs.get((int)ch);check(g!=null&&g[0]==8&&g[2]==8&&g[3]==8,"actual Chinese 8px font metrics");}
        SH sh=allocate(SH.class);put(sh,"b",(azz<String,SL>)(key->{String s=dictionary.get(key);if(s==null)throw new AssertionError("Missing actual dictionary key "+key);return new SL(s,key);}));
        Kr state=allocate(Kr.class);put(state,"d",sh);put(state,"p",BASE);put(state,"q",FLASH);put(state,"g",0.025);put(state,"f","100");put(state,"c",3600.0);
        // Execute the actual Ks dictionary loader/row zipper and real patched Kr entries.
        for(String prefix:new String[]{"ui.end.BadEnding.l","ui.end.Tier1.l","ui.end.Tier2.l","ui.end.Tier3.l","ui.end.Tier4.l","ui.end.cr"}) {
            draws.clear();azz renderer=(azz)Ks.MODULE$.a(prefix,0,10,false,sh).apply(state);renderer.apply(RECORD);
            for(int row=0;row<10;row++) {
                String key=prefix+row,source=dictionary.get(key);check(source!=null,"actual ending field "+key);
                String display=source.startsWith("*!")?source.replace("*!","  "):source;
                check(!display.contains("\n")&&!display.contains("\r")&&display.length()<=32,"field must fit unchanged 32 columns: "+key+" = ["+source+"]");
                List<Draw> line=atY(It.MODULE$.b(16-row));
                eq(join(line),display,"real Ks/Kr preserves all source and columns "+key);
                if(han(display)){eq(line.size(),1,"Han whole-line draw "+key);eq(line.get(0).role,"classic","Han actual classic role");eq(line.get(0).x,0,"original field x");}
                for(Draw d:line){check(d.colour==(source.startsWith("*!")?FLASH:BASE),"original marker colour identity");ink(d,0,256);}
                fields++;
            }
        }
        // Actual entries, including blink colour selection and unchanged ASCII Id per-char path.
        draws.clear();state.a("中文",3,16,RECORD);eq(draws.size(),1,"real patched plain Kr");eq(draws.get(0).x,24,"original col3");eq(draws.get(0).y,134,"original row16");check(draws.get(0).colour==BASE,"plain colour");
        draws.clear();state.a("中文",5,15,false,RECORD);check(draws.get(0).colour==FLASH,"real flashing colour");put(state,"s",1);draws.clear();state.a("中文",5,15,false,RECORD);check(draws.get(0).colour==BASE,"blink phase remains original");put(state,"s",0);
        for(String ascii:new String[]{"CLEAR","TIME","RATE","01:23:45","100%","0%","999999%"}) {
            draws.clear();state.a(ascii,3,9,RECORD);eq(join(draws),ascii,"dynamic/ASCII exact original");eq(draws.size(),ascii.length(),"ASCII retains original per-character Id path");
            for(int i=0;i<draws.size();i++){eq(draws.get(i).x,24+i*8,"original ASCII advance");eq(draws.get(i).role,"default","original ASCII role");}
        }
        // Real summary renderer also exercises CP CLEAR/TIME/RATE and dynamic metrics.
        Method summary=Ks.class.getDeclaredMethod("a",Kr.class,SN.class);summary.setAccessible(true);draws.clear();summary.invoke(null,state,RECORD);
        check(draws.stream().anyMatch(d->d.y==134&&d.x==24),"real Ks CLEAR anchor");
        check(draws.stream().anyMatch(d->d.y==126&&d.x==40),"real Ks TIME anchor");
        check(draws.stream().anyMatch(d->d.y==70&&d.x==40),"real Ks RATE anchor");
        // Entire actual data-book description inventory through Kc.b, not helper-only fixtures.
        Method panel=Kc.class.getDeclaredMethod("b",SN.class,boolean.class,int.class);panel.setAccessible(true);
        Kc book=allocate(Kc.class);Selector selector=allocate(Selector.class);put(book,"l",selector);put(book,"o",false);
        boolean ending=false,gameover=false;
        for(Map.Entry<String,String> e:dictionary.entrySet())if(e.getKey().startsWith("ui.data.")&&e.getKey().endsWith(".desc")) {
            data(panel,book,selector,e.getKey(),e.getValue());descriptions++;
            ending|=e.getKey().contains("EndingGood");gameover|=e.getKey().contains("GameOverAreaE")||e.getKey().contains("GameOverArea0");
        }
        check(ending&&gameover,"real EndingGood/GameOver data-book entries included");
        data(panel,book,selector,"fixture/long-Han",repeat("中",80));
        data(panel,book,selector,"fixture/style","$中文|普通正文");
        boolean rejected=false;try{data(panel,book,selector,"fixture/overflow",repeat("中",85));}catch(InvocationTargetException ex){rejected=ex.getCause() instanceof IllegalArgumentException;}
        check(rejected,"real patched Kc rejects overflow instead of zip dropping text");
        System.out.println("PASS EndingReportLayout checks="+checks+" actualEndingFields="+fields+" actualDataDescriptions="+descriptions+"; real Ks/Kr/Kc, original colours/blink/control/ASCII/dynamics, pinned classic8, no GL/visual claim");
    }
    static void data(Method panel,Kc book,Selector selector,String key,String source)throws Exception {
        SL value=new SL(source,key);IA item=new IA(0,0,value,(azy<SL>)(()->value),(azy<Zv>)(()->null),"default",null);selector.selected=new aAw(item);
        draws.clear();panel.invoke(book,RECORD,false,0);List<Draw> plain=new ArrayList<Draw>(draws);
        draws.clear();panel.invoke(book,RECORD,true,0);List<Draw> styled=new ArrayList<Draw>(draws);
        String expected=source.replace("|","").replace("$","").replace(" ","");
        List<Draw> ordered=concat(plain,styled);Collections.sort(ordered,(a,b)->Integer.compare(b.y,a.y));
        eq(join(ordered).replace(" ",""),expected,"actual Kc complete description no hidden source "+key);
        check(plain.size()<=3&&styled.size()<=3,"Kc original three-row capacity "+key);
        for(Draw d:concat(plain,styled)) {
            check(d.y==30||d.y==22||d.y==14,"unchanged Kc panel y row "+key);eq(d.x,16,"unchanged Kc x");
            if(han(d.text))eq(d.role,"classic","data Han font role");else eq(d.role,"default","data ASCII role");ink(d,16,240);
        }
    }
    static List<Draw> concat(List<Draw>a,List<Draw>b){List<Draw> c=new ArrayList<Draw>(a);c.addAll(b);return c;}
    static List<Draw> atY(int y){List<Draw> out=new ArrayList<Draw>();for(Draw d:draws)if(d.y==y)out.add(d);return out;}
    static String join(List<Draw> values){StringBuilder s=new StringBuilder();for(Draw d:values)s.append(d.text);return s.toString();}
    static boolean han(String s){for(int i=0;i<s.length();i++)if(Character.UnicodeScript.of(s.charAt(i))==Character.UnicodeScript.HAN)return true;return false;}
    static void ink(Draw d,int left,int right){int x=d.x;for(int i=0;i<d.text.length();i++){char cp=d.text.charAt(i);int[] g=glyphs.get((int)cp);check(g!=null,"actual classic glyph exists U+"+Integer.toHexString(cp));if(g[2]>0&&g[3]>0){int padding=cp<128?1:0;check(x+g[1]>=left-padding&&x+g[1]+g[2]<=right+padding,"BMFont box fits panel (ASCII atlas has declared 1px padding): "+d.text);}x+=g[0];}}
    static void readFont(String text){Pattern p=Pattern.compile("(\\w+)=(-?\\d+)");for(String line:text.split("\\r?\\n"))if(line.startsWith("char ")){Map<String,Integer> f=new HashMap<String,Integer>();Matcher m=p.matcher(line);while(m.find())f.put(m.group(1),Integer.valueOf(m.group(2)));glyphs.put(f.get("id"),new int[]{f.get("xadvance"),f.get("xoffset"),f.get("width"),f.get("height")});}}
    static String hash(byte[] bytes)throws Exception{StringBuilder s=new StringBuilder();for(byte b:MessageDigest.getInstance("SHA-256").digest(bytes))s.append(String.format("%02x",b&255));return s.toString();}
    static <T>T allocate(Class<T> type)throws Exception{Class<?> u=Class.forName("sun.misc.Unsafe");Field f=u.getDeclaredField("theUnsafe");f.setAccessible(true);return type.cast(u.getMethod("allocateInstance",Class.class).invoke(f.get(null),type));}
    static void put(Object target,String name,Object value)throws Exception{Field f=target.getClass().getDeclaredField(name);f.setAccessible(true);f.set(target,value);}
    static String repeat(String s,int n){StringBuilder b=new StringBuilder();while(n-->0)b.append(s);return b.toString();}
    static void check(boolean ok,String why){checks++;if(!ok)throw new AssertionError(why);}
    static void eq(Object a,Object b,String why){check(Objects.equals(a,b),why+": ["+a+"] != ["+b+"]");}
    // Minimal strict flat string dictionary parser; consumes the actual decoded JSON, not test translations.
    static Map<String,String> json(String source){int[] p={0};Map<String,String> out=new TreeMap<String,String>();space(source,p);expect(source,p,'{');space(source,p);while(source.charAt(p[0])!='}'){String k=string(source,p);space(source,p);expect(source,p,':');space(source,p);String v=string(source,p);if(out.put(k,v)!=null)throw new IllegalArgumentException("duplicate key");space(source,p);if(source.charAt(p[0])=='}')break;expect(source,p,',');space(source,p);}expect(source,p,'}');space(source,p);if(p[0]!=source.length())throw new IllegalArgumentException("JSON tail");return out;}
    static void space(String s,int[] p){while(p[0]<s.length()&&Character.isWhitespace(s.charAt(p[0])))p[0]++;}
    static void expect(String s,int[] p,char c){if(p[0]>=s.length()||s.charAt(p[0]++)!=c)throw new IllegalArgumentException("JSON syntax");}
    static String string(String s,int[] p){expect(s,p,'"');StringBuilder b=new StringBuilder();while(p[0]<s.length()){char c=s.charAt(p[0]++);if(c=='"')return b.toString();if(c=='\\'){c=s.charAt(p[0]++);if(c=='u'){b.append((char)Integer.parseInt(s.substring(p[0],p[0]+4),16));p[0]+=4;}else if(c=='n')b.append('\n');else if(c=='r')b.append('\r');else if(c=='t')b.append('\t');else if(c=='b')b.append('\b');else if(c=='f')b.append('\f');else if(c=='"'||c=='\\'||c=='/')b.append(c);else throw new IllegalArgumentException("JSON escape");}else {if(c<32)throw new IllegalArgumentException("JSON control");b.append(c);}}throw new IllegalArgumentException("JSON string");}
}
