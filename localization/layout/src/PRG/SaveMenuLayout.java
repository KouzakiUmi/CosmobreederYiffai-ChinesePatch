package PRG;

import cosmoloc.layout.PixelLayout;

/** Save-menu-only, single-card candidate. G3 clip/CRT verification is mandatory. */
public final class SaveMenuLayout {
    public static final String PROFILE = "save-single-card-10px-v1-candidate";
    public static final int X = 24, TOP = 174, STEP = 14, WIDTH = 224;
    public static final int PANEL_X = 6, PANEL_Y = 104, PANEL_W = 244, PANEL_H = 77;
    private static volatile boolean prototypeEnabled = Boolean.getBoolean("cosmo.layout.save.prototype");
    private static final ThreadLocal<Object[]> CONTEXT = new ThreadLocal<Object[]>();
    private SaveMenuLayout() { }

    /** Explicit diagnostic opt-in only; never an implicit release adaptation. */
    public static void configurePrototype() { validateGeometry(); prototypeEnabled = true; }
    public static void disablePrototype() { prototypeEnabled = false; CONTEXT.remove(); }
    public static boolean prototypeEnabled() { return prototypeEnabled; }

    /** Called AFTER the original background draw, never from the name-entry scene. */
    public static void begin(Mf parent, SN sn) {
        if (!prototypeEnabled) return;
        validateGeometry();
        if (CONTEXT.get() != null) throw new IllegalStateException("Nested save layout context");
        aEO<?> slots = parent.s();
        int chosen = -1;
        if (parent.m() instanceof LV) chosen = ((LV) parent.m()).a();
        Object selected = option(parent.e().a());
        if (chosen < 0) chosen = slotId(selected);
        // Action buttons have no slot identity: show the lowest original slot ID.
        if (chosen < 0) {
            for (int i = 0; i < slots.e(); i++) {
                int id = slotId(slots.m(i));
                if (id >= 0 && (chosen < 0 || id < chosen)) chosen = id;
            }
        }
        CONTEXT.set(new Object[] {parent, Integer.valueOf(chosen), Integer.valueOf(slots.e())});
        // Candidate interior only: does not expand or replace the background asset.
        // Covers obsolete vertical column lines; bounds are NOT asserted to be a runtime clip.
        sn.a("BlackFill", PANEL_X, PANEL_Y, PANEL_W, PANEL_H);
    }

    public static void end() { CONTEXT.remove(); }

    private static Object option(azK<?> value) {
        return value instanceof aAw ? ((aAw) value).e() : null;
    }

    public static int slotId(Object slot) {
        if (slot instanceof LY) return ((LY) slot).j().a();
        if (slot instanceof LX) return ((LX) slot).j();
        return -1;
    }

    private static boolean active() { return CONTEXT.get() != null; }
    private static boolean shown(Object slot) {
        return slotId(slot) == ((Integer) CONTEXT.get()[1]).intValue();
    }

    /** Pure extraction: retain original numeric/area transformations and full raw name. */
    public static String[] fields(String rawName, String first, String second) {
        if (rawName == null || first == null || second == null || first.length() < 8
                || second.length() < 15 || !first.substring(8).startsWith("  LVL")
                || !second.startsWith("          "))
            throw new IllegalArgumentException("Save field format identity mismatch");
        int cut = first.lastIndexOf(' ');
        if (cut < 8 || first.length() - cut - 1 != 4 || second.charAt(second.length() - 5) != ' ')
            throw new IllegalArgumentException("Save hexadecimal field mismatch");
        String hex = first.substring(cut + 1) + second.substring(second.length() - 4);
        if (!hex.matches("[0-9A-F]{8}")) throw new IllegalArgumentException("Save hex encoding mismatch");
        String metadata = first.substring(8, cut).trim();
        String area = second.substring(10, second.length() - 5);
        String prefix = rawName.substring(0, Math.min(8, rawName.length()));
        while (prefix.length() < 8) prefix += " ";
        if (!first.startsWith(prefix) || !metadata.matches("LVL[0-9]{3,} TRY[0-9]{3,}")
                || !area.matches("(?s).+ [0-9]{3,}%"))
            throw new IllegalArgumentException("Save metadata/name format mismatch");
        return new String[] {rawName, metadata, area, hex};
    }

