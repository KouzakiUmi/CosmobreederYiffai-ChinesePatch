package PRG;

import cosmoloc.layout.PixelLayout;
import java.lang.ref.WeakReference;
import java.util.ArrayList;
import java.util.List;

/** ClassicPreTitle candidate adapter. No profile is enabled by default.
 * Runtime code is Java 8; ASM exists only in the build-time transformer.
 */
public final class VsnLayout {
    private VsnLayout() { }
    public static final String STATUS = "CANDIDATE_NOT_ACCEPTED_UNVERIFIED_RECT";
    private static final int LIMIT = 64;
    private static final String[] TEXT = {
        "这是超光速航行与先进赛博机器人技术的时代。",
        "[3P组织]已成为推动太空探索的一股重要力量。",
        "[3P组织]派出英勇之士，前往各地收集情报。",
        "这些被称为[宇宙育种者]的英雄，让文明得以繁荣。",
        "穿行群星，探寻未知，这就是冒险的人生。",
        "人人敬仰，许多孩子梦想长大后成为[宇宙育种者]。",
        "然而，离开安稳的家园、踏上星际旅途，绝非胆小者所能为。",
        "毕竟，谁又能说清遥远的未知星球上潜藏着什么危险……"
    };
    public static final String SOURCE_SHA256 = "c360b7bc0610fa400f6d1153853dd21d1e5751ad74bbd379638b313ec943c5d4";
    public static final String NON_TARGET_SOURCE_SHA256 = "93f5c0dd1ffc4e76059f3d9e0d6eee36b28ea8ec11106b6343c76a9336ddaa33";
    private static final int[] OFFSETS = {86, 120, 220, 255, 356, 389, 520, 571};
    private static final int[] ENGLISH_OFFSETS = {86, 169, 317, 403, 552, 644, 829, 936};
    private static final String[] ENGLISH = {
        "It is the age of faster than light travel and advanced cyber-robotics.",
        "[THE 3P ORGANIZATION] has become a driving force for space exploration.",
        "Brave heroes are sent out by [THE 3P ORGANIZATION] to gather information.",
        "These [COSMOBREEDERS], as they are known, allow civilization to prosper.",
        "Traveling through the stars and making new discoveries is a life of adventure.",
        "Respected by all, many a child dreams of growing up to become a [COSMOBREEDER]",
        "Space travel and leaving the safety of home is not for the faint of heart, however.",
        "For who can truly say what dangers await on distant, unknown planets..."
    };
    private static final List<Capture> CAPTURES = new ArrayList<Capture>();
    private static final List<Context> CONTEXTS = new ArrayList<Context>();
    private static final List<Prototype> PROTOTYPES = new ArrayList<Prototype>();

    /** Called only at the locked amH constructor-consumer site, after amn exists. */
    public static synchronized void capture(amH command, String full, amn animated) {
        prune();
        if (command == null || full == null || animated == null) return;
        if (find(animated) != null) throw new IllegalStateException("duplicate VSN capture");
        if (CAPTURES.size() == LIMIT) CAPTURES.remove(0);
        CAPTURES.add(new Capture(command, full, animated));
    }

    /** Called only by the locked receiver-based amn copier. The returned object
     * is always the original child: no animation parameter or timing is changed.
     * Provenance follows the exact parent reference, never an equal-text lookup.
     * Existing child provenance (including a different event) is never replaced.
     */
    public static synchronized amn inherit(amn parent, amn child) {
        prune();
        if (parent == null || child == null || parent == child || find(child) != null) return child;
        Capture original = find(parent);
        if (original == null || !parent.a().equals(child.a())) return child;
        amH command = original.command.get();
        if (command == null) return child;
        if (CAPTURES.size() == LIMIT) CAPTURES.remove(0);
        CAPTURES.add(new Capture(command, original.full, child));
        return child;
    }

