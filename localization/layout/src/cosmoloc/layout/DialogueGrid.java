package cosmoloc.layout;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** Pixel-wrap final dialogue text, then serialize to the game's unchanged UTF-16 grid. */
public final class DialogueGrid {
    private DialogueGrid() { }

    public static final class Page {
        public final String grid;
        public final List<String> lines;
        public final double pixelWidth;
        private Page(String grid, List<String> lines, double width) {
            this.grid = grid;
            this.lines = Collections.unmodifiableList(new ArrayList<String>(lines));
            this.pixelWidth = width;
        }
    }

    /** q is the consumer's ORIGINAL cut size, not the Chinese characters-per-line cap. */
    public static List<Page> format(String finalText, PixelLayout.Metrics metrics,
                                    int q, int rows, double width) {
        if (finalText == null || metrics == null) throw new NullPointerException("dialogue input");
        if (q < 1 || rows < 1 || q > 1000 || rows > 100 || !(width > 0) || !Double.isFinite(width))
            throw new IllegalArgumentException("Invalid dialogue grid");
        // Rendering is still the original renderer; never silently strip format/control characters.
        for (int i = 0; i < finalText.length();) {
            int cp = finalText.codePointAt(i);
            int kind = Character.getType(cp);
            if ((kind == Character.CONTROL || kind == Character.FORMAT) && cp != '\n' && cp != '\r')
                throw new IllegalArgumentException("Unsupported dialogue control U+" + Integer.toHexString(cp));
            i += Character.charCount(cp);
        }
        List<Page> pages = new ArrayList<Page>();
        // Same literal paragraph delimiter as the original THREE-argument amw, not the UI '|'.
        String[] paragraphs = finalText.split("<p>");
        for (String paragraph : paragraphs) {
            PixelLayout.Profile profile = new PixelLayout.Profile("dialogue-grid", "10px-v1",
                new PixelLayout.Rect(0, 0, width, Double.MAX_VALUE), 16, PixelLayout.Insets.NONE);
            PixelLayout.Plan plan = PixelLayout.layout(paragraph, metrics, profile);
            if (plan.overflow) throw new IllegalArgumentException("Dialogue glyph cannot fit: " + plan.issues);
            List<String> lines = new ArrayList<String>();
            for (PixelLayout.Line line : plan.lines) {
                String content = paragraph.substring(line.display.start, line.display.end)
                    .replace("\r", "").replace("\n", "").replace("\u2028", "").replace("\u2029", "");
                if (content.length() > q) throw new IllegalArgumentException("Dialogue exceeds legacy UTF-16 row");
                if (line.layoutBounds.width() > width + 0.000001)
                    throw new IllegalArgumentException("Dialogue exceeds pixel row");
                lines.add(content);
            }
            if (lines.isEmpty()) lines.add("");
            for (int at = 0; at < lines.size(); at += rows) {
                List<String> selected = new ArrayList<String>();
                StringBuilder grid = new StringBuilder(q * rows);
                for (int row = 0; row < rows; row++) {
                    String content = at + row < lines.size() ? lines.get(at + row) : "";
                    selected.add(content);
                    grid.append(content);
                    for (int n = content.length(); n < q; n++) grid.append(' ');
                }
                if (grid.length() != q * rows) throw new AssertionError("Grid shape");
                pages.add(new Page(grid.toString(), selected, width));
            }
        }
        return Collections.unmodifiableList(pages);
    }

    /** Opt-in for story12's 240px rows: ASCII still advances 8px, so a legal
     * pixel row can exceed the unchanged q28 animation/draw grid. Reflow such
     * rows only at PixelLayout's existing atomic-unit boundaries, then let the
     * ORIGINAL formatter validate pixels and serialize pages. Legacy format()
     * and all radio/Continue callers retain their exact previous contract. */
    public static List<Page> formatCapped(String finalText, PixelLayout.Metrics metrics,
                                          int q, int rows, double width) {
        if (finalText == null || metrics == null) throw new NullPointerException("dialogue input");
        if (q < 1 || rows < 1 || q > 1000 || rows > 100 || !(width > 0) || !Double.isFinite(width))
            throw new IllegalArgumentException("Invalid dialogue grid");
        StringBuilder reflowed = new StringBuilder();
        boolean changed = false;
        String[] paragraphs = finalText.split("<p>", -1);
        for (int p = 0; p < paragraphs.length; p++) {
            if (p != 0) reflowed.append("<p>");
            String paragraph = paragraphs[p];
            PixelLayout.Plan plan = PixelLayout.layout(paragraph, metrics, new PixelLayout.Profile(
                "story12-utf16-cap", "12px-v1", new PixelLayout.Rect(0, 0, width, Double.MAX_VALUE),
                16, PixelLayout.Insets.NONE));
            for (int l = 0; l < plan.lines.size(); l++) {
                if (l != 0) reflowed.append('\n');
                PixelLayout.Line line = plan.lines.get(l);
                String content = plain(paragraph.substring(line.display.start, line.display.end));
                if (content.length() <= q) { reflowed.append(content); continue; }
                changed = true;
                int used = 0;
                for (PixelLayout.Unit unit : line.units) {
                    String atomic = plain(paragraph.substring(unit.display.start, unit.display.end));
                    if (atomic.length() > q) throw new IllegalArgumentException("Atomic dialogue unit exceeds legacy UTF-16 row");
                    if (used + atomic.length() > q) { reflowed.append('\n'); used = 0; }
                    reflowed.append(atomic); used += atomic.length();
                }
            }
        }
        return format(changed ? reflowed.toString() : finalText, metrics, q, rows, width);
    }
    private static String plain(String text) {
        return text.replace("\r", "").replace("\n", "").replace("\u2028", "").replace("\u2029", "");
    }

    public static boolean hasHan(String text) {
        for (int i = 0; i < text.length();) {
            int cp = text.codePointAt(i);
            if (Character.UnicodeScript.of(cp) == Character.UnicodeScript.HAN) return true;
            i += Character.charCount(cp);
        }
        return false;
    }
}
