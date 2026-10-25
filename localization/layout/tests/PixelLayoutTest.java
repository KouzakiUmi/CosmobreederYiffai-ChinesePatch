import cosmoloc.layout.PixelLayout;
import cosmoloc.layout.PixelLayout.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/** No dependencies or -ea requirement. Run main; assertion failures exit nonzero. */
public final class PixelLayoutTest {
    private static int checks;
    private static final Metrics TEN = new Metrics() {
        public Glyph glyph(int cp) {
            if (cp == ' ') return new Glyph(4, 0, 0, 0, 0);
            int type = Character.getType(cp);
            if (type == Character.NON_SPACING_MARK || type == Character.COMBINING_SPACING_MARK
                || type == Character.ENCLOSING_MARK || (cp >= 0x1f3fb && cp <= 0x1f3ff))
                return new Glyph(0, -5, 0, 5, 4);
            return new Glyph(cp < 128 ? 6 : 10, 0, 0, cp < 128 ? 6 : 10, 10);
        }
        public double kerning(int a, int b) { return 0; }
    };

    public static void main(String[] args) {
        pixelBoundaries(); geometry(); wordsAndPunctuation(); explicitBreaksAndSpaces();
        atomicText(); reveal(); sourceMaps(); controlsAndInvalidInput(); overflow();
        immutableAndDeterministic(); exhaustiveSmallInputs();
        System.out.println("PixelLayoutTest: " + checks + " checks passed");
    }

    private static Profile profile(double width, double height, double step) {
        return new Profile("test", "1", new Rect(0, 0, width, height), step, Insets.NONE);
    }
    private static Plan plan(String text, double width) {
        return PixelLayout.layout(text, TEN, profile(width, 1000, 14));
    }
    private static void pixelBoundaries() {
        eq(2, plan("中文", 19).lines.size(), "width -1");
        eq(1, plan("中文", 20).lines.size(), "width exact");
        eq(1, plan("中文", 21).lines.size(), "width +1");
        check(PixelLayout.layout("中\n文", TEN, profile(10, 27, 14)).overflow, "height -1");
        check(!PixelLayout.layout("中\n文", TEN, profile(10, 28, 14)).overflow, "height exact");
        check(!PixelLayout.layout("中\n文", TEN, profile(10, 29, 14)).overflow, "height +1");
        eq(2, plan("中文", 20 - 0.25).lines.size(), "fractional width does not round up");
    }

    private static void geometry() {
        Metrics offsets = new Metrics() {
            public Glyph glyph(int cp) { return new Glyph(8, -2, -3, 10, 10); }
            public double kerning(int a, int b) { return -1; }
        };
        Profile p = new Profile(new Rect(30, 40, 20, 16), 16, new Insets(1, 1, 2, 2));
        Plan exact = PixelLayout.layout("甲乙", offsets, p);
        check(!exact.overflow, "offset/effect exact fit");
        eq(20, exact.lines.get(0).layoutBounds.width(), "offset/kern/effects footprint");
        PlacedGlyph first = exact.lines.get(0).glyphs.get(0);
        PlacedGlyph last = exact.lines.get(0).glyphs.get(1);
        eq(33, first.x, "negative first offset shifts pen, not clip");
        eq(44, first.y, "negative top offset plus effect shifts origin");
        eq(30, first.effectBounds.left, "left effect in rect");
        eq(40, first.effectBounds.top, "top effect in rect");
        eq(7, last.x - first.x, "negative kern accumulated");
        eq(50, last.effectBounds.right, "last glyph width not just advance");
        eq(2, PixelLayout.layout("甲乙", offsets,
            new Profile(new Rect(0, 0, 19, 100), 16, p.effects)).lines.size(), "effects width -1");
        Metrics wideLast = new Metrics() {
            public Glyph glyph(int cp) { return new Glyph(4, 3, 2, 9, 10); }
            public double kerning(int a, int b) { return 2; }
        };
        eq(18, PixelLayout.layout("AB", wideLast, profile(18, 20, 14))
            .lines.get(0).layoutBounds.width(), "positive offset, last ink and kern");
        eq(2, PixelLayout.layout("AB", wideLast, profile(17, 40, 14)).lines.size(), "last ink -1");
        eq(1, PixelLayout.layout("AB", wideLast, profile(19, 20, 14)).lines.size(), "last ink +1");
        eq(24, plan("中 文", 24).lines.get(0).advance, "space advance preserved");
        Metrics looseAdvance = new Metrics() {
            public Glyph glyph(int cp) { return new Glyph(20, 0, 0, 10, 10); }
            public double kerning(int a, int b) { return 0; }
        };
        Plan single = PixelLayout.layout("甲", looseAdvance, profile(10, 14, 14));
        check(!single.overflow, "unused last advance does not create false overflow");
        eq(10, single.lines.get(0).layoutBounds.width(), "last ink not last advance");
        eq(20, single.lines.get(0).advance, "advance still available to adapter");
        eq(1, PixelLayout.layout("甲乙", looseAdvance, profile(30, 14, 14)).lines.size(),
            "nonfinal advances retained");
        eq(2, PixelLayout.layout("甲乙", looseAdvance, profile(29, 28, 14)).lines.size(),
            "nonfinal advance boundary -1");
    }

