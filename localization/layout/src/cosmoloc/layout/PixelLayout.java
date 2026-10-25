package cosmoloc.layout;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Game-independent, Java 8 pixel layout. Coordinates are logical pixels; all
 * spans are half-open UTF-16 offsets, and revealIndex is a consumed source
 * UTF-16 count (not an inclusive character index). No global cache is used.
 *
 * Input must be final display text, not markup. CR/LF/CRLF and U+2028/U+2029
 * are explicit line breaks. Other controls/format characters are preserved as
 * zero-advance, non-drawing code points and reported (except shaping joiners,
 * variation selectors and emoji tags). TAB is therefore not a tab stop.
 * This is a positioning core, not a bidi/shaping engine: metrics must describe
 * the intended glyphs. Conservative atomic units protect combining marks,
 * joiner/virama sequences, Hangul, flags and ellipsis runs. They do not claim
 * a versioned, complete Unicode UAX #29 implementation.
 */
public final class PixelLayout {
    private PixelLayout() { }

    public interface Metrics {
        Glyph glyph(int codePoint);
        double kerning(int leftCodePoint, int rightCodePoint);
    }

    public static final class Glyph {
        public final double xAdvance, xOffset, yOffset, width, height;
        public Glyph(double xAdvance, double xOffset, double yOffset,
                     double width, double height) {
            nonnegative(xAdvance, "xAdvance");
            finite(xOffset, "xOffset"); finite(yOffset, "yOffset");
            nonnegative(width, "width"); nonnegative(height, "height");
            this.xAdvance = xAdvance; this.xOffset = xOffset;
            this.yOffset = yOffset; this.width = width; this.height = height;
        }
    }

    public static final class Rect {
        public final double x, y, width, height;
        public Rect(double x, double y, double width, double height) {
            finite(x, "x"); finite(y, "y");
            nonnegative(width, "width"); nonnegative(height, "height");
            finite(x + width, "right"); finite(y + height, "bottom");
            this.x = x; this.y = y; this.width = width; this.height = height;
        }
    }

    public static final class Insets {
        public static final Insets NONE = new Insets(0, 0, 0, 0);
        public final double left, top, right, bottom;
        public Insets(double left, double top, double right, double bottom) {
            nonnegative(left, "left"); nonnegative(top, "top");
            nonnegative(right, "right"); nonnegative(bottom, "bottom");
            this.left = left; this.top = top; this.right = right; this.bottom = bottom;
        }
    }

    /** One profile per final-text/font/container revision; identity is adapter-owned. */
    public static final class Profile {
        public final Rect content;
        public final double lineStep;
        public final Insets effects;
        public final String id, version;
        public Profile(Rect content, double lineStep, Insets effects) {
            this("", "", content, lineStep, effects);
        }
        public Profile(String id, String version, Rect content,
                       double lineStep, Insets effects) {
            if (id == null || version == null || content == null || effects == null)
                throw new NullPointerException("profile field");
            finite(lineStep, "lineStep");
            if (lineStep <= 0) throw new IllegalArgumentException("lineStep must be positive");
            this.id = id; this.version = version; this.content = content;
            this.lineStep = lineStep; this.effects = effects;
        }
    }

    public static final class Span {
        public final int start, end;
        public Span(int start, int end) {
            if (start < 0 || end < start) throw new IllegalArgumentException("invalid span");
            this.start = start; this.end = end;
        }
        @Override public String toString() { return "[" + start + "," + end + ")"; }
    }

    /** A contiguous display range may expand/contract one original source range. */
    public static final class SourceRange {
        public final Span display, source;
        public SourceRange(int displayStart, int displayEnd, int sourceStart, int sourceEnd) {
            display = new Span(displayStart, displayEnd);
            source = new Span(sourceStart, sourceEnd);
        }
    }

    public static final class Bounds {
        public final double left, top, right, bottom;
        public final boolean empty;
        private Bounds(double left, double top, double right, double bottom, boolean empty) {
            finite(left, "bounds left"); finite(top, "bounds top");
            finite(right, "bounds right"); finite(bottom, "bounds bottom");
            this.left = left; this.top = top; this.right = right;
            this.bottom = bottom; this.empty = empty;
        }
        public double width() { return empty ? 0 : right - left; }
        public double height() { return empty ? 0 : bottom - top; }
    }

    public enum IssueKind {
        UNIT_TOO_WIDE, LINE_TOO_WIDE, LINE_TOO_HIGH, HEIGHT_OVERFLOW,
        FORCED_BREAK, CONTROL_CHARACTER
    }

