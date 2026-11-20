package PRG;

/** Kr's fixed 32-column/8-pixel ending UI only. Not VSN or a global Id hook. */
public final class EndingReportLayout {
    private EndingReportLayout() { }
    public static final String FONT_ROLE = "classic";
    public static final String FONT_SHA256 = "a456bb96b944b2c443868b5ea02d2b458744eb795e161d6835a2d490a67c2510";

    /** Caller has already resolved the original grid coordinates and blink colour.
     * Ks has already replaced its leading *! control marker with two spaces.
     * Do not trim, uppercase, wrap, clip, truncate or otherwise rewrite this text. */
    public static void draw(Id original, SN target, String text, int x, int y, aBa<Object,Object,Object,Object> colour) {
        if (!hasHan(text)) {
            original.a(target, text, x, y, colour);
            return;
        }
        target.a(text, x, y, colour, FONT_ROLE);
    }

    /** The data book has exactly three fixed 28-column rows. Its old four-argument
     * formatter only pads to two rows and silently loses excess source in consumers.
     * Preserve explicit | lines and $ line style; never return an overlong block. */
    public static String formatData(amw original, String text, amq columns, amv minimumRows, boolean normalize) {
        if (columns != Ol.MODULE$ || minimumRows != Oa.MODULE$ || normalize)
            return original.a(text, columns, minimumRows, normalize);
        // English goes through the same source-conserving path: the original
        // formatter's second wrapping pass lost two actual SFW closing ']'.
        return SceneText.fixedGrid(text, 28, 3, true);
    }

    public static void drawData(SN target, String text, int x, int y, String originalRole) {
        target.a(text, x, y, hasHan(text) ? FONT_ROLE : originalRole);
    }
    public static void drawData(SN target, String text, int x, int y, aBa<Object,Object,Object,Object> colour, String originalRole) {
        target.a(text, x, y, colour, hasHan(text) ? FONT_ROLE : originalRole);
    }

    private static boolean hasHan(String text) {
        for (int at = 0; at < text.length();) {
            int cp = text.codePointAt(at);
            if (Character.UnicodeScript.of(cp) == Character.UnicodeScript.HAN) return true;
            at += Character.charCount(cp);
        }
        return false;
    }
}