    /** Called at jl's render-composition entry; compares references, never Scala equals. */
    public static synchronized void observe(anh state, amU source) {
        prune();
        for (int i = CONTEXTS.size() - 1; i >= 0; i--)
            if (CONTEXTS.get(i).state.get() == state) CONTEXTS.remove(i);
        if (state == null || source == null) return;
        if (CONTEXTS.size() == LIMIT) CONTEXTS.remove(0);
        CONTEXTS.add(new Context(state, source));
        if ("ClassicPreTitle".equals(source.a()) && prototype(source) == null
            && "true".equals(System.getProperty("cosmo.layout.vsn.prototype"))) {
            // No inferred container: explicit complete coordinates are mandatory.
            PixelLayout.Rect rect = new PixelLayout.Rect(property("x"), property("y"),
                property("width"), property("height"));
            PixelLayout.Insets effects = new PixelLayout.Insets(property("effectLeft"),
                property("effectTop"), property("effectRight"), property("effectBottom"));
            enablePrototype(source, new PixelLayout.Profile("ClassicPreTitle",
                "explicit-unverified-prototype", rect, property("lineStep"), effects),
                "explicit system properties; NOT clip/scene verified");
        }
    }
    private static double property(String name) {
        String key = "cosmo.layout.vsn." + name;
        String value = System.getProperty(key);
        if (value == null || value.trim().isEmpty())
            throw new IllegalStateException("VSN prototype requires -D" + key + "=<logical pixels>");
        try { return Double.parseDouble(value); }
        catch (NumberFormatException invalid) { throw new IllegalStateException("invalid " + key, invalid); }
    }

    /** Explicit OFFLINE/EXPERIMENTAL activation, bound to this exact parsed source.
     * This is not a verified/release activation API. Caller supplies relative,
     * top-down logical pixels and a provenance label; no size is guessed here.
     * Old hint placement and all tail logic remain unchanged, hence hint/clip
     * and timing require scene validation before any release.
     */
    public static synchronized void enablePrototype(amU source, PixelLayout.Profile profile,
                                                     String evidenceLabel) {
        if (source == null || !"ClassicPreTitle".equals(source.a()) || profile == null
            || evidenceLabel == null || evidenceLabel.trim().isEmpty()
            || profile.content.width <= 0 || profile.content.height <= 0)
            throw new IllegalArgumentException("explicit ClassicPreTitle profile/provenance required");
        disablePrototype(source);
        if (PROTOTYPES.size() == LIMIT) PROTOTYPES.remove(0);
        PROTOTYPES.add(new Prototype(source, profile, evidenceLabel));
    }

    public static synchronized void disablePrototype(amU source) {
        for (int i = PROTOTYPES.size() - 1; i >= 0; i--)
            if (PROTOTYPES.get(i).source.get() == source) PROTOTYPES.remove(i);
    }

    public static synchronized String status(amn animated) {
        Capture c = find(animated);
        return c == null ? "UNBOUND_ANIMATION" : c.status;
    }