    public static final class Issue {
        public final IssueKind kind;
        public final Span display;
        public final int lineIndex;
        private Issue(IssueKind kind, Span display, int lineIndex) {
            this.kind = kind; this.display = display; this.lineIndex = lineIndex;
        }
        public boolean isOverflow() {
            return kind == IssueKind.UNIT_TOO_WIDE || kind == IssueKind.LINE_TOO_WIDE
                || kind == IssueKind.LINE_TOO_HIGH || kind == IssueKind.HEIGHT_OVERFLOW;
        }
    }

    public static final class PlacedGlyph {
        public final int codePoint;
        public final Span display, source;
        public final Glyph glyph;
        /** Pen origin; offsets are already included in inkBounds, not in x/y. */
        public final double x, y;
        public final Bounds inkBounds, effectBounds;
        private PlacedGlyph(RawGlyph raw, Span source, double x, double y, Insets effects) {
            this.codePoint = raw.cp; this.display = raw.span; this.source = source;
            this.glyph = raw.glyph; this.x = x; this.y = y;
            boolean empty = glyph.width == 0 || glyph.height == 0;
            inkBounds = new Bounds(x + glyph.xOffset, y + glyph.yOffset,
                x + glyph.xOffset + glyph.width, y + glyph.yOffset + glyph.height, empty);
            effectBounds = empty ? inkBounds : new Bounds(inkBounds.left - effects.left,
                inkBounds.top - effects.top, inkBounds.right + effects.right,
                inkBounds.bottom + effects.bottom, false);
        }
    }

    public static final class Unit {
        public final Span display, source;
        public final boolean hardBreak;
        public final List<PlacedGlyph> glyphs;
        private Unit(RawUnit raw, List<PlacedGlyph> glyphs) {
            display = raw.span; source = raw.source; hardBreak = raw.hardBreak;
            this.glyphs = immutable(glyphs);
        }
    }

    public static final class Line {
        public final int index;
        public final Span display;
        public final List<Unit> units;
        public final List<PlacedGlyph> glyphs;
        public final double originX, originY, advance;
        /** Ink/effects plus whitespace advances and at least one lineStep.
         * The unused advance after the last ink-bearing glyph is not a width. */
        public final Bounds layoutBounds;
        public final Bounds inkBounds, effectBounds;
        private Line(int index, Span span, List<Unit> units, List<PlacedGlyph> glyphs,
                     double x, double y, double advance, Bounds layout,
                     Bounds ink, Bounds effects) {
            this.index = index; display = span; this.units = immutable(units);
            this.glyphs = immutable(glyphs); originX = x; originY = y;
            this.advance = advance; layoutBounds = layout; inkBounds = ink; effectBounds = effects;
        }
        /** Atomic units reveal at their entire source range's exclusive end. */
        public VisiblePrefix visiblePrefix(int originalRevealIndex) {
            int count = 0, glyphCount = 0, end = display.start;
            for (Unit u : units) {
                if (originalRevealIndex < u.source.end) break;
                count++; glyphCount += u.glyphs.size(); end = u.display.end;
            }
            return new VisiblePrefix(this, count, glyphCount, end);
        }
    }

    public static final class VisiblePrefix {
        public final Line line;
        public final int unitCount, glyphCount, displayEnd;
        public final List<Unit> units;
        public final List<PlacedGlyph> glyphs;
        private VisiblePrefix(Line line, int unitCount, int glyphCount, int displayEnd) {
            this.line = line; this.unitCount = unitCount; this.glyphCount = glyphCount;
            this.displayEnd = displayEnd;
            units = line.units.subList(0, unitCount);
            glyphs = line.glyphs.subList(0, glyphCount);
        }
    }

    public static final class Plan {
        public final String text;
        public final Profile profile;
        public final List<SourceRange> sourceRanges;
        public final List<Line> lines;
        public final List<Issue> issues;
        public final Bounds layoutBounds, inkBounds, effectBounds;
        public final boolean overflow;
        private Plan(String text, Profile profile, List<SourceRange> ranges,
                     List<Line> lines, List<Issue> issues) {
            this.text = text; this.profile = profile; sourceRanges = immutable(ranges);
            this.lines = immutable(lines); this.issues = immutable(issues);
            Bounds layout = emptyBounds(), ink = emptyBounds(), effect = emptyBounds();
            for (Line line : lines) {
                layout = union(layout, line.layoutBounds); ink = union(ink, line.inkBounds);
                effect = union(effect, line.effectBounds);
            }
            layoutBounds = layout; inkBounds = ink; effectBounds = effect;
            boolean over = false;
            for (Issue issue : issues) over |= issue.isOverflow();
            overflow = over;
        }
        public List<VisiblePrefix> visiblePrefixes(int originalRevealIndex) {
            List<VisiblePrefix> visible = new ArrayList<VisiblePrefix>();
            for (Line line : lines) visible.add(line.visiblePrefix(originalRevealIndex));
            return immutable(visible);
        }
    }