    private static void wordsAndPunctuation() {
        Plan mixed = plan("中文 ABC DEF中文", 38);
        eq("中文 ", lineText(mixed, 0), "prefer English word boundary");
        preserved(mixed);
        Plan word = plan("abcdefghij", 19);
        eq("abc", lineText(word, 0), "long English split without hyphen");
        preserved(word);
        for (Line line : word.lines) check(!lineText(word, line.index).contains("-"), "no hyphen inserted");
        Plan comma = plan("你好，世界。", 20);
        eq("你", lineText(comma, 0), "avoid leading comma");
        for (Line line : comma.lines)
            check(!"，。".contains(lineText(comma, line.index).substring(0, 1)), "no leading CJK punctuation");
        Plan opening = plan("你（世界）", 20);
        for (Line line : opening.lines) check(!lineText(opening, line.index).endsWith("（"), "no trailing opener");
        Plan forced = plan("（你", 10);
        check(has(forced, IssueKind.FORCED_BREAK), "impossible kinsoku reported");
        preserved(forced);
        Plan ellipsis = plan("甲……乙", 20);
        eq("……", lineText(ellipsis, 1), "ellipsis stays together");
        eq(1, ellipsis.lines.get(1).units.size(), "paired ellipsis atomic");
        Plan dots = plan("a...b", 12);
        check(has(dots, IssueKind.UNIT_TOO_WIDE), "oversized ASCII ellipsis reported");
        eq("...", lineText(dots, 1), "ASCII ellipsis never split");
        preserved(dots);
        Plan nbsp = plan("a\u00a0b", 12);
        check(has(nbsp, IssueKind.FORCED_BREAK), "NBSP only broken with explicit fallback");
    }

    private static void explicitBreaksAndSpaces() {
        Plan empty = plan("", 0);
        eq(1, empty.lines.size(), "empty text has one empty line");
        eq(0, empty.lines.get(0).display.start, "empty span start");
        eq(0, empty.lines.get(0).display.end, "empty span end");
        eq(0, empty.lines.get(0).glyphs.size(), "empty has no glyph");
        Plan breaks = plan("\n甲\r\n\r乙\u2028\u2029", 30);
        eq(6, breaks.lines.size(), "all explicit breaks and trailing line preserved");
        preserved(breaks);
        eq("甲\r\n", lineText(breaks, 1), "CRLF atomic, retained in preceding line");
        eq(0, breaks.lines.get(5).units.size(), "trailing line empty");
        Plan spaces = plan("  a  b ", 14);
        preserved(spaces);
        eq(7, spaces.text.length(), "all original spaces retained");
        Plan justSpaces = plan("    ", 8);
        eq(2, justSpaces.lines.size(), "spaces use width even without ink");
        check(justSpaces.inkBounds.empty, "spaces do not invent ink/effects");
    }