    /** True bypasses the WHOLE old character-chunk loop, not the callback tail. */
    public static synchronized boolean draw(anh state, SN sn, String speaker, boolean fox,
                                             amn animated, int reveal, String masked,
                                             int anchorX, int anchorY) {
        // Exact original boolean: (Fox && !fox) || HardFox uses dingbats.
        if (("Fox".equals(speaker) && !fox) || "HardFox".equals(speaker)) return false;
        amU source = null;
        for (Context context : CONTEXTS)
            if (context.state.get() == state) source = context.source.get();
        if (source == null || !"ClassicPreTitle".equals(source.a())) return false;
        Capture c = find(animated);
        if (c == null) {
            // Original skip/input code can copy an amn. Never infer a new
            // instance binding from equal text, nor silently use old Chinese
            // chunks under an explicitly activated target profile.
            if (prototype(source) != null && frozenChineseSource(source))
                throw new IllegalStateException("VSN prototype rejected: UNBOUND_ANIMATION_INSTANCE");
            return false;
        }
        int ordinal = -1, autoCount = 0, occurrences = 0;
        aEO<amW> commands = source.l();
        for (int i = 0; i < commands.length(); i++) {
            amW command = commands.m(i);
            if (command == c.command.get()) { ordinal = autoCount; occurrences++; }
            if (command instanceof amH) autoCount++;
        }
        if (occurrences != 1 || autoCount != TEXT.length || ordinal < 0 || ordinal >= TEXT.length)
            return reject(c, "UNBOUND_COMMAND_IDENTITY", source);
        amH command = c.command.get();
        String key = command.a().e();
        if (ENGLISH[ordinal].equals(c.full)
            && ("vsn.ClassicPreTitle." + ENGLISH_OFFSETS[ordinal]).equals(key)) {
            c.status = "KNOWN_R21_SFW_ENGLISH_NON_TARGET";
            return false;
        }
        if (!("vsn.ClassicPreTitle." + OFFSETS[ordinal]).equals(key)
            || command.e() != 8.0 || !"default".equals(command.f())
            || !TEXT[ordinal].equals(c.full) || !expectedAnimated(ordinal).equals(animated.a()))
            return reject(c, "SOURCE_BINDING_MISMATCH", source);
        if (reveal < 0 || reveal > animated.a().length()
            || !amw.MODULE$.a(animated.a(), reveal).equals(masked))
            return reject(c, "REVEAL_MASK_MISMATCH", source);
        Prototype prototype = prototype(source);
        if (prototype == null) return reject(c, "BLOCKED_UNVERIFIED_RECT", source);
        String role = sn.b();
        if ("dingbats".equals(role)) return false;
        arp font = LayoutBridge.font(sn, role);
        if (font == null) return reject(c, "MISSING_ACTUAL_FONT", source);
        PixelLayout.Metrics metrics = LayoutBridge.metrics(font);
        long signature = signature(c.full, metrics);
        if (c.plan == null || c.font.get() != font || c.prototype != prototype
            || c.metricSignature != signature) {
            c.plan = PixelLayout.layout(c.full, metrics, prototype.profile, sourceMap(ordinal));
            c.font = new WeakReference<arp>(font);
            c.metricSignature = signature;
            c.prototype = prototype;
        }
        if (c.plan.overflow || !c.plan.issues.isEmpty())
            return reject(c, "LAYOUT_OVERFLOW_OR_UNSUPPORTED_BREAK", source);
        for (PixelLayout.VisiblePrefix prefix : c.plan.visiblePrefixes(reveal)) {
            if (prefix.displayEnd <= prefix.line.display.start) continue;
            String text = c.full.substring(prefix.line.display.start, prefix.displayEnd);
            LayoutBridge.draw(sn, text, integer(anchorX + prefix.line.originX),
                integer(anchorY - prefix.line.originY), role);
        }
        c.status = "PROTOTYPE_DRAWN_NOT_ACCEPTED";
        return true;
    }

    /** Frozen r21 parser -> amH -> amw(Ol=28,Om=3) traces, not a whitespace
     * heuristic. All eight actual Chinese inputs are <=28 BMP code units;
     * their animations are the unchanged text plus generated tail padding.
     * The source L20 trailing space is consumed by the REAL r21 parser, not us.
     */
    public static String expectedAnimated(int ordinal) {
        String text = TEXT[ordinal];
        String value = text;
        StringBuilder out = new StringBuilder(value);
        while (out.length() < 84) out.append(' ');
        return out.toString();
    }

    public static List<PixelLayout.SourceRange> sourceMap(int ordinal) {
        List<PixelLayout.SourceRange> ranges = new ArrayList<PixelLayout.SourceRange>();
        for (int i = 0; i < TEXT[ordinal].length(); i++) {
            int original = i;
            ranges.add(new PixelLayout.SourceRange(i, i + 1, original, original + 1));
        }
        return ranges;
    }