    public static Plan layout(String text, Metrics metrics, Profile profile) {
        if (text == null) throw new NullPointerException("text");
        List<SourceRange> identity = new ArrayList<SourceRange>();
        for (int at = 0; at < text.length();) {
            int next = at + Character.charCount(text.codePointAt(at));
            identity.add(new SourceRange(at, next, at, next));
            at = next;
        }
        return build(text, metrics, profile, identity, true);
    }

    /**
     * Ranges must exactly partition display text at code-point boundaries.
     * Source ranges may repeat, overlap, or be non-monotonic. Every atomic unit
     * waits for all intersecting ranges; each returned line is always a prefix.
     */
    public static Plan layout(String text, Metrics metrics, Profile profile,
                              List<SourceRange> sourceRanges) {
        return build(text, metrics, profile, sourceRanges, false);
    }

    private static Plan build(String text, Metrics metrics, Profile profile,
                              List<SourceRange> ranges, boolean identity) {
        if (text == null || metrics == null || profile == null || ranges == null)
            throw new NullPointerException("layout input");
        validateText(text);
        ranges = new ArrayList<SourceRange>(ranges);
        int covered = 0;
        for (SourceRange r : ranges) {
            if (r == null || r.display.start != covered || r.display.end <= covered
                || r.display.end > text.length() || !codePointBoundary(text, r.display.end))
                throw new IllegalArgumentException("source ranges must partition display text");
            covered = r.display.end;
        }
        if (covered != text.length()) throw new IllegalArgumentException("incomplete source map");
        List<Issue> issues = new ArrayList<Issue>();
        List<RawUnit> units = units(text, metrics, profile, ranges, identity, issues);
        List<Line> lines = new ArrayList<Line>();
        int paragraphStart = 0;
        for (int i = 0; i <= units.size(); i++) {
            if (i == units.size() || units.get(i).hardBreak) {
                wrap(text, metrics, profile, units, paragraphStart, i,
                    i < units.size() ? units.get(i) : null, lines, issues);
                paragraphStart = i + 1;
            }
        }
        return new Plan(text, profile, ranges, lines, issues);
    }

    private static void wrap(String text, Metrics metrics, Profile p, List<RawUnit> units,
                             int start, int end, RawUnit newline,
                             List<Line> lines, List<Issue> issues) {
        int at = start;
        do {
            int fit = at;
            int preferred = -1, legal = -1;
            Measure measure = new Measure();
            while (fit < end) {
                Measure next = new Measure(measure);
                append(next, units.get(fit), metrics, p.effects, null);
                if (next.width() > p.content.width && fit > at) break;
                measure = next;
                fit++;
                if (fit == end || legalBoundary(text, units.get(fit - 1), units.get(fit))) {
                    legal = fit;
                    if (fit == end || preferredBoundary(text, units.get(fit - 1), units.get(fit)))
                        preferred = fit;
                }
                if (next.width() > p.content.width) break; // one oversized unit, always progresses
            }
            int stop = fit;
            if (fit < end) {
                if (preferred > at) stop = preferred;
                else if (legal > at) stop = legal;
                else {
                    // Constraints cannot all hold: preserve all text, record deterministic fallback.
                    issues.add(new Issue(IssueKind.FORCED_BREAK,
                        new Span(units.get(at).span.start, units.get(fit - 1).span.end), lines.size()));
                }
            }
            RawUnit lastBreak = stop == end ? newline : null;
            int emptyOffset = at < units.size() ? units.get(at).span.start : text.length();
            lines.add(place(metrics, p, units, at, stop, lastBreak, emptyOffset, lines.size(), issues));
            at = stop;
        } while (at < end);
    }