    private static void atomicText() {
        String[] atomic = {"\ud83d\ude00", "e\u0301", "a\u0301\u0327", "\ud83d\udc69\u200d\ud83d\udcbb",
            "\ud83d\udc4d\ud83c\udffd", "\ud83c\udde8\ud83c\uddf3", "\u1100\u1161\u11a8",
            "\u0915\u094d\u0937", "\u2764\ufe0f", "\u0600A", "……\u0301", "...\u0301"};
        for (String text : atomic) {
            Plan p = plan(text + "中", 1);
            eq(text, lineText(p, 0), "atomic cluster " + text);
            eq(1, p.lines.get(0).units.size(), "one cluster unit");
            check(has(p, IssueKind.UNIT_TOO_WIDE), "oversized cluster explicitly reported");
            for (int i = 0; i < text.length(); i++)
                eq(0, p.visiblePrefixes(i).get(0).glyphCount, "no half cluster reveal");
            check(p.visiblePrefixes(text.length()).get(0).glyphCount > 0, "cluster reveals together");
            preserved(p);
        }
        Plan flags = plan("\ud83c\udde8\ud83c\uddf3\ud83c\uddfa\ud83c\uddf8", 20);
        eq(2, flags.lines.size(), "regional indicators paired, not entire run");
    }

    private static void reveal() {
        Plan p = plan("甲e\u0301\ud83d\ude00，ABC\n乙", 26);
        int total = 0;
        List<PlacedGlyph> saved = new ArrayList<PlacedGlyph>();
        for (Line line : p.lines) { total += line.glyphs.size(); saved.addAll(line.glyphs); }
        int[] previousCounts = new int[p.lines.size()];
        for (int reveal = -1; reveal <= p.text.length() + 1; reveal++) {
            List<VisiblePrefix> visible = p.visiblePrefixes(reveal);
            for (int i = 0; i < visible.size(); i++) {
                VisiblePrefix prefix = visible.get(i);
                check(prefix.glyphCount >= previousCounts[i], "reveal monotonic");
                previousCounts[i] = prefix.glyphCount;
                for (int j = 0; j < prefix.glyphCount; j++)
                    check(prefix.glyphs.get(j) == p.lines.get(i).glyphs.get(j), "reveal reuses fixed glyph/origin");
                check(prefix.line == p.lines.get(i), "reveal reuses line plan");
            }
        }
        int visibleTotal = 0;
        for (VisiblePrefix prefix : p.visiblePrefixes(Integer.MAX_VALUE)) visibleTotal += prefix.glyphCount;
        eq(total, visibleTotal, "all glyphs eventually reveal");
        eq(0, p.visiblePrefixes(0).get(0).unitCount, "identity not visible at zero");
        eq(1, p.visiblePrefixes(1).get(0).unitCount, "identity reveals first UTF16 character");
        check(saved.size() == total, "full text measured once, not reveal fragments");
        final int[] calls = {0};
        Metrics counted = new Metrics() {
            public Glyph glyph(int cp) { calls[0]++; return TEN.glyph(cp); }
            public double kerning(int a, int b) { calls[0]++; return TEN.kerning(a, b); }
        };
        Plan measured = PixelLayout.layout(p.text, counted, profile(26, 1000, 14));
        int beforeReveal = calls[0];
        for (int i = 0; i <= p.text.length(); i++) measured.visiblePrefixes(i);
        eq(beforeReveal, calls[0], "reveal never remeasures glyphs or kerning");
    }