    private static boolean frozenChineseSource(amU source) {
        int ordinal = 0;
        aEO<amW> commands = source.l();
        for (int i = 0; i < commands.length(); i++) {
            if (!(commands.m(i) instanceof amH)) continue;
            if (ordinal >= TEXT.length) return false;
            amH command = (amH)commands.m(i);
            if (!("vsn.ClassicPreTitle." + OFFSETS[ordinal]).equals(command.a().e())
                || !TEXT[ordinal].equals(command.a().a())) return false;
            ordinal++;
        }
        return ordinal == TEXT.length;
    }

    private static long signature(String text, PixelLayout.Metrics m) {
        long h = 1;
        for (int i = 0; i < text.length(); i++) {
            int cp = text.charAt(i);
            PixelLayout.Glyph g = m.glyph(cp);
            if (g == null) throw new IllegalStateException("missing VSN glyph " + cp);
            h = hash(h, g.xAdvance); h = hash(h, g.xOffset); h = hash(h, g.yOffset);
            h = hash(h, g.width); h = hash(h, g.height);
            if (i > 0) h = hash(h, m.kerning(text.charAt(i - 1), cp));
        }
        return h;
    }
    private static long hash(long h, double value) { return 31 * h + Double.doubleToLongBits(value); }
    private static int integer(double value) {
        if (value != Math.rint(value) || value < Integer.MIN_VALUE || value > Integer.MAX_VALUE)
            throw new IllegalStateException("non-integral SN layout origin: " + value);
        return (int) value;
    }
    private static boolean reject(Capture c, String status, amU source) {
        Prototype enabled = prototype(source);
        if (!status.equals(c.status)) {
            c.status = status;
            System.err.println("[vsn-layout] " + STATUS + ": " + status);
        }
        // Diagnostic-only fallback is visible in status; activated prototypes fail closed.
        if (enabled != null) throw new IllegalStateException("VSN prototype rejected: " + status);
        return false;
    }
    private static Prototype prototype(amU source) {
        for (Prototype p : PROTOTYPES) if (p.source.get() == source) return p;
        return null;
    }
    private static Capture find(amn animated) {
        for (Capture c : CAPTURES) if (c.animated.get() == animated) return c;
        return null;
    }
    private static void prune() {
        for (int i = CAPTURES.size() - 1; i >= 0; i--)
            if (CAPTURES.get(i).animated.get() == null || CAPTURES.get(i).command.get() == null)
                CAPTURES.remove(i);
        for (int i = CONTEXTS.size() - 1; i >= 0; i--)
            if (CONTEXTS.get(i).state.get() == null || CONTEXTS.get(i).source.get() == null)
                CONTEXTS.remove(i);
        for (int i = PROTOTYPES.size() - 1; i >= 0; i--)
            if (PROTOTYPES.get(i).source.get() == null) PROTOTYPES.remove(i);
    }
    private static final class Capture {
        final WeakReference<amH> command;
        final WeakReference<amn> animated;
        final String full;
        String status = "CAPTURED_UNBOUND_SOURCE";
        WeakReference<arp> font = new WeakReference<arp>(null);
        long metricSignature;
        Prototype prototype;
        PixelLayout.Plan plan;
        Capture(amH command, String full, amn animated) {
            this.command = new WeakReference<amH>(command);
            this.animated = new WeakReference<amn>(animated); this.full = full;
        }
    }
    private static final class Context {
        final WeakReference<anh> state;
        final WeakReference<amU> source;
        Context(anh state, amU source) {
            this.state = new WeakReference<anh>(state); this.source = new WeakReference<amU>(source);
        }
    }
    private static final class Prototype {
        final WeakReference<amU> source;
        final PixelLayout.Profile profile;
        final String provenance;
        Prototype(amU source, PixelLayout.Profile profile, String provenance) {
            this.source = new WeakReference<amU>(source); this.profile = profile; this.provenance = provenance;
        }
    }
}
