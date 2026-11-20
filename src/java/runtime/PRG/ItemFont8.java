package PRG;

import java.lang.ref.WeakReference;
import java.util.*;

/** Only registered Le fields; existing atlas roles, no font scaling or input IO.
 * Name/category/icon rows keep their original geometry. The 122x26 description
 * interior is used as two 10px lines when possible, otherwise three classic8
 * lines. Overflow has a paced, labelled complete-page cycle, never a cut/throw.
 */
public final class ItemFont8 {
    public static final String ROLE="classic";
    public static final int NAME_WIDTH=72, DESCRIPTION_WIDTH=112, LINE_STEP=8;
    private static final List<WeakReference<Object>> NAMES=new ArrayList<WeakReference<Object>>();
    private static final List<WeakReference<Object>> DESCRIPTIONS=new ArrayList<WeakReference<Object>>();
    private static final Map<Lb,Float> CLOCK=new WeakHashMap<Lb,Float>();
    private static final Map<Lb,String> SOURCE=new WeakHashMap<Lb,String>();
    private static final Map<Lg,Float> NAME_CLOCK=new WeakHashMap<Lg,Float>();
    private static final Map<Lg,String> NAME_SOURCE=new WeakHashMap<Lg,String>();
    public static synchronized void updateName(Lg w,float delta){if(contains(NAMES,w)&&Float.isFinite(delta)&&delta>0)NAME_CLOCK.put(w,Math.min(86400f,(NAME_CLOCK.containsKey(w)?NAME_CLOCK.get(w):0f)+delta));}
    private static synchronized float nameElapsed(Lg w,String text){if(selectionChanged(w)||!text.equals(NAME_SOURCE.get(w))){NAME_SOURCE.put(w,text);NAME_CLOCK.put(w,0f);}Float v=NAME_CLOCK.get(w);return v==null?0:v;}
    private static final Map<Object,WeakReference<Le>> OWNERS=new WeakHashMap<Object,WeakReference<Le>>();
    private static final Map<Object,WeakReference<Object>> SELECTION=new WeakHashMap<Object,WeakReference<Object>>();
    private ItemFont8() { }
    public static synchronized void registerName(Lg w){add(NAMES,w);}
    public static synchronized void registerDescription(Lb w){add(DESCRIPTIONS,w);CLOCK.put(w,0f);}
    public static synchronized void registerName(Lg w,Le owner){registerName(w);OWNERS.put(w,new WeakReference<Le>(owner));}
    public static synchronized void registerDescription(Lb w,Le owner){registerDescription(w);OWNERS.put(w,new WeakReference<Le>(owner));}
    private static boolean selectionChanged(Object widget){
        WeakReference<Le> ref=OWNERS.get(widget);Le owner=ref==null?null:ref.get();
        if(owner==null)return false;
        azK<?> option=owner.x().a();Object selected=option instanceof aAw?((aAw<?>)option).e():null;
        WeakReference<Object> previous=SELECTION.get(widget);Object old=previous==null?null:previous.get();
        SELECTION.put(widget,new WeakReference<Object>(selected));return old!=selected;
    }
    private static void add(List<WeakReference<Object>> a,Object w){if(w==null)throw new NullPointerException("item widget");if(contains(a,w))throw new IllegalStateException("duplicate item widget");a.add(new WeakReference<Object>(w));}
    private static synchronized boolean contains(List<WeakReference<Object>> a,Object w){boolean found=false;for(Iterator<WeakReference<Object>> i=a.iterator();i.hasNext();){Object v=i.next().get();if(v==null)i.remove();else if(v==w)found=true;}return found;}
    /** Existing Lb update receives seconds; no new input or game clock ownership. */
    public static synchronized void update(Lb w,float delta){if(contains(DESCRIPTIONS,w)&&Float.isFinite(delta)&&delta>0)CLOCK.put(w,Math.min(86400f,(CLOCK.containsKey(w)?CLOCK.get(w):0f)+delta));}
    private static synchronized float elapsed(Lb w,String text){if(selectionChanged(w)||!text.equals(SOURCE.get(w))){SOURCE.put(w,text);CLOCK.put(w,0f);}Float v=CLOCK.get(w);return v==null?0:v;}
    private static void validate(arp f){if(f.a.o!=1||f.a.p!=1||f.a.q)throw new IllegalStateException("unscaled integral item font required");}
    private static int advance(arp f,char c){arp.b g=f.a.a(c);if(Character.isSurrogate(c)||g==null||g.l<=0)throw new IllegalArgumentException("unsupported item glyph U+"+Integer.toHexString(c));return g.l;}
    /** Measured real glyph advance and kerning; no 10px glyph is reported as 8px. */
    public static int width(arp f,String s){validate(f);int w=0;for(int i=0;i<s.length();i++){if(i>0)w+=f.a.a(s.charAt(i-1)).a(s.charAt(i));w=Math.addExact(w,advance(f,s.charAt(i)));}return w;}
    public static void drawName(SN sn,String text,int x,int y,String original,Lg widget){
        if(!contains(NAMES,widget)||!hasChinese(text)){sn.a(text,x,y,original);return;}
        arp f=LayoutBridge.font(sn,ROLE);
        // Tight original 72px row is immediately above 16px item icons: classic8
        // prevents the 10px CJK ink from descending into their actual icon row.
        if(text.isEmpty())return; // preserve the original equipment blink gate
        float clock=nameElapsed(widget,text);
        if(width(f,text)>NAME_WIDTH) {
            String[] chunks=wrap(f,text,NAME_WIDTH);
            // Future overlong names remain inside the same row and each chunk
            // is displayed for eight seconds; the registered Lg update owns time.
            LayoutBridge.draw(sn,chunks[((int)(clock/8f))%chunks.length],x,y,ROLE);return;
        }
        LayoutBridge.draw(sn,text,x,y,ROLE);
    }
    public static boolean drawDescription(Lb w,SN sn,String text){
        if(!contains(DESCRIPTIONS,w))return false;
        float clock=elapsed(w,text);
        arp body=LayoutBridge.font(sn,"default"),small=LayoutBridge.font(sn,ROLE);
        String[] lines=wrap(body,text,DESCRIPTION_WIDTH);String role="default";int step=12;
        if(lines.length>2){lines=wrap(small,text,DESCRIPTION_WIDTH);role=ROLE;step=8;}
        int anchor=w.f_()+5; // original22 ->27: screen196, inside [130,196,252,222)
        if(lines.length<= (role.equals(ROLE)?3:2)){
            for(int i=0;i<lines.length;i++)if(!lines[i].isEmpty())LayoutBridge.draw(sn,lines[i],w.e_(),anchor-i*step,role);
            return true;
        }
        // Only truly overheight dynamic descriptions reach this route. Two full
        // content lines plus a visible page counter in the third 8px line.
        int pages=(lines.length+1)/2;
        float dwell=Math.max(8f,Math.min(20f,text.length()*0.35f/pages));
        int page=((int)(clock/dwell))%pages;
        for(int i=0;i<2&&page*2+i<lines.length;i++)if(!lines[page*2+i].isEmpty())LayoutBridge.draw(sn,lines[page*2+i],w.e_(),anchor-i*8,ROLE);
        LayoutBridge.draw(sn,(page+1)+"/"+pages,w.e_(),anchor-16,ROLE);
        return true;
    }
    private static boolean hasChinese(String t){for(int i=0;i<t.length();i++)if(t.charAt(i)>=0x2e80&&t.charAt(i)<=0x9fff)return true;return false;}
    private static boolean word(char c){return c<128&&(Character.isLetterOrDigit(c)||c=='\''||c=='-');}
    private static boolean noStart(char c){return "，。！？；：、）》】〕〉」』”’…,.!?;:%)]}".indexOf(c)>=0;}
    private static boolean noEnd(char c){return "（《【〔〈「『“‘([{ $".indexOf(c)>=0&&c!=' ';}
    /** Width-first wrapping with English-word preference and CJK punctuation
     * prohibition. All source units (including spaces) are retained. Explicit
     * pipe/CRLF breaks are interpreted before layout, never old q14/amw cuts.
     * Overwide unbroken Latin words use the last measured fitting boundary.
     */
    public static String[] wrap(arp f,String text,int maximum){
        validate(f);if(maximum<8)throw new IllegalArgumentException("item line too narrow");
        List<String> out=new ArrayList<String>();
        String normal=text.replace("\r\n","\n").replace('\r','\n').replace('|','\n');
        String[] paragraphs=normal.split("\n",-1);
        for(String p:paragraphs){
            if(p.isEmpty()){out.add("");continue;}
            int start=0;
            while(start<p.length()){
                int end=start;
                while(end<p.length()&&width(f,p.substring(start,end+1))<=maximum)end++;
                if(end==start)throw new IllegalArgumentException("single item glyph wider than field");
                if(end<p.length()){
                    int fit=end;
                    if(word(p.charAt(end-1))&&word(p.charAt(end))){int b=end;while(b>start&&word(p.charAt(b-1)))b--;if(b>start)end=b;}
                    while(end>start&&(noStart(p.charAt(end))||noEnd(p.charAt(end-1))))end--;
                    if(end==start)end=fit; // irreducible overwide atom, not a fabricated advance
                    // Keep paired ellipsis / em-dash on one side where possible.
                    if(end>start&&end<p.length()&&p.charAt(end)==p.charAt(end-1)&&(p.charAt(end)=='…'||p.charAt(end)=='—'))end--;
                    if(end==start)end=fit;
                }
                out.add(p.substring(start,end));start=end;
            }
        }
        return out.toArray(new String[out.size()]);
    }
}
