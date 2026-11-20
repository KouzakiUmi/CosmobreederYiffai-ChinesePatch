import PRG.*;
import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/**
 * Regression for the all.ds (datadf/1 & datadm/1) parser acceptance.
 *
 * <p>The game loads datadf/1 and datadm/1 as {@code all.ds} and parses them with
 * {@code PRG.afF} (Scala FastParse CubeDSParser). Its dialogue-content rule is
 * {@code PRG.afH.i(auN)}; that rule accepts ASCII/CJK/punctuation but returns a
 * {@code Parsed.Failure} (Parsed.Failure) the moment it meets U+2028. This test
 * feeds every dialogue line of the BUILT payload through the REAL parser rule
 * using the REAL FastParse run harness ({@code PRG.auL} + {@code PRG.ava}) and the
 * REAL {@code PRG.afF.c(String)} ParserInput converter, i.e. the same machinery
 * the game's afF pipeline uses, then asserts 100% success.
 *
 * <p>Note: constructing a full {@code PRG.afF} instance standalone requires the
 * game's dependency-injection/global bootstrap (SO/SQ and adE/adu are null outside
 * the running game), so the test drives the exact character-level dialogue rule
 * afF delegates to, over the complete corpus. It also proves the mechanism: a
 * U+2028 line must FAIL and the on-disk sentinel U+2502 must PASS.
 *
 * args: candidateJar datadf.txt datadm.txt pakDatadf.txt pakDatadm.txt
 */
public final class DsParseTest {
    private static final char SENTINEL = '\u2502';
    private static final char SOFT_BREAK = '\u2028';