    private static void sourceMaps() {
        List<SourceRange> mapping = new ArrayList<SourceRange>(Arrays.asList(
            new SourceRange(0, 1, 0, 1), new SourceRange(1, 3, 1, 6), new SourceRange(3, 4, 6, 7)));
        Plan p = PixelLayout.layout("甲AB乙", TEN, profile(100, 14, 14), mapping);
        mapping.clear();
        eq(3, p.sourceRanges.size(), "source map defensive copy");
        eq(1, p.visiblePrefixes(5).get(0).unitCount, "expanded variable waits entire source interval");
        eq(3, p.visiblePrefixes(6).get(0).unitCount, "shared source interval reveals all expansion");
        eq(4, p.visiblePrefixes(7).get(0).unitCount, "source tail reveals");
        Plan contracted = PixelLayout.layout("甲", TEN, profile(10, 14, 14),
            Arrays.asList(new SourceRange(0, 1, 0, 20)));
        eq(0, contracted.visiblePrefixes(19).get(0).unitCount, "contraction source end");
        eq(1, contracted.visiblePrefixes(20).get(0).unitCount, "contraction revealed");
        Plan composed = PixelLayout.layout("e\u0301", TEN, profile(10, 14, 14),
            Arrays.asList(new SourceRange(0, 1, 0, 1), new SourceRange(1, 2, 1, 8)));
        eq(0, composed.visiblePrefixes(7).get(0).unitCount, "cluster unions all intersecting ranges");
        eq(1, composed.visiblePrefixes(8).get(0).unitCount, "cluster mapping end");
        Plan reversed = PixelLayout.layout("AB", TEN, profile(20, 14, 14),
            Arrays.asList(new SourceRange(0, 1, 5, 6), new SourceRange(1, 2, 0, 1)));
        eq(0, reversed.visiblePrefixes(2).get(0).unitCount, "nonmonotonic map never creates holes");
        eq(2, reversed.visiblePrefixes(6).get(0).unitCount, "nonmonotonic map eventually complete");
        Plan generated = PixelLayout.layout("AB", TEN, profile(20, 14, 14),
            Arrays.asList(new SourceRange(0, 2, 0, 0)));
        eq(2, generated.visiblePrefixes(0).get(0).unitCount, "zero-length source allows generated text");
        expectIllegal(new Runnable() { public void run() {
            PixelLayout.layout("AB", TEN, profile(20, 14, 14), Arrays.asList(new SourceRange(1, 2, 0, 1)));
        }}, "source gap rejected");
        expectIllegal(new Runnable() { public void run() {
            PixelLayout.layout("\ud83d\ude00", TEN, profile(20, 14, 14), Arrays.asList(
                new SourceRange(0, 1, 0, 1), new SourceRange(1, 2, 1, 2)));
        }}, "source display range cannot bisect surrogate");
    }

    private static void controlsAndInvalidInput() {
        Plan p = plan("A\t\u0001\u200eB", 12);
        eq(1, p.lines.size(), "controls zero width");
        eq(2, p.lines.get(0).glyphs.size(), "controls not passed to glyph draw");
        eq(3, count(p, IssueKind.CONTROL_CHARACTER), "controls visibly diagnosable");
        preserved(p);
        expectIllegal(new Runnable() { public void run() { plan("\ud800", 20); }}, "lone high surrogate rejected");
        expectIllegal(new Runnable() { public void run() { plan("\udc00", 20); }}, "lone low surrogate rejected");
        expectIllegal(new Runnable() { public void run() { new Glyph(-1, 0, 0, 1, 1); }}, "negative advance rejected");
        expectIllegal(new Runnable() { public void run() { profile(10, 10, 0); }}, "nonpositive step rejected");
        expectIllegal(new Runnable() { public void run() { profile(Double.NaN, 10, 1); }}, "NaN rejected");
        expectIllegal(new Runnable() { public void run() {
            PixelLayout.layout("A", new Metrics() {
                public Glyph glyph(int cp) { return null; }
                public double kerning(int a, int b) { return 0; }
            }, profile(10, 10, 14));
        }}, "missing glyph explicitly rejected");
        expectIllegal(new Runnable() { public void run() {
            PixelLayout.layout("AB", new Metrics() {
                public Glyph glyph(int cp) { return new Glyph(1, 0, 0, 1, 1); }
                public double kerning(int a, int b) { return Double.NaN; }
            }, profile(10, 10, 14));
        }}, "nonfinite kern rejected");
    }

    private static void overflow() {
        Plan narrow = PixelLayout.layout("中文ABC", TEN, profile(0, 0, 14));
        check(narrow.overflow, "zero dimensions return overflow");
        eq(5, narrow.lines.size(), "zero width always advances one atomic unit");
        eq(5, count(narrow, IssueKind.UNIT_TOO_WIDE), "every oversized unit reported");
        preserved(narrow);
        Plan tall = PixelLayout.layout("中文", TEN, profile(10, 13, 9));
        check(has(tall, IssueKind.LINE_TOO_HIGH), "ink exceeds row step reported");
        check(has(tall, IssueKind.HEIGHT_OVERFLOW), "excess rows retained, not truncated");
        eq(2, tall.lines.size(), "height does not truncate");
        Plan huge = plan("……", 1);
        eq(1, huge.lines.size(), "single overlarge unit finite");
        eq(2, huge.lines.get(0).glyphs.size(), "overlarge unit intact");
        check(has(huge, IssueKind.UNIT_TOO_WIDE), "overlarge unit diagnostic");
        check(!plan("", 0).overflow, "empty zero-width content is valid with height");
    }

