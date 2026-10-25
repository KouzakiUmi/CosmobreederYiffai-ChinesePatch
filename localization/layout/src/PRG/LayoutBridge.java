package PRG;

import cosmoloc.layout.FontAccess;
import cosmoloc.layout.PixelLayout;

/** Entry-local access to the SAME BitmapFont that SN uses for rendering.
 * No reflection, global font mutation, glyph substitution or per-frame file IO.
 * Field meanings are pinned to the original 1.0.5_full arp/arp$a/arp$b bytecode.
 */
public final class LayoutBridge {
    private LayoutBridge() {}

    public static arp font(SN sn, String role) {
        if (!(sn instanceof FontAccess))
            throw new IllegalStateException("layout renderer has no font bridge");
        Object value = ((FontAccess) sn).cosmo$layoutFont(role);
        if (!(value instanceof arp))
            throw new IllegalStateException("layout role has no BitmapFont: " + role);
        arp font = (arp) value;
        validate(font.a);
        return font;
    }

    private static void validate(arp.a data) {
        if (data.q)
            throw new IllegalStateException("layout does not reinterpret font markup");
        // The target arq cache rounds each quad independently in integer mode.
        // Fractional scaling is not equivalent to rounding a final measured line.
        // Current profiles deliberately support only the proven 1:1 pixel grid.
        if (data.o != 1.0f || data.p != 1.0f
                || data.k != Math.round(data.k) || data.h != Math.round(data.h))
            throw new IllegalStateException("layout requires the unscaled integral font grid");
    }

    public static PixelLayout.Metrics metrics(arp font) {
        validate(font.a);
        return new EngineMetrics(font.a);
    }

    /** x/y are logical pen origins (y is the original SN coordinate).
     * arr cancels the first glyph xoffset and subtracts padLeft. Restore those
     * here so its whole-line positions match the plan's ordinary pen model.
     * y is unchanged: metrics() expresses the actual arq quads top-down.
     */
    public static void draw(SN sn, String text, int x, int y, String role) {
        if (text.length() == 0) return;
        arp font = font(sn, role);
        requireRenderableLine(font.a, text);
        arp.b first = font.a.a(text.charAt(0));
        if (first == null)
            throw new IllegalStateException("layout missing first glyph");
        if (text.indexOf('\n') >= 0 || text.indexOf('\r') >= 0)
            throw new IllegalArgumentException("draw accepts one planned line");
        float correction = first.n ? 0 : first.j * font.a.o + font.a.h;
        if (correction != Math.round(correction))
            throw new IllegalStateException("non-integral renderer correction needs a float backend");
        sn.a(text, Math.addExact(x, Math.round(correction)), y, role);
    }

    /** The core can preserve non-drawing Unicode units, but this legacy backend
     * would replace missing interior controls with its missingGlyph. Reject that
     * unsupported domain rather than measure AB and accidentally render A?B.
     */
    static void requireRenderableLine(arp.a data, String text) {
        for (int i = 0; i < text.length(); i++) {
            char value = text.charAt(i);
            int type = Character.getType(value);
            if (Character.isSurrogate(value) || type == Character.CONTROL
                    || type == Character.FORMAT || (value >= 0xFE00 && value <= 0xFE0F)
                    || data.a(value) == null)
                throw new IllegalArgumentException("legacy layout backend cannot render code unit U+"
                        + Integer.toHexString(value));
        }
    }

    public static final class EngineMetrics implements PixelLayout.Metrics {
        private final arp.a data;
        EngineMetrics(arp.a data) { validate(data); this.data = data; }
        @Override public PixelLayout.Glyph glyph(int codePoint) {
            if (codePoint < 0 || codePoint > Character.MAX_VALUE
                    || Character.isSurrogate((char) codePoint)) return null;
            arp.b glyph = data.a((char) codePoint);
            if (glyph == null) return null;
            // arq: bottom = raw SN y + data.ascent + glyph.yoffset * scaleY;
            // convert the quad top to the layout engine's downward y axis.
            return new PixelLayout.Glyph(glyph.l * data.o, glyph.j * data.o,
                    -(data.k + (glyph.k + glyph.e) * data.p),
                    glyph.d * data.o, glyph.e * data.p);
        }
        @Override public double kerning(int left, int right) {
            if (left < 0 || left > Character.MAX_VALUE || right < 0
                    || right > Character.MAX_VALUE) return 0;
            arp.b glyph = data.a((char) left);
            return glyph == null ? 0 : glyph.a((char) right) * data.o;
        }
    }
}