    private static Line place(Metrics metrics, Profile p, List<RawUnit> all,
                              int start, int end, RawUnit newline, int emptyOffset,
                              int index, List<Issue> issues) {
        Measure m = new Measure();
        List<Position> positions = new ArrayList<Position>();
        for (int i = start; i < end; i++) append(m, all.get(i), metrics, p.effects, positions);
        double x = p.content.x - m.left;
        double y = p.content.y + index * p.lineStep - m.top;
        finite(y, "line origin");
        List<Unit> units = new ArrayList<Unit>();
        List<PlacedGlyph> glyphs = new ArrayList<PlacedGlyph>();
        Bounds ink = emptyBounds(), effect = emptyBounds();
        int pos = 0;
        for (int i = start; i < end; i++) {
            RawUnit raw = all.get(i);
            List<PlacedGlyph> local = new ArrayList<PlacedGlyph>();
            for (RawGlyph g : raw.glyphs) {
                Position position = positions.get(pos++);
                PlacedGlyph placed = new PlacedGlyph(g, raw.source, x + position.x, y, p.effects);
                local.add(placed); glyphs.add(placed);
                ink = union(ink, placed.inkBounds); effect = union(effect, placed.effectBounds);
            }
            units.add(new Unit(raw, local));
            Measure single = new Measure();
            append(single, raw, metrics, p.effects, null);
            if (single.width() > p.content.width)
                issues.add(new Issue(IssueKind.UNIT_TOO_WIDE, raw.span, index));
        }
        if (newline != null) units.add(new Unit(newline, Collections.<PlacedGlyph>emptyList()));
        int spanStart = units.isEmpty() ? emptyOffset : units.get(0).display.start;
        int spanEnd = units.isEmpty() ? emptyOffset : units.get(units.size() - 1).display.end;
        Span span = new Span(spanStart, spanEnd);
        double height = Math.max(p.lineStep, m.bottom - m.top);
        Bounds box = new Bounds(p.content.x, p.content.y + index * p.lineStep,
            p.content.x + m.width(), p.content.y + index * p.lineStep + height, false);
        if (m.width() > p.content.width) issues.add(new Issue(IssueKind.LINE_TOO_WIDE, span, index));
        if (m.bottom - m.top > p.lineStep) issues.add(new Issue(IssueKind.LINE_TOO_HIGH, span, index));
        if (box.bottom > p.content.y + p.content.height)
            issues.add(new Issue(IssueKind.HEIGHT_OVERFLOW, span, index));
        return new Line(index, span, units, glyphs, x, y, m.pen, box, ink, effect);
    }

    private static final class Measure {
        double pen, left, right, top, bottom;
        int previous = -1;
        Measure() { }
        Measure(Measure m) {
            pen = m.pen; left = m.left; right = m.right;
            top = m.top; bottom = m.bottom; previous = m.previous;
        }
        double width() { return right - left; }
    }
    private static final class Position {
        final double x;
        Position(double x) { this.x = x; }
    }
    private static void append(Measure m, RawUnit unit, Metrics metrics, Insets effects,
                               List<Position> positions) {
        for (RawGlyph raw : unit.glyphs) {
            Glyph g = raw.glyph;
            if (m.previous >= 0) {
                double kern = metrics.kerning(m.previous, raw.cp);
                finite(kern, "kerning"); m.pen += kern;
            }
            if (positions != null) positions.add(new Position(m.pen));
            m.left = Math.min(m.left, m.pen);
            m.right = Math.max(m.right, m.pen);
            if (g.width > 0 && g.height > 0) {
                m.left = Math.min(m.left, m.pen + g.xOffset - effects.left);
                m.right = Math.max(m.right, m.pen + g.xOffset + g.width + effects.right);
                m.top = Math.min(m.top, g.yOffset - effects.top);
                m.bottom = Math.max(m.bottom, g.yOffset + g.height + effects.bottom);
            }
            m.pen += g.xAdvance;
            finite(m.pen, "accumulated advance");
            // A final ink glyph's xAdvance positions a hypothetical next glyph;
            // it is not its rendered right edge. Empty glyphs (notably spaces)
            // still consume their entire advance, including trailing spaces.
            if (g.width == 0 || g.height == 0) {
                m.left = Math.min(m.left, m.pen); m.right = Math.max(m.right, m.pen);
            }
            finite(m.width(), "measured width");
            m.previous = raw.cp;
        }
    }

