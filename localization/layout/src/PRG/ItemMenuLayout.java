package PRG;

import cosmoloc.layout.PixelLayout;
import java.lang.ref.WeakReference;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

/** Main Le item menu only. Unknown parent clip is deliberately NOT a profile.
 * No input hooks, new paging keys, timer, file IO, or global font mutation.
 */
public final class ItemMenuLayout {
    public static final String PROFILE = "item-menu-explicit-prototype-v1";
    public static final int MAX_ENTRIES = 64;
    private static final List<Entry> ENTRIES = new ArrayList<Entry>();
    private static volatile Configuration configuration = new Configuration(false, null, null);
    private static volatile Diagnostic lastName, lastDescription;
    private static boolean configured;
    public static final String PROPERTY = "cosmo.layout.item.prototype";
    private ItemMenuLayout() { }

    /** Profiles are local to each original SN anchor, top-down: SN y = anchorY - originY.
     * Rectangles are caller-supplied prototypes, NOT measured clips or shipping defaults.
     */
    public static synchronized void configurePrototype(PixelLayout.Profile name, PixelLayout.Profile description) {
        validate(name); validate(description);
        configuration = new Configuration(true, name, description);
        configured = true;
    }

    /** Explicit launch opt-in; every local rectangle coordinate/dimension is mandatory.
     * -Dcosmo.layout.item.prototype=true
     * -Dcosmo.layout.item.{name,description}.{x,y,width,height,step}=number
     * No property is inferred from the 256x192 background or the icon grid.
     */
    public static synchronized void configureFromProperties() {
        String value = System.getProperty(PROPERTY, "false");
        if ("false".equals(value)) { configureDiagnostic(null, null); return; }
        if (!"true".equals(value)) throw new IllegalArgumentException("Invalid " + PROPERTY);
        PixelLayout.Profile name = propertyProfile("name");
        PixelLayout.Profile description = propertyProfile("description");
        configurePrototype(name, description);
    }

    private static PixelLayout.Profile propertyProfile(String field) {
        String prefix = "cosmo.layout.item." + field + ".";
        return new PixelLayout.Profile(PROFILE + "-" + field, "1",
                new PixelLayout.Rect(property(prefix + "x"), property(prefix + "y"),
                        property(prefix + "width"), property(prefix + "height")),
                property(prefix + "step"), PixelLayout.Insets.NONE);
    }
    private static double property(String key) {
        String value = System.getProperty(key);
        if (value == null) throw new IllegalStateException("ITEM_MENU_CANDIDATE_BLOCKED: missing " + key);
        try { return Double.parseDouble(value); }
        catch (NumberFormatException failure) { throw new IllegalArgumentException("Invalid " + key, failure); }
    }

    /** Optional proposed rectangles allow diagnostics without replacing original rendering. */
    public static synchronized void configureDiagnostic(PixelLayout.Profile name, PixelLayout.Profile description) {
        if (name != null) validate(name);
        if (description != null) validate(description);
        configuration = new Configuration(false, name, description);
        configured = true;
    }

    public static void disablePrototype() { configureDiagnostic(null, null); }
    public static boolean prototypeEnabled() { return configuration.prototype; }
    public static String mode() { return prototypeEnabled() ? "prototype-unverified" : "diagnostic-not-adapted"; }
    public static Diagnostic lastName() { return lastName; }
    public static Diagnostic lastDescription() { return lastDescription; }

    private static void validate(PixelLayout.Profile p) {
        if (p == null || p.id.length() == 0 || p.version.length() == 0
                || p.content.width <= 0 || p.content.height <= 0 || p.lineStep < 14)
            throw new IllegalArgumentException("Item prototype needs versioned positive rectangles and >=14px line step");
    }