    private static Method cStr;
    private static Method afhI;
    static {
        try {
            cStr = afF.class.getMethod("c", String.class);
            cStr.setAccessible(true);
            afhI = afH.MODULE$.getClass().getMethod("i", auN.class);
            afhI.setAccessible(true);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    static final class Conv implements azz<String, auI> {
        public auI apply(String s) {
            try { return (auI) cStr.invoke(null, s); }
            catch (Exception e) { throw new RuntimeException(e); }
        }
    }
    static final class Parser implements azz<auN, auN> {
        public auN apply(auN r) {
            try { return (auN) afhI.invoke(afH.MODULE$, r); }
            catch (Exception e) { throw new RuntimeException(e); }
        }
    }

    /** Run the real afH dialogue rule over `s`; return consumed index or -1 on failure. */
    static int consumed(String s) {
        auK k = auL.MODULE$.a((Object) s, (azz) new Conv());
        auG g = ava.MODULE$.a((auK) k, (azz) new Parser(),
                (boolean) ava.MODULE$.<Object>a(), (int) ava.MODULE$.<Object>b(),
                (auT) ava.MODULE$.<Object>c());
        String cn = g.getClass().getName();
        if (cn.endsWith("auG$d")) {
            try {
                Method f = g.getClass().getMethod("f");
                return ((Integer) f.invoke(g)).intValue();
            } catch (Exception e) { throw new RuntimeException(e); }
        }
        return -1;
    }

    static String rtrim(String s) {
        int end = s.length();
        while (end > 0 && s.charAt(end - 1) == ' ') end--;
        return s.substring(0, end);
    }

    // Mirrors tools/lib/editorial_repairs.py _line_role(..., "ds"): dialogue
    // content is either a '*'-prefixed line or a "Speaker: ..." line; structural
    // lines (<header>, #comment, include/if/else/do, braces) are skipped.
    private static final java.util.regex.Pattern NON_DIALOGUE =
            java.util.regex.Pattern.compile("^\\s*(?:<|#|include\\b|if\\b|else\\b|do\\b|[{}]).*$", java.util.regex.Pattern.DOTALL);
    private static final java.util.regex.Pattern STAR =
            java.util.regex.Pattern.compile("^\\s*\\*\\s?(.*)$", java.util.regex.Pattern.DOTALL);
    private static final java.util.regex.Pattern SPEAKER =
            java.util.regex.Pattern.compile("^\\s*([^<>{}#*\\s][^:]{0,40}):\\s?(.*)$", java.util.regex.Pattern.DOTALL);

    static String bodyOf(String line) {
        if (NON_DIALOGUE.matcher(line).matches()) return null;
        java.util.regex.Matcher m = STAR.matcher(line);
        if (m.matches()) return m.group(1);
        m = SPEAKER.matcher(line);
        if (m.matches()) return m.group(2);
        return null;
    }

    static int failures = 0;

    static void check(boolean ok, String msg) {
        if (!ok) { failures++; System.out.println("FAIL: " + msg); }
    }

    static void verifyFile(String label, String text) {
        check(text.indexOf(SOFT_BREAK) < 0, label + ": still contains U+2028 (Parsed.Failure cause)");
        check(text.indexOf('\u2029') < 0, label + ": still contains U+2029");
        check(text.indexOf('\u0085') < 0, label + ": still contains U+0085");
        int lines = 0, parsed = 0, bad = 0, breaks = 0, sentinelLines = 0, firstBad = -1;
        String[] split = text.split("\n", -1);
        for (int i = 0; i < split.length; i++) {
            String line = split[i];
            if (line.endsWith("\r")) line = line.substring(0, line.length() - 1);
            if (line.indexOf(SENTINEL) >= 0) sentinelLines++;
            breaks += countChar(line, SENTINEL);
            String trimmed = line.trim();
            if (trimmed.startsWith("<") && trimmed.endsWith(">") && trimmed.length() > 2) continue;
            String body = bodyOf(line);
            if (body == null) continue; // not a dialogue content line
            lines++;
            String content = rtrim(body);
            int got = consumed(body);
            if (got < 0 || got < content.length()) {
                bad++;
                if (firstBad < 0) firstBad = i + 1;
            } else parsed++;
        }
        System.out.println(label + ": dialogueLines=" + lines + " parsed=" + parsed
                + " bad=" + bad + " sentinelSoftBreaks=" + breaks + " sentinelLines=" + sentinelLines);
        check(lines > 0, label + ": no dialogue lines found");
        check(bad == 0, label + ": " + bad + " dialogue lines rejected by real afH rule (first at line " + firstBad + ")");
    }

    static int countChar(String s, char c) {
        int n = 0;
        for (int i = 0; i < s.length(); i++) if (s.charAt(i) == c) n++;
        return n;
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 5) throw new IllegalArgumentException("usage: DsParseTest candidateJar datadf datadm pakDatadf pakDatadm");
        String candidateJar = args[0];
        // Mechanism proof against the real rule:
        int okAscii = consumed("  * Hello there, traveler!");
        check(okAscii == "  * Hello there, traveler!".length(), "real afH rule must accept plain dialogue");
        int cjk = consumed("  * 我这儿有些好东西，给你个好价钱。");
        check(cjk == "  * 我这儿有些好东西，给你个好价钱。".length(), "real afH rule must accept CJK dialogue");
        String poisoned = "  * before" + SOFT_BREAK + "after";
        check(consumed(poisoned) < 0 || consumed(poisoned) < poisoned.length(),
                "real afH rule must REJECT U+2028 (mechanism under test)");
        String safe = "  * before" + SENTINEL + "after";
        check(consumed(safe) == safe.length(), "real afH rule must ACCEPT the U+2502 sentinel");
        System.out.println("mechanism: U+2028 rejected, U+2502 accepted, plain/CJK accepted");

        for (int i = 1; i < args.length && i < 5; i++) {
            String text = new String(Files.readAllBytes(Paths.get(args[i])), StandardCharsets.UTF_8);
            verifyFile(Paths.get(args[i]).getFileName().toString(), text);
            if (i == 1) check(text.indexOf("Area0_Macsen1.Hello") >= 0, "expected scenario Area0_Macsen1.Hello missing");
        }

        // The candidate jar must actually carry the sealed entries we tested.
        // (Presence sanity via zip entry names belongs to the Python build; here we
        // only require the parser classes are the real game classes.)
        Class.forName("PRG.afF");
        Class.forName("PRG.afH");

        if (failures != 0) throw new IllegalStateException("DsParseTest failures: " + failures);
        System.out.println("PASS DsParseTest: all datadf/datadm dialogue lines parse with the real afH rule; no U+2028");
    }
}