    private static final class RawGlyph {
        final int cp;
        final Span span;
        final Glyph glyph;
        RawGlyph(int cp, Span span, Glyph glyph) { this.cp = cp; this.span = span; this.glyph = glyph; }
    }
    private static final class RawUnit {
        final Span span, source;
        final boolean hardBreak;
        final List<RawGlyph> glyphs;
        RawUnit(Span span, Span source, boolean hardBreak, List<RawGlyph> glyphs) {
            this.span = span; this.source = source; this.hardBreak = hardBreak; this.glyphs = glyphs;
        }
    }

    private static List<RawUnit> units(String text, Metrics metrics, Profile p,
                                      List<SourceRange> ranges, boolean identity, List<Issue> issues) {
        List<RawUnit> result = new ArrayList<RawUnit>();
        int mapAt = 0;
        for (int start = 0; start < text.length();) {
            int end = unitEnd(text, start);
            Span span = new Span(start, end);
            boolean hard = hardBreak(text.codePointAt(start));
            Span source = span;
            if (!identity) {
                while (ranges.get(mapAt).display.end <= start) mapAt++;
                int lo = Integer.MAX_VALUE, hi = 0;
                for (int r = mapAt; r < ranges.size() && ranges.get(r).display.start < end; r++) {
                    lo = Math.min(lo, ranges.get(r).source.start);
                    hi = Math.max(hi, ranges.get(r).source.end);
                }
                source = new Span(lo, hi);
            }
            List<RawGlyph> glyphs = new ArrayList<RawGlyph>();
            if (!hard) {
                for (int at = start; at < end;) {
                    int cp = text.codePointAt(at), next = at + Character.charCount(cp);
                    if (nonDrawing(cp)) {
                        if (!shapingControl(cp)) issues.add(new Issue(IssueKind.CONTROL_CHARACTER,
                            new Span(at, next), -1));
                    } else {
                        Glyph glyph = metrics.glyph(cp);
                        if (glyph == null) throw new IllegalArgumentException("missing glyph U+" + Integer.toHexString(cp));
                        glyphs.add(new RawGlyph(cp, new Span(at, next), glyph));
                    }
                    at = next;
                }
            }
            result.add(new RawUnit(span, source, hard, glyphs));
            start = end;
        }
        return result;
    }

    private static int unitEnd(String text, int start) {
        int first = text.codePointAt(start), at = start + Character.charCount(first);
        if (first == '\r' && at < text.length() && text.charAt(at) == '\n') return at + 1;
        if (hardBreak(first)) return at;
        // Ellipses are never split internally, including the Chinese six-dot pair.
        if (first == 0x2026 || first == 0x22ef || first == '.') {
            int end = at;
            while (end < text.length() && text.codePointAt(end) == first)
                end += Character.charCount(first);
            if (first != '.' || end - start >= 3) at = end;
        }
        int previous = first, regionalCount = regional(first) ? 1 : 0;
        boolean joinNext = first == 0x200d || virama(first);
        while (at < text.length()) {
            int cp = text.codePointAt(at);
            if (hardBreak(cp)) break;
            boolean attach = combining(cp) || shapingControl(cp) || joinNext || prepend(previous)
                || hangulJoin(previous, cp) || (regional(cp) && regionalCount == 1);
            if (!attach) break;
            at += Character.charCount(cp);
            if (regional(cp)) regionalCount++; else if (!combining(cp)) regionalCount = 0;
            joinNext = cp == 0x200d || virama(cp) || (joinNext && combining(cp));
            previous = cp;
        }
        return at;
    }

