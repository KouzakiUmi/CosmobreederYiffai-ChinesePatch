package PRG;

import cosmoloc.layout.PixelLayout;

/** Headless tests against the target game's actual font data/glyph classes. */
public final class FontBridgeTest {
    private static void eq(double expected, double actual) {
        if (Math.abs(expected - actual) > 0.00001)
            throw new AssertionError(expected + " != " + actual);
    }
    public static void main(String[] args) {
        arp.a data = new arp.a();
        data.o = 1; data.p = 1; data.k = 2; data.m = -14;
        arp.b glyph = new arp.b();
        glyph.a = '\u4e2d'; glyph.d = 10; glyph.e = 10;
        glyph.j = -1; glyph.k = -10; glyph.l = 10;
        glyph.a('\u6587', -1);
        data.a('\u4e2d', glyph);
        arp.b second = new arp.b();
        second.a = '\u6587'; second.d = 10; second.e = 10;
        second.j = 0; second.k = -10; second.l = 10;
        data.a('\u6587', second);
        LayoutBridge.EngineMetrics metrics = new LayoutBridge.EngineMetrics(data);
        PixelLayout.Glyph measured = metrics.glyph('\u4e2d');
        eq(10, measured.xAdvance); eq(-1, measured.xOffset);
        eq(-2, measured.yOffset); eq(10, measured.width); eq(10, measured.height);
        eq(-1, metrics.kerning('\u4e2d', '\u6587'));
        if (metrics.glyph(0x1F600) != null || metrics.glyph(0xD800) != null)
            throw new AssertionError("BMP backend must not fake unsupported glyphs");
        PixelLayout.Plan plan = PixelLayout.layout("\u4e2d\u6587", metrics,
                new PixelLayout.Profile(new PixelLayout.Rect(0, 0, 30, 20),
                        14, PixelLayout.Insets.NONE));
        if (plan.overflow) throw new AssertionError("fixture should fit");
        PixelLayout.Line line = plan.lines.get(0);
        // Reproduce original arr first advance and arq quad placement, including
        // the bridge's compensation, not an assumed 8/10px character grid.
        double correction = glyph.j * data.o + data.h;
        double firstAdvance = -glyph.j * data.o - data.h;
        eq(line.glyphs.get(0).inkBounds.left,
                line.originX + correction + firstAdvance + glyph.j * data.o);
        eq(line.glyphs.get(1).inkBounds.left,
                line.originX + correction + firstAdvance
                        + glyph.l * data.o + glyph.a('\u6587') * data.o + second.j * data.o);
        eq(line.glyphs.get(0).inkBounds.top,
                line.originY - (data.k + (glyph.k + glyph.e) * data.p));
        LayoutBridge.requireRenderableLine(data, "\u4e2d\u6587");
        String[] unsupported = {"\u4e2d\u200d\u6587", "\u4e2d\u200c\u6587", "\u4e2d\u0009\u6587", "\u4e2d\ufe0f\u6587", "\u4e2d?\u6587"};
        for (String text : unsupported) {
            boolean rejected = false;
            try { LayoutBridge.requireRenderableLine(data, text); }
            catch (IllegalArgumentException expected) { rejected = true; }
            if (!rejected) throw new AssertionError("core/backend non-drawing domain mismatch");
        }
        arp.a padded = new arp.a();
        padded.o = 1; padded.p = 1; padded.k = 0; padded.h = 3; padded.f = 4;
        arp.b a = new arp.b();
        a.a = 'A'; a.j = -2; a.d = 10; a.e = 10; a.k = -10; a.l = 8; a.a('B', -1);
        arp.b b = new arp.b();
        b.a = 'B'; b.j = 1; b.d = 11; b.e = 10; b.k = -10; b.l = 20;
        padded.a('A', a); padded.a('B', b);
        PixelLayout.Metrics paddedMetrics = new LayoutBridge.EngineMetrics(padded);
        PixelLayout.Plan paddedPlan = PixelLayout.layout("AB", paddedMetrics,
                new PixelLayout.Profile(new PixelLayout.Rect(0, 0, 21, 14), 14, PixelLayout.Insets.NONE));
        if (paddedPlan.overflow || paddedPlan.lines.size() != 1) throw new AssertionError("21px actual quad union fits");
        eq(0, paddedPlan.lines.get(0).glyphs.get(0).inkBounds.left);
        eq(10, paddedPlan.lines.get(0).glyphs.get(1).inkBounds.left);
        eq(21, paddedPlan.lines.get(0).glyphs.get(1).inkBounds.right);
        PixelLayout.Plan tooNarrow = PixelLayout.layout("AB", paddedMetrics,
                new PixelLayout.Profile(new PixelLayout.Rect(0, 0, 20, 28), 14, PixelLayout.Insets.NONE));
        if (tooNarrow.lines.size() != 2) throw new AssertionError("padRight is not unused quad capacity");
        data.o = 0.5f;
        boolean refused = false;
        try { new LayoutBridge.EngineMetrics(data); }
        catch (IllegalStateException expected) { refused = true; }
        if (!refused) throw new AssertionError("fractional scale can round a 9px plan into a 10px quad union");
        data.o = 1;
        data.k = 0.5f;
        refused = false;
        try { new LayoutBridge.EngineMetrics(data); }
        catch (IllegalStateException expected) { refused = true; }
        if (!refused) throw new AssertionError("fractional ascent must not bypass quad rounding gate");
        System.out.println("FontBridgeTest: actual font fields, quad formula and integer-grid gate PASS");
    }
}
