package PRG;

import cosmoloc.layout.PixelLayout;
import java.util.ArrayList;
import java.util.List;

/** Entry-local scene adapters. Never changes the shared font, input, language or grid. */
public final class SceneText {
    private SceneText() { }
    private static final PixelLayout.Metrics GRID8 = new PixelLayout.Metrics() {
        public PixelLayout.Glyph glyph(int cp) {
            if (cp > 65535 || Character.isSurrogate((char)cp) || Character.isISOControl(cp))
                return null;
            return new PixelLayout.Glyph(8, 0, 0, cp == ' ' ? 0 : 8, cp == ' ' ? 0 : 8);
        }
        public double kerning(int a, int b) { return 0; }
    };

    /** The fixed classic8 grid contract is pinned by the candidate corpus test.
     * $ is a ROW style, not a printable glyph; | is an explicit scene row break.
     * All source is laid out before fixed-grid serialization; never calls old amw. */
    public static String fixedGrid(String text, int columns, int rows, boolean styles) {
        return grid(text, columns, rows, styles, GRID8, columns * 8);
    }
    static String grid(String text, int columns, int rows, boolean styles,
                       PixelLayout.Metrics metrics, int width) {
        requireSceneText(text);
        List<String> lines = new ArrayList<String>();
        for (String paragraph : text.split("\\|", -1)) {
            boolean styled = styles && paragraph.startsWith("$");
            String payload = styled ? paragraph.substring(1) : paragraph;
            int capacity = columns - (styled ? 1 : 0);
            // In these fixed grids every supported unit advances at least 8px.
            // A single width constraint therefore also enforces the UTF-16 cap;
            // no second substring cap can introduce a new forbidden break.
            int budget = Math.min(width - (styled ? 8 : 0), capacity * 8);
            PixelLayout.Plan p = PixelLayout.layout(payload, metrics,
                new PixelLayout.Profile(new PixelLayout.Rect(0,0,budget,1000000), 16, PixelLayout.Insets.NONE));
            if (p.overflow) throw new IllegalArgumentException("Scene text has unsupported glyph/width: " + text);
            for (PixelLayout.Line line : p.lines) {
                String value = payload.substring(line.display.start, line.display.end)
                    .replace("\r", "").replace("\n", "").replace("\u2028", "").replace("\u2029", "");
                if (value.length() > capacity) throw new IllegalArgumentException("Scene grid unit capacity");
                lines.add((styled ? "$" : "") + value);
            }
        }
        if (lines.size() > rows) throw new IllegalArgumentException("Scene text exceeds " + columns + " columns x " + rows + " reachable rows: " + text);
        StringBuilder result = new StringBuilder(columns * rows);
        for (String line : lines) {
            result.append(line);
            for (int n=line.length(); n<columns; n++) result.append(' ');
        }
        while (result.length() < columns * rows) result.append(' ');
        return result.toString();
    }
    /** Kc's style marker lives outside the 28 drawable columns. The old
     * serializer incorrectly counted it as a column and dropped final ']'.
     * Reproduce the pinned Kc row renderer's pass gating and exact colour. */
    @SuppressWarnings({"rawtypes", "unchecked"})
    public static void dataBlock(SN sn,String text,boolean pass,int x,int baseY,int offset) {
        requireSceneText(text);
        boolean chinese=wide(text);
        String role=chinese?sn.b():"classic";
        PixelLayout.Metrics metrics=chinese?LayoutBridge.metrics(LayoutBridge.font(sn,role)):GRID8;
        int step=chinese?10:8;
        List<String> lines=new ArrayList<String>();
        for(String paragraph:text.split("\\|",-1)) {
            boolean style=paragraph.startsWith("$");
            String payload=style?paragraph.substring(1):paragraph;
            PixelLayout.Plan plan=PixelLayout.layout(payload,metrics,
                new PixelLayout.Profile(new PixelLayout.Rect(0,0,224,1000000),16,PixelLayout.Insets.NONE));
            if(plan.overflow)throw new IllegalArgumentException("Data book glyph/width: "+text);
            for(PixelLayout.Line line:plan.lines) {
                String value=payload.substring(line.display.start,line.display.end)
                    .replace("\r", "").replace("\n", "").replace("\u2028", "").replace("\u2029", "");
                lines.add((style?"$":"")+value);
            }
        }
        if(lines.size()>3)throw new IllegalArgumentException("Data book exceeds three reachable 224px rows: "+text);
        // Plan and check the WHOLE description before the first draw.
        for(int row=0;row<lines.size();row++) {
            String value=lines.get(row);boolean styled=value.startsWith("$");
            if(styled!=pass)continue;
            if(styled) sn.a(value.substring(1),x,baseY-row*step+offset,
                new aBa<Object,Object,Object,Object>(0.31299999356269836f,0.18799999356269836f,0f,1f),chinese?role:sn.c());
            else sn.a(value,x,baseY-row*step+offset,chinese?role:sn.b());
        }
    }
    /** Data-book list rows are 8px apart; the default10 Chinese name overlaps
     * the next row. Change only this consumer, never the stored name or grid. */
    public static void dataName(SN sn,String text,int x,int y,String role) {
        sn.a(text,x,y,wide(text)?"classic":role);
    }
    public static String breedFormat(amw original, String text, amq cols, amv rows, boolean normalize, SN sn) {
        if (cols != Ol.MODULE$ || rows != NW.MODULE$ || normalize)
            throw new IllegalArgumentException("Unregistered Ew formatter");
        arp font=LayoutBridge.font(sn, sn.b());
        return grid(text, 28, 2, false, LayoutBridge.metrics(font), 224);
    }
    public static String breedAffinity(amw original,String text,amq cols,amv rows,boolean normalize,SN sn) {
        return breedBlock(original,text,cols,rows,normalize,sn,true);
    }
    public static String breedNeeds(amw original,String text,amq cols,amv rows,boolean normalize,SN sn) {
        return breedBlock(original,text,cols,rows,normalize,sn,false);
    }
    private static boolean wide(String text) {
        for(int i=0;i<text.length();i++)if(text.charAt(i)>=0x2e80&&text.charAt(i)<=0x9fff)return true;
        return false;
    }
    private static String breedBlock(amw original,String text,amq cols,amv rows,boolean normalize,SN sn,boolean affinity) {
        if(cols!=Ol.MODULE$||rows!=NW.MODULE$||normalize)throw new IllegalArgumentException("Unregistered breed block");
        boolean chinese=wide(text);
        int count=affinity&&!chinese?3:2,step=chinese?12:8,baseY=affinity?110:78;
        String role=sn.b();arp font=LayoutBridge.font(sn,role);
        String block;
        try {block=grid(text,28,count,false,LayoutBridge.metrics(font),224);}
        catch(IllegalArgumentException tooHigh) {
            // Author-specified 3-row Chinese affinity exists in the real corpus.
            // Its original 8px baselines are a genuine compact-font requirement,
            // not a reason to discard the third explicit row or merge its words.
            if(!affinity||!chinese||text.split("\\|",-1).length!=3||!tooHigh.getMessage().startsWith("Scene text exceeds"))throw tooHigh;
            role="classic";font=LayoutBridge.font(sn,role);count=3;step=8;
            block=grid(text,28,count,false,LayoutBridge.metrics(font),224);
        }
        // Every selected row is validated before drawing. No fixed old zip/index
        // consumer ever receives a nonempty fragment, so it cannot clip the tail.
        for(int row=0;row<count;row++) {
            String value=rtrim(block.substring(row*28,(row+1)*28));
            if(!value.isEmpty())sn.a(value,16,baseY-row*step,role);
        }
        StringBuilder empty=new StringBuilder(56);while(empty.length()<56)empty.append(' ');
        return empty.toString();
    }
    public static void breedDraw(SN sn, String text, int x, int y, String role) {
        // The registered old consumers receive only blank placeholders after the
        // complete block has been rendered with its stable full-source profile.
        String value=rtrim(text);if(!value.isEmpty())sn.a(value,x,y,role);
    }
    public static String cardFormat(amw original, String text, amq cols, amv rows, boolean normalize) {
        if (cols != NV.MODULE$ || (rows != NU.MODULE$ && rows != NT.MODULE$) || !normalize)
            throw new IllegalArgumentException("Unregistered Jm formatter");
        // Preserve the game's exact normalization, BEFORE replacing only its lossy formatter.
        String display=ams.MODULE$.a(original.a(text));
        return fixedGrid(display,16,rows.a(),false);
    }
    public static void cardDraw(SN sn, String text, int x, int y, String role) {
        // Its 8px baselines and 128px right panel require classic8, including stats.
        if (fixedWidth(LayoutBridge.font(sn,"classic"),text)>128)
            throw new IllegalArgumentException("Card row exceeds original 128px panel: "+text);
        sn.a(text,x,y,"classic");
    }
    public static String achievementFormat(amw original, String text, amq cols, amv rows, boolean normalize) {
        if (cols != Oi.MODULE$ || rows != Oa.MODULE$ || normalize)
            throw new IllegalArgumentException("Unregistered kn formatter");
        return fixedGrid(text,30,2,false);
    }
    private static int fixedWidth(arp font,String text) {
        LayoutBridge.requireRenderableLine(font.a,text);
        int advance=0;
        for(int i=0;i<text.length();i++) {
            arp.b g=font.a.a(text.charAt(i));
            if(g.l!=8 || font.a.o!=1 || font.a.p!=1 || font.a.q)
                throw new IllegalStateException("Scene fixed grid requires pinned classic8");
            advance+=g.l;
        }
        return advance;
    }
    /** Real arr glyph layout (including offsets, kerning, padding), not length*8.
     * Return the native SN origin, including first-quad padding compensation. */
    public static int center(SN sn,String text,int width,String role) {
        arp font=LayoutBridge.font(sn,role);
        LayoutBridge.requireRenderableLine(font.a,text);
        if(text.length()==0) return width/2;
        arr measured=new arr();
        measured.a(font,text,0,text.length(),new ara(1,1,1,1),0,8,false,null);
        if(measured.d > width) throw new IllegalArgumentException("Single-line scene label exceeds "+width+"px: "+text);
        return (int)Math.floor((width-measured.d)/2.0)+Math.round(font.a.h);
    }
    public static int mapCenter(SN sn,String text,int width,String ignoredMeasureRole) {
        return center(sn,text,width,sn.b());
    }
    public static void mapDraw(SN sn,String text,int ignoredX,int y,String role) {
        sn.a(text,center(sn,text,256,role),y,role);
    }
    public static void achievementDraw(SN sn,String text,int ignoredX,int y,String role) {
        fixedWidth(LayoutBridge.font(sn,role),text);
        sn.a(text,center(sn,text,256,role),y,role);
    }
    public static void achievementDraw(SN sn,String text,int ignoredX,int y,aBa<Object,Object,Object,Object> colour,String role) {
        fixedWidth(LayoutBridge.font(sn,role),text);
        sn.a(text,center(sn,text,256,role),y,colour,role);
    }
    private static void requireSceneText(String text) {
        for(int at=0;at<text.length();at++) {
            char ch=text.charAt(at);
            if(Character.isSurrogate(ch)||Character.getType(ch)==Character.FORMAT
                    ||(Character.isISOControl(ch)&&ch!='\r'&&ch!='\n'))
                throw new IllegalArgumentException("Unsupported scene text code unit U+"+Integer.toHexString(ch));
        }
    }
    private static String rtrim(String text) {
        int end=text.length(); while(end>0 && text.charAt(end-1)==' ')end--;
        return text.substring(0,end);
    }
}