    private static boolean legalBoundary(String text, RawUnit left, RawUnit right) {
        int a = trailingBase(text, left.span), b = text.codePointAt(right.span.start);
        if (a == 0xa0 || b == 0xa0 || a == 0x2060 || b == 0x2060) return false;
        return !contains("（［｛〈《「『【〔〖〘〚‘“([{", a)
            && !contains("、。，．：；？！‼⁇⁈⁉）］｝〉》」』】〕〗〙〛’”)]},.!?:;%‰…⋯", b);
    }
    private static boolean preferredBoundary(String text, RawUnit left, RawUnit right) {
        int a = trailingBase(text, left.span), b = text.codePointAt(right.span.start);
        return !(word(a) && word(b));
    }
    private static int trailingBase(String text, Span span) {
        int at = span.end;
        int cp = text.codePointBefore(at);
        while (at > span.start && (combining(cp) || shapingControl(cp))) {
            at -= Character.charCount(cp);
            if (at == span.start) break;
            cp = text.codePointBefore(at);
        }
        return cp;
    }
    private static boolean word(int cp) {
        return cp == '_' || cp == '\'' || Character.isDigit(cp)
            || (Character.isLetter(cp) && Character.UnicodeScript.of(cp) == Character.UnicodeScript.LATIN);
    }
    private static boolean contains(String value, int cp) { return value.indexOf(cp) >= 0; }
    private static boolean hardBreak(int cp) {
        return cp == '\r' || cp == '\n' || cp == 0x2028 || cp == 0x2029;
    }
    private static boolean nonDrawing(int cp) {
        int type = Character.getType(cp);
        return type == Character.CONTROL || type == Character.FORMAT || shapingControl(cp);
    }
    private static boolean shapingControl(int cp) {
        return cp == 0x200c || cp == 0x200d || (cp >= 0xfe00 && cp <= 0xfe0f)
            || (cp >= 0xe0100 && cp <= 0xe01ef) || (cp >= 0xe0020 && cp <= 0xe007f);
    }
    private static boolean combining(int cp) {
        int t = Character.getType(cp);
        return t == Character.NON_SPACING_MARK || t == Character.COMBINING_SPACING_MARK
            || t == Character.ENCLOSING_MARK || (cp >= 0x1f3fb && cp <= 0x1f3ff);
    }
    private static boolean virama(int cp) {
        if (!combining(cp)) return false;
        String name = Character.getName(cp);
        return name != null && (name.contains("VIRAMA") || name.contains("HALANT"));
    }
    private static boolean prepend(int cp) {
        return (cp >= 0x0600 && cp <= 0x0605) || cp == 0x06dd || cp == 0x070f
            || (cp >= 0x0890 && cp <= 0x0891) || cp == 0x08e2 || cp == 0x0d4e
            || cp == 0x110bd || cp == 0x110cd || (cp >= 0x111c2 && cp <= 0x111c3)
            || cp == 0x1193f || cp == 0x11941 || cp == 0x11a3a
            || (cp >= 0x11a84 && cp <= 0x11a89) || cp == 0x11d46;
    }
    private static boolean regional(int cp) { return cp >= 0x1f1e6 && cp <= 0x1f1ff; }
    private static int hangul(int cp) {
        if ((cp >= 0x1100 && cp <= 0x115f) || (cp >= 0xa960 && cp <= 0xa97c)) return 1;
        if ((cp >= 0x1160 && cp <= 0x11a7) || (cp >= 0xd7b0 && cp <= 0xd7c6)) return 2;
        if ((cp >= 0x11a8 && cp <= 0x11ff) || (cp >= 0xd7cb && cp <= 0xd7fb)) return 3;
        if (cp >= 0xac00 && cp <= 0xd7a3) return (cp - 0xac00) % 28 == 0 ? 4 : 5;
        return 0;
    }
    private static boolean hangulJoin(int a, int b) {
        int x = hangul(a), y = hangul(b);
        return (x == 1 && (y == 1 || y == 2 || y == 4 || y == 5))
            || ((x == 2 || x == 4) && (y == 2 || y == 3))
            || ((x == 3 || x == 5) && y == 3);
    }
    private static void validateText(String text) {
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (Character.isHighSurrogate(c)) {
                if (i + 1 >= text.length() || !Character.isLowSurrogate(text.charAt(i + 1)))
                    throw new IllegalArgumentException("unpaired surrogate at " + i);
                i++;
            } else if (Character.isLowSurrogate(c))
                throw new IllegalArgumentException("unpaired surrogate at " + i);
        }
    }
    private static boolean codePointBoundary(String text, int offset) {
        return offset == 0 || offset == text.length() || !Character.isLowSurrogate(text.charAt(offset));
    }
    private static Bounds emptyBounds() { return new Bounds(0, 0, 0, 0, true); }
    private static Bounds union(Bounds a, Bounds b) {
        if (a.empty) return b;
        if (b.empty) return a;
        return new Bounds(Math.min(a.left, b.left), Math.min(a.top, b.top),
            Math.max(a.right, b.right), Math.max(a.bottom, b.bottom), false);
    }
    private static <T> List<T> immutable(List<T> values) {
        return Collections.unmodifiableList(new ArrayList<T>(values));
    }
    private static void finite(double value, String name) {
        if (Double.isNaN(value) || Double.isInfinite(value))
            throw new IllegalArgumentException(name + " must be finite");
    }
    private static void nonnegative(double value, String name) {
        finite(value, name);
        if (value < 0) throw new IllegalArgumentException(name + " must be nonnegative");
    }
}