    /** Inserted immediately before Le.u/Le.v assignments; equality never determines identity. */
    public static synchronized void registerName(Le owner, Lg name) { register(owner, name, true); }
    public static synchronized void registerDescription(Le owner, Lb description) { register(owner, description, false); }
    private static void register(Object owner, Object widget, boolean name) {
        if (!configured) configureFromProperties();
        if (owner == null || widget == null) throw new NullPointerException("item widget");
        Entry old = entry(widget);
        if (old != null) throw new IllegalStateException("Duplicate item widget registration");
        // entry() pruned dead weak identities. Never evict a live registered widget:
        // doing so would silently send it back through the old layout.
        if (ENTRIES.size() >= MAX_ENTRIES)
            throw new IllegalStateException("ITEM_MENU_CANDIDATE_BLOCKED: registration-capacity-" + MAX_ENTRIES);
        ENTRIES.add(new Entry(owner, widget, name));
    }

    private static synchronized Entry entry(Object widget) {
        Entry found = null;
        for (Iterator<Entry> it = ENTRIES.iterator(); it.hasNext();) {
            Entry e = it.next();
            Object current = e.widget.get();
            if (current == null || e.owner.get() == null) it.remove();
            else if (current == widget) found = e;
        }
        return found;
    }

    /** Observe Le.b's complete local2 BEFORE the equipped-name formatting branch.
     * This never changes the original blink/empty-string gate or the '+' transform.
     */
    public static synchronized void observeFullName(Le owner, String fullName) {
        for (Entry e : ENTRIES)
            if (e.name && e.owner.get() == owner) e.fullName = fullName;
    }

    /** Replacement of the final SN call in Lg; category labels are passed through unchanged. */
    public static void drawName(SN sn, String text, int x, int y, String role, Lg widget) {
        Entry e = entry(widget);
        if (e == null || !e.name) { sn.a(text, x, y, role); return; }
        Configuration c = configuration;
        Diagnostic d = diagnose(e, sn, text, x, y, role, c.name, c.prototype);
        lastName = d;
        if (!c.prototype) { sn.a(text, x, y, role); return; }
        requireDrawable(d);
        render(sn, d.plan, x, y, role);
    }

    /** Receives the final amr$d.a() string BEFORE amw, 14-code-unit splitting and zip.
     * False means diagnostic/unregistered: the original chain consumes the SAME string once.
     */
    public static boolean drawDescription(Lb widget, SN sn, String fullText) {
        Entry e = entry(widget);
        if (e == null || e.name) return false;
        Configuration c = configuration;
        Diagnostic d = diagnose(e, sn, fullText, widget.e_(), widget.f_(), sn.b(),
                c.description, c.prototype);
        lastDescription = d;
        if (!c.prototype) return false;
        requireDrawable(d);
        render(sn, d.plan, d.anchorX, d.anchorY, d.fontRole);
        return true;
    }

    private static Diagnostic diagnose(Entry e, SN sn, String text, int x, int y, String role,
                                       PixelLayout.Profile profile, boolean prototype) {
        if (profile == null)
            return new Diagnostic(text, e.fullName, x, y, role, null, null, prototype,
                    "unknown-contentRect-and-parent-clip");
        arp font = LayoutBridge.font(sn, role);
        PixelLayout.Metrics metrics = LayoutBridge.metrics(font);
        long[] signature = metricSignature(text, metrics);
        PixelLayout.Plan plan;
        synchronized (e) {
            // Re-measure the actual consumed glyphs/kerning to detect mutable font revisions;
            // rebuild only when final text, metrics or the explicit profile changes.
            if (e.plan == null || e.font != font || e.profile != profile
                    || !Arrays.equals(e.signature, signature) || !text.equals(e.plan.text)) {
                e.plan = PixelLayout.layout(text, metrics, profile);
                e.font = font; e.profile = profile; e.signature = signature;
            }
            plan = e.plan;
        }
        String reason = plan.overflow ? "pixel-layout-overflow-no-safe-original-paging" : null;
        if (reason == null && !drawableOrigins(plan, x, y)) reason = "non-integral-or-out-of-range-SN-origins";
        return new Diagnostic(text, e.fullName, x, y, role, profile, plan, prototype, reason);
    }

    /** Pure test/diagnostic entry; retains every line even on overflow. */
    public static PixelLayout.Plan plan(String finalText, PixelLayout.Metrics metrics,
                                        PixelLayout.Profile profile) {
        validate(profile);
        return PixelLayout.layout(finalText, metrics, profile);
    }

