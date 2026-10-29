package PRG;

/** Local eight-cell fields only. No global Id/It/font mutation or save/input calls.
 * The original name quota, three slot pitch, gender cell and neighbouring columns
 * remain byte-for-byte geometry. classic8 is necessary for these 64x8 fields.
 */
public final class CompactFields {
    public static final int NAME_WIDTH = 64, CELL = 8;
    private CompactFields() { }
    public static boolean compact(String text) {
        for (int i=0;i<text.length();i++) if (text.charAt(i)>127) return true;
        return false;
    }
    /** True advance from the font consumed by the renderer, not relabelled 10px. */
    public static int width(SN sn, String text) {
        return ItemFont8.width(LayoutBridge.font(sn, "classic"), text);
    }
    private static void line(SN sn,String text,int x,int y) {
        if (!text.isEmpty()) LayoutBridge.draw(sn,text,x,y,"classic");
    }
    /** LY first row: split exactly at its existing eight-code-unit field boundary.
     * Preserve the original formatter and metadata; no name storage is rewritten.
     */
    public static void saveRow(Id original,SN sn,String text,int x,int y) {
        if (!compact(text)) { original.a(sn,text,x,y); return; }
        int end=Math.min(8,text.length());
        String name=text.substring(0,end);
        if (compact(name)) line(sn,name,x,y); else original.a(sn,name,x,y);
        String tail=text.substring(end);
        if (compact(tail)) line(sn,tail,x+NAME_WIDTH,y);
        else original.a(sn,tail,x+NAME_WIDTH,y);
    }
    /** LY lower row also has only an 8px baseline separation. */
    public static void saveLower(Id original,SN sn,String text,int x,int y) {
        if (compact(text)) line(sn,text,x,y); else original.a(sn,text,x,y);
    }
    public static void name(Id original,SN sn,String text,int x,int y) {
        if (compact(text)) line(sn,text,x,y); else original.a(sn,text,x,y);
    }
    /** Same role and actual glyph advances as name(); original eight-cell cap. */
    public static void nameCursor(SN sn,String image,int ignoredX,int y,int w,int h,Mb field) {
        String raw=field.k().m();
        if (!compact(raw)) { sn.a(image,ignoredX,y,w,h); return; }
        int x=field.e_()+width(sn,raw);
        sn.a(image,x,y,CELL,CELL);
    }
    /** Letter-button normal and highlighted repaint use the same 8px bitmap;
     * their existing 8x8 white selection background stays in place. */
    public static void letter(SN sn,String text,int x,int y,String role) {
        if (compact(text)) line(sn,text,x,y); else sn.a(text,x,y,role);
    }
    public static void selectedLetter(SN sn,String text,int x,int y,aBa color,String role) {
        if (!compact(text)) { sn.a(text,x,y,color,role); return; }
        arp font=LayoutBridge.font(sn,"classic");
        arp.b first=font.a.a(text.charAt(0));
        int correction=first.n?0:Math.round(first.j+font.a.h);
        sn.a(text,x+correction,y,color,"classic");
    }
}