    private static void immutableAndDeterministic() {
        final Plan p = plan("中文 ABC", 24);
        expectUnsupported(new Runnable() { public void run() { p.lines.clear(); }}, "immutable lines");
        expectUnsupported(new Runnable() { public void run() { p.lines.get(0).glyphs.clear(); }}, "immutable glyphs");
        expectUnsupported(new Runnable() { public void run() { p.lines.get(0).units.clear(); }}, "immutable units");
        expectUnsupported(new Runnable() { public void run() { p.issues.clear(); }}, "immutable issues");
        expectUnsupported(new Runnable() { public void run() { p.sourceRanges.clear(); }}, "immutable source map");
        expectUnsupported(new Runnable() { public void run() { p.visiblePrefixes(10).get(0).glyphs.clear(); }}, "immutable reveal");
        Plan q = plan(p.text, 24);
        eq(p.lines.size(), q.lines.size(), "same input line count");
        for (int i = 0; i < p.lines.size(); i++) {
            eq(lineText(p, i), lineText(q, i), "deterministic break");
            for (int j = 0; j < p.lines.get(i).glyphs.size(); j++) {
                eq(p.lines.get(i).glyphs.get(j).x, q.lines.get(i).glyphs.get(j).x, "deterministic x");
                eq(p.lines.get(i).glyphs.get(j).y, q.lines.get(i).glyphs.get(j).y, "deterministic y");
            }
        }
    }

    private static void exhaustiveSmallInputs() {
        String[] pieces = {"中", "a", " ", "，", "（", "\n", "e\u0301", "\ud83d\ude00"};
        for (String a : pieces) for (String b : pieces) for (String c : pieces) {
            for (int width : new int[] {0, 9, 10, 11, 19, 20, 21}) {
                Plan p = plan(a + b + c, width);
                preserved(p);
                int prior = 0;
                for (Line line : p.lines) {
                    check(line.display.start == prior, "line spans partition full display");
                    prior = line.display.end;
                    for (Unit unit : line.units) {
                        check(unit.display.end > unit.display.start, "every unit makes progress");
                        check(!Character.isLowSurrogate(p.text.charAt(unit.display.start)), "unit not inside pair");
                    }
                }
                eq(p.text.length(), prior, "last line ends at display end");
            }
        }
    }

    private static String lineText(Plan p, int line) {
        Span span = p.lines.get(line).display;
        return p.text.substring(span.start, span.end);
    }
    private static void preserved(Plan p) {
        StringBuilder reconstructed = new StringBuilder();
        for (Line line : p.lines) reconstructed.append(lineText(p, line.index));
        eq(p.text, reconstructed.toString(), "display unchanged, no truncation or insertion");
    }
    private static int count(Plan p, IssueKind kind) {
        int result = 0;
        for (Issue issue : p.issues) if (issue.kind == kind) result++;
        return result;
    }
    private static boolean has(Plan p, IssueKind kind) { return count(p, kind) != 0; }
    private static void expectIllegal(Runnable task, String message) {
        try { task.run(); } catch (IllegalArgumentException expected) { checks++; return; }
        throw new AssertionError(message);
    }
    private static void expectUnsupported(Runnable task, String message) {
        try { task.run(); } catch (UnsupportedOperationException expected) { checks++; return; }
        throw new AssertionError(message);
    }
    private static void check(boolean value, String message) {
        checks++;
        if (!value) throw new AssertionError(message);
    }
    private static void eq(int expected, int actual, String message) {
        check(expected == actual, message + ": expected " + expected + ", actual " + actual);
    }
    private static void eq(double expected, double actual, String message) {
        check(Math.abs(expected - actual) < 0.000001,
            message + ": expected " + expected + ", actual " + actual);
    }
    private static void eq(String expected, String actual, String message) {
        check(expected.equals(actual), message + ": expected [" + expected + "], actual [" + actual + "]");
    }
}