    /** Overflow is explicit; never silently clip/truncate/shrink an unread field. */
    public static PixelLayout.Plan planField(String text, PixelLayout.Metrics metrics, int width) {
        PixelLayout.Plan plan = PixelLayout.layout(text, metrics,
            new PixelLayout.Profile(PROFILE, "1", new PixelLayout.Rect(0, 0, width, STEP),
                STEP, PixelLayout.Insets.NONE));
        if (plan.overflow || plan.lines.size() != 1)
            throw new IllegalStateException("Save candidate field overflow: " + text);
        PixelLayout.Line line = plan.lines.get(0);
        if (line.originX != Math.rint(line.originX) || line.originY != Math.rint(line.originY))
            throw new IllegalStateException("Save candidate needs an integral SN pen origin");
        return plan;
    }
    public static void requireSingleLine(String text, PixelLayout.Metrics metrics, int width) {
        planField(text, metrics, width);
    }

    /** Static candidate panel assertions, not evidence of the actual parent clip. */
    public static void requireCandidateRect(double x, double y, double width, double height) {
        if (!Double.isFinite(x) || !Double.isFinite(y) || !Double.isFinite(width)
                || !Double.isFinite(height) || width < 0 || height < 0
                || x < PANEL_X || y < PANEL_Y || x + width > PANEL_X + PANEL_W
                || y + height > PANEL_Y + PANEL_H)
            throw new IllegalStateException("Save candidate rectangle escapes registered panel");
    }
    public static void validateGeometry() {
        requireCandidateRect(X, TOP - STEP, 84, STEP); // complete name field
        requireCandidateRect(X + 88, TOP - 6, 8, 8); // RN image
        requireCandidateRect(216, TOP - STEP, 32, STEP); // slot indicator
        for (int row = 1; row <= 3; row++)
            requireCandidateRect(X, TOP - row * STEP - STEP, WIDTH, STEP);
        for (int i = 0; i < 8; i++)
            requireCandidateRect(X + 8 * i, TOP - 3 * STEP - 8, 8, 8);
        requireCandidateRect(X - 7, TOP - 6, 5, 7); // selected-slot cursor
    }
    private static void line(SN sn, String text, int x, int y, int width) {
        String font = sn.b();
        PixelLayout.Plan plan = planField(text, LayoutBridge.metrics(LayoutBridge.font(sn, font)), width);
        PixelLayout.Bounds bounds = plan.effectBounds;
        if (!bounds.empty) requireCandidateRect(x + bounds.left, y - bounds.bottom,
                bounds.width(), bounds.height());
        PixelLayout.Line line = plan.lines.get(0);
        LayoutBridge.draw(sn, text, x + (int) line.originX, y - (int) line.originY, font);
    }

    private static void number(SN sn, int slot) {
        int count = ((Integer) CONTEXT.get()[2]).intValue();
        line(sn, Integer.toString(slot + 1) + "/" + count, 216, TOP, 32);
    }

    /** Return true when handled, including deliberately nonvisible original slots. */
    public static boolean full(LY slot, SN sn) {
        if (!active()) return false;
        if (!shown(slot)) return true;
        // Preserve the exact deletion-confirm blink gate used by LY.b before drawing.
        Object deletingParent = option(slot.k());
        if (deletingParent instanceof Mf) {
            Mf p = (Mf) deletingParent;
            if (p.m() instanceof LV && ((LV) p.m()).a() == slotId(slot)
                    && Id.MODULE$.a((double) p.e().f(), 5.0)) return true;
        }
        aAJ<?, ?> rows = slot.m();
        String[] f = fields(slot.l().e(), (String) rows.a(), (String) rows.e());
        line(sn, f[0], X, TOP, 84);
        Id.MODULE$.a(sn, slot.j().e().f(), X + 88, TOP);
        number(sn, slotId(slot));
        line(sn, f[1] + " " + f[3], X, TOP - STEP, WIDTH);
        line(sn, f[2], X, TOP - 2 * STEP, WIDTH);
        aEO<?> symbols = slot.n();
        if (symbols.e() != 8) throw new IllegalStateException("Save symbol count mismatch");
        for (int i = 0; i < symbols.e(); i++) {
            aAJ<?, ?> symbol = (aAJ<?, ?>) symbols.m(i);
            if (symbol.m()) sn.a("ClassicHUDZenerSymbols" + (String) symbol.a(),
                    X + 8 * i, TOP - 3 * STEP - 8);
        }
        return true;
    }

    public static boolean empty(LX slot, SN sn) {
        if (!active()) return false;
        if (!shown(slot)) return true;
        line(sn, "[无数据]", X, TOP, 152);
        number(sn, slotId(slot));
        return true;
    }

    /** The original action-button cursor and every unrelated Iu remain unchanged. */
    public static boolean cursor(Iu selector, SN sn, ZH target, float time) {
        if (!active() || selector.l() != CONTEXT.get()[0] || slotId(target) < 0) return false;
        if (shown(target) && (selector.g() || Id.MODULE$.a((double) time, 5.0)))
            sn.a("WhiteFill", X - 7, TOP - 6, 5, 7);
        return true;
    }
}
