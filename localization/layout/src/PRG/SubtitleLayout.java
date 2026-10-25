package PRG;

import cosmoloc.layout.DialogueGrid;
import cosmoloc.layout.PixelLayout;
import java.io.IOException;
import java.io.InputStream;
import java.io.Serializable;
import java.util.List;

/** Default-on final-text VSN adapter. No graphics, uppercasing, input or animation hooks. */
@SuppressWarnings({"rawtypes", "unchecked"})
public final class SubtitleLayout {
    private SubtitleLayout() { }
    public static final String FONT_SHA256 = DialogueWrap.FONT_SHA256; // Legacy ASCII pin; story12 owns its separate pin.
    public static final int LINE_WIDTH = 240; // 20 real 12px CJK cells; story12 draws at x8.
    public static final int LEGACY_LINE_WIDTH = 220; // Pure ASCII keeps its 10px role and x16.
    private static final class Font {
        static final PixelLayout.Metrics METRICS = load();
        private static PixelLayout.Metrics load() {
            try (InputStream in = SubtitleLayout.class.getResourceAsStream("/bbc2.fnt")) {
                if (in == null) throw new IOException("Missing pinned /bbc2.fnt");
                return DialogueWrap.readMetrics(in);
            } catch (IOException e) { throw new IllegalStateException("Subtitle font unavailable", e); }
        }
    }

    /** Same literal <p> syntax as three-argument amw. In particular, | is NOT markup.
     * Unlike DialogueWrap.pages, subtitle consumers do not uppercase the text. */
    public static List<DialogueGrid.Page> pages(String text, int q) {
        boolean cjk = StoryFont12.uses12(text);
        return cjk ? DialogueGrid.formatCapped(text, StoryFont12.metrics(), q, 3, LINE_WIDTH)
            : DialogueGrid.format(text, Font.METRICS, q, 3, LEGACY_LINE_WIDTH);
    }

    /** Retains the original receiver stack and the caller's original s() instruction. */
    public static aEO format(amw original, String text, amq columns, amv rows) {
        // VSN's real display profile is 28 x 3. Unknown/narrow profiles keep their
        // original formatting contract; finish still safely consumes every page.
        if (columns != Ol.MODULE$ || rows != Om.MODULE$)
            return original.a(text, columns, rows);
        List<DialogueGrid.Page> pages = pages(text, columns.a());
        aEO out = aFC.MODULE$;
        for (int i = pages.size() - 1; i >= 0; i--)
            out = new aEg(new amr.d(animationGrid(pages.get(i).grid, columns.a())), out);
        return out;
    }

    /** Original amn computes its final reveal index with String.trim().length().
     * A soft-wrapped page starting with a space would therefore hide its final
     * visible character forever. Drop leading all-blank rows and move the first
     * ink row's indentation to its trailing padding. All ink and subsequent
     * line boundaries survive; no animation algorithm is changed. */
    public static String animationGrid(String grid, int q) {
        int start = 0;
        while (start < grid.length() && grid.charAt(start) == ' ') start++;
        if (start == 0 || start == grid.length()) return grid;
        int blankRows = start / q, indent = start % q, firstEnd = (blankRows + 1) * q;
        StringBuilder out = new StringBuilder(grid.length());
        out.append(grid.substring(start, firstEnd));
        for (int i = 0; i < indent; i++) out.append(' ');
        out.append(grid.substring(firstEnd));
        for (int i = 0; i < blankRows * q; i++) out.append(' ');
        return out.toString();
    }

    public static anh finish(anh result, aEO pages, amH source) {
        return remaining(result, pages, true, source.e(), source.f());
    }
    public static anh finish(anh result, aEO pages, anp source) {
        return remaining(result, pages, false, 0, source.e());
    }
    private static anh remaining(anh state, aEO pages, boolean auto, double seconds, String style) {
        aEO rest = (aEO)pages.E();
        if (rest.b()) return state; // Preserve exact original state/list identities for one page.
        aEO pending = state.t();
        // Prepend to, NEVER replace/reorder, the original script continuation.
        // Manual pages remain manual. Auto overflow gets the SAME original delay
        // PER page (not all pages squeezed into the first deadline). Thus an
        // oversized auto caption extends the scene, without losing any text or
        // moving fade/music/tail events ahead of its last page.
        for (int i = rest.length() - 1; i >= 0; i--)
            pending = new aEg(new PageCommand(((amr.d)rest.m(i)).a(), auto, seconds, style), pending);
        return copy(state, state.s(), pending);
    }
    private static anh copy(anh state, azK active, aEO pending) {
        return state.a(state.o(), state.r(), active, pending, state.u(), state.v(),
            state.w(), state.x(), state.y(), state.p(), state.q());
    }
    /** Already-formatted continuation: bypass amw, but use the SAME original amo,
     * amn, amG, anh and script-queue consumers. Serializable with its containing state. */
    private static final class PageCommand implements amW, Serializable {
        private static final long serialVersionUID = 1L;
        private final String grid, style;
        private final boolean auto;
        private final double seconds;
        PageCommand(String grid, boolean auto, double seconds, String style) {
            this.grid = grid; this.auto = auto; this.seconds = seconds; this.style = style;
        }
        public anh a(anh state, amX metadata) {
            amn animation = amo.MODULE$.a(grid, state.e(), ams.MODULE$.c());
            azK deadline = auto ? new aAw(Double.valueOf(state.e() + seconds)) : azI.MODULE$;
            return copy(state, new aAw(new amG(animation, deadline, style)), state.t());
        }
    }
}