    private static boolean drawableOrigins(PixelLayout.Plan p, int x, int y) {
        for (PixelLayout.Line l : p.lines)
            if (!integer(l.originX) || !integer(l.originY)
                    || !integer(x + l.originX) || !integer(y - l.originY)) return false;
        return true;
    }
    private static boolean integer(double value) {
        return value == Math.rint(value) && value >= Integer.MIN_VALUE && value <= Integer.MAX_VALUE;
    }

    private static void requireDrawable(Diagnostic d) {
        if (d.blockedReason != null)
            throw new IllegalStateException("ITEM_MENU_CANDIDATE_BLOCKED: " + d.blockedReason);
    }

    private static void render(SN sn, PixelLayout.Plan plan, int anchorX, int anchorY, String role) {
        // All lines validated before the first draw: no partial candidate on overflow.
        for (PixelLayout.Line line : plan.lines) {
            PixelLayout.VisiblePrefix visible = line.visiblePrefix(plan.text.length());
            StringBuilder value = new StringBuilder();
            // Do not send zero-advance controls or explicit breaks to SN's whole-line renderer.
            for (PixelLayout.PlacedGlyph glyph : visible.glyphs) value.appendCodePoint(glyph.codePoint);
            if (value.length() > 0) LayoutBridge.draw(sn, value.toString(),
                    Math.addExact(anchorX, (int) line.originX),
                    Math.subtractExact(anchorY, (int) line.originY), role);
        }
    }

    private static long[] metricSignature(String text, PixelLayout.Metrics metrics) {
        long[] values = new long[Math.multiplyExact(text.length(), 6)];
        int used = 0, previous = -1;
        for (int at = 0; at < text.length();) {
            int cp = text.codePointAt(at); at += Character.charCount(cp);
            // Match non-drawing characters in PixelLayout; unsupported glyphs are its error.
            if (Character.getType(cp) == Character.CONTROL || Character.getType(cp) == Character.FORMAT
                    || cp == 0x2028 || cp == 0x2029 || (cp >= 0xfe00 && cp <= 0xfe0f)
                    || (cp >= 0xe0100 && cp <= 0xe01ef)) { continue; }
            PixelLayout.Glyph g = metrics.glyph(cp);
            if (g == null) throw new IllegalArgumentException("Missing item glyph U+" + Integer.toHexString(cp));
            values[used++] = Double.doubleToLongBits(g.xAdvance);
            values[used++] = Double.doubleToLongBits(g.xOffset);
            values[used++] = Double.doubleToLongBits(g.yOffset);
            values[used++] = Double.doubleToLongBits(g.width);
            values[used++] = Double.doubleToLongBits(g.height);
            values[used++] = previous >= 0 ? Double.doubleToLongBits(metrics.kerning(previous, cp)) : 0;
            previous = cp;
        }
        return Arrays.copyOf(values, used);
    }

    public static final class Diagnostic {
        public final String finalText, completeNameBeforeEquipmentSuffix, fontRole, blockedReason;
        public final int anchorX, anchorY;
        public final PixelLayout.Profile profile;
        public final PixelLayout.Plan plan;
        public final boolean prototype, parentClipVerified = false;
        private Diagnostic(String text, String name, int x, int y, String role,
                           PixelLayout.Profile profile, PixelLayout.Plan plan,
                           boolean prototype, String blocked) {
            finalText = text; completeNameBeforeEquipmentSuffix = name;
            anchorX = x; anchorY = y; fontRole = role; this.profile = profile;
            this.plan = plan; this.prototype = prototype; blockedReason = blocked;
        }
    }
    private static final class Configuration {
        final boolean prototype;
        final PixelLayout.Profile name, description;
        Configuration(boolean prototype, PixelLayout.Profile name, PixelLayout.Profile description) {
            this.prototype = prototype; this.name = name; this.description = description;
        }
    }
    private static final class Entry {
        final WeakReference<Object> owner, widget;
        final boolean name;
        String fullName;
        arp font;
        PixelLayout.Profile profile;
        PixelLayout.Plan plan;
        long[] signature;
        Entry(Object owner, Object widget, boolean name) {
            this.owner = new WeakReference<Object>(owner); this.widget = new WeakReference<Object>(widget);
            this.name = name;
        }
    }
}
