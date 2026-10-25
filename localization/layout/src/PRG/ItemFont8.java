package PRG;

import java.lang.ref.WeakReference;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/** Only Chinese in the selected Le name and description, using existing classic8.
 * No font/texture creation: iF already registers classic with its owned atlas.
 * Original ASCII-only rendering, global scale, default10, grid/input and saves stay.
 */
public final class ItemFont8 {
    public static final String ROLE = "classic";
    public static final int NAME_WIDTH = 72, DESCRIPTION_WIDTH = 112, LINE_STEP = 8;
    private static final List<WeakReference<Object>> NAMES = new ArrayList<WeakReference<Object>>();
    private static final List<WeakReference<Object>> DESCRIPTIONS = new ArrayList<WeakReference<Object>>();
    private ItemFont8() { }

    public static synchronized void registerName(Lg widget) { add(NAMES, widget); }
    public static synchronized void registerDescription(Lb widget) { add(DESCRIPTIONS, widget); }
    private static void add(List<WeakReference<Object>> entries, Object widget) {
        if (widget == null) throw new NullPointerException("item8 widget");
        if (contains(entries, widget)) throw new IllegalStateException("duplicate item8 widget");
        entries.add(new WeakReference<Object>(widget));
    }
    private static synchronized boolean contains(List<WeakReference<Object>> entries, Object widget) {
        boolean found = false;
        for (Iterator<WeakReference<Object>> it = entries.iterator(); it.hasNext();) {
            Object live = it.next().get();
            if (live == null) it.remove();
            else if (live == widget) found = true;
        }
        return found;
    }

    private static void validate(arp font) {
        if (font.a.o != 1.0f || font.a.p != 1.0f || font.a.q || font.a.i != LINE_STEP)
            throw new IllegalStateException("item8 requires integral unscaled classic8 bitmap");
    }
    private static arp font(SN sn) {
        arp font = LayoutBridge.font(sn, ROLE);
        validate(font);
        return font;
    }
    private static int advance(arp font, char c) {
        arp.b glyph = font.a.a(c);
        // Original Latin records include 1px transparent padding (10px quads,
        // 8px advance); added CJK records are real 8x8 bitmap cells. Don't relabel
        // those padded Latin quads as 8px, or mutate their original metrics.
        if (Character.isSurrogate(c) || glyph == null || glyph.l <= 0 || glyph.l > 8
                || (c > 127 && (glyph.d < 0 || glyph.d > 8 || glyph.e < 0 || glyph.e > 8)))
            throw new IllegalArgumentException("item8 glyph outside classic8 contract U+" + Integer.toHexString(c));
        return glyph.l;
    }
    public static int width(arp font, String text) {
        validate(font);
        int width = 0;
        for (int i = 0; i < text.length(); i++) width = Math.addExact(width, advance(font, text.charAt(i)));
        return width;
    }

    /** Final original Lg consumer. Category Lg instances stay default10. The
     * original Le.b equipment 8-character pad/cut + '+' and blink gate are intact.
     * Corpus capacity is checked at build/test; don't silently cut another name.
     */
    public static void drawName(SN sn, String text, int x, int y, String originalRole, Lg widget) {
        if (!contains(NAMES, widget) || !hasChinese(text)) { sn.a(text, x, y, originalRole); return; }
        arp font = font(sn);
        if (width(font, text) > NAME_WIDTH)
            throw new IllegalArgumentException("item8 name exceeds original single-line 72px budget: " + text);
        if (text.length() != 0) LayoutBridge.draw(sn, text, x, y, ROLE);
    }

    /** Full amr$d source, before either original amw/NZ14 and q14/zip cut.
     * The original 112px x 2 lines, y anchor and 8px line step are unchanged.
     * No truncation: every scalar is measured; all lines checked before drawing.
     */
    public static boolean drawDescription(Lb widget, SN sn, String text) {
        if (!contains(DESCRIPTIONS, widget) || !hasChinese(text)) return false;
        arp font = font(sn);
        String[] lines = wrap(font, text, DESCRIPTION_WIDTH);
        if (lines.length > 2)
            throw new IllegalArgumentException("item8 description exceeds original two-line budget: " + text);
        for (int i = 0; i < lines.length; i++)
            if (lines[i].length() != 0) LayoutBridge.draw(sn, lines[i], widget.e_(), widget.f_() - i * LINE_STEP, ROLE);
        return true;
    }

    private static boolean hasChinese(String text) {
        for (int i = 0; i < text.length(); i++) if (text.charAt(i) >= '\u2e80' && text.charAt(i) <= '\u9fff') return true;
        return false;
    }

    /** Pixel-width wrapping, not 14-code-unit chopping. Pipes retain the game's
     * explicit line-break meaning; CRLF is one break. No mutable font scaling.
     */
    public static String[] wrap(arp font, String text, int maximum) {
        validate(font);
        if (maximum < 8) throw new IllegalArgumentException("item8 line too narrow");
        List<String> lines = new ArrayList<String>();
        StringBuilder line = new StringBuilder();
        int width = 0;
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == '|' || c == '\n' || c == '\r') {
                if (c == '\r' && i + 1 < text.length() && text.charAt(i + 1) == '\n') i++;
                lines.add(line.toString()); line.setLength(0); width = 0; continue;
            }
            int next = advance(font, c);
            if (width + next > maximum) {
                lines.add(line.toString()); line.setLength(0); width = 0;
            }
            line.append(c); width += next;
        }
        lines.add(line.toString());
        return lines.toArray(new String[lines.size()]);
    }
}
