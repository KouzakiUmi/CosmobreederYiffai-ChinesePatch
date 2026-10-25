package PRG;

import cosmoloc.layout.DialogueGrid;
import cosmoloc.layout.PixelLayout;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.*;
import java.util.regex.*;

/** Final-text adapter for JR/Nb only. No graphics, source joining or state mutation. */
public final class DialogueWrap {
    private DialogueWrap() { }
    public static final String FONT_SHA256 = "000c85594bb86de3402ab9c4dab3b50c0590051dbbe9b96a8d856acb7e983753";
    private static final String[] VARIABLES = {"@DerekChipReport", "@ZoneName", "@EmuButtons", "@BOYPC", "@GIRLPC"};

    @SuppressWarnings({"rawtypes", "unchecked"})
    public static aEO radio(aEO source, amq columns, amv rows, SA sa) {
        // Only the source-verified radio (Ob) and Continue/defeat (NY) callers
        // are supported. Unknown profiles retain the WHOLE old eager pipeline.
        if ((columns != Ob.MODULE$ && columns != NY.MODULE$) || rows != Om.MODULE$) {
            azz<Object, aCd<Object>> wrap = value -> {
                aAZ tuple = (aAZ)value;
                String full = ams.MODULE$.a((amr.h)tuple.a(), amr.i.MODULE$.a());
                return amw.MODULE$.a(full, columns, rows).v(page ->
                    new aAZ(new amr.d(((amr.d)page).a()), tuple.e(), tuple.f()));
            };
            azz<Object, Object> transform = value -> {
                aAZ page = (aAZ)value;
                return new aAZ(sa.d().apply(new amr.d(((amr.d)page.a()).a())), page.e(), page.f());
            };
            return source.w(wrap).v(transform);
        }
        int legacyColumns = columns == NY.MODULE$ ? 12 : 20;
        double pixelWidth = columns == NY.MODULE$ ? 80 : 150;
        List<Object> out = new ArrayList<Object>();
        for (aEO rest = source; !rest.b(); rest = (aEO)rest.E()) {
            aAZ tuple = (aAZ)rest.s();
            String full = ams.MODULE$.a((amr.h)tuple.a(), amr.i.MODULE$.a());
            if (!DialogueGrid.hasHan(full) && !hasVariable(full)) {
                appendLegacyRadio(out, tuple, full, columns, rows, sa);
                continue;
            }
            // SA is the actual game's replacement function, applied to the COMPLETE translated tuple.
            String finalText = sa.d().apply(new amr.d(full)).a();
            // Known substitutions must be measured even when their result is ASCII:
            // @DerekChipReport can expand to a long English report as well as CJK.
            for (DialogueGrid.Page page : pages(finalText, legacyColumns, pixelWidth, metrics()))
                out.add(new aAZ(new amr.d(legacyColumns == 12 ? continueGrid(page.grid) : page.grid), tuple.e(), tuple.f()));
        }
        return list(out);
    }

    /** Original amn completes at grid.trim().length(), not at rtrim(grid).length().
     * A wrapped page starting with a space would therefore hide its final ink.
     * Move only FIRST-ROW leading spaces into that same row's padding: retain
     * all ink, all 36 code units and all subsequent row positions. Never silently
     * collapse a deliberately blank leading row. */
    private static String continueGrid(String grid) {
        int leading = 0;
        while (leading < 12 && grid.charAt(leading) == ' ') leading++;
        if (leading == 0 || grid.trim().isEmpty()) return grid;
        if (leading == 12) throw new IllegalArgumentException("Continue page starts with a blank row; original amn cannot reveal it safely");
        StringBuilder fixed = new StringBuilder(36).append(grid.substring(leading, 12));
        for (int i = 0; i < leading; i++) fixed.append(' ');
        return fixed.append(grid.substring(12)).toString();
    }

    @SuppressWarnings({"rawtypes", "unchecked"})
    private static void appendLegacyRadio(List<Object> out, aAZ tuple, String full, amq q, amv h, SA sa) {
        aEO pages = amw.MODULE$.a(full, q, h);
        for (aEO rest = pages; !rest.b(); rest = (aEO)rest.E()) {
            String page = ((amr.d)rest.s()).a();
            out.add(new aAZ(sa.d().apply(new amr.d(page)), tuple.e(), tuple.f()));
        }
    }

    @SuppressWarnings({"rawtypes", "unchecked"})
    public static aEO story(aEO source) {
        List<Object> out = new ArrayList<Object>();
        for (aEO rest = source; !rest.b(); rest = (aEO)rest.E()) {
            aAJ tuple = (aAJ)rest.s();
            String full = ams.MODULE$.a((amr.h)tuple.a(), amr.i.MODULE$.a());
            if (!StoryFont12.uses12(full)) {
                aEO old = amw.MODULE$.a(full, Ol.MODULE$, Om.MODULE$);
                for (aEO restPage = old; !restPage.b(); restPage = (aEO)restPage.E())
                    out.add(new aAJ(restPage.s(), tuple.e()));
            } else {
                for (DialogueGrid.Page page : storyPages(full))
                    out.add(new aAJ(new amr.d(page.grid), tuple.e()));
            }
        }
        return list(out);
    }

    /** Story-only 12px profile. Keep the radio/Continue pages() implementation
     * byte-for-byte separate; original same-locale uppercase precedes layout. */
    public static List<DialogueGrid.Page> storyPages(String finalText) {
        Locale locale = Locale.getDefault();
        StringBuilder upper = new StringBuilder();
        String[] paragraphs = finalText.split("<p>", -1);
        for (int i = 0; i < paragraphs.length; i++) {
            if (i != 0) upper.append("<p>");
            String value = paragraphs[i].toUpperCase(locale);
            if (!value.equals(value.toUpperCase(locale)))
                throw new IllegalArgumentException("Dialogue uppercase is not idempotent");
            upper.append(value);
        }
        List<DialogueGrid.Page> result = DialogueGrid.formatCapped(upper.toString(), StoryFont12.metrics(), 28, 3, 240);
        for (DialogueGrid.Page page : result)
            if (!page.grid.equals(page.grid.toUpperCase(locale)))
                throw new IllegalArgumentException("Post-wrap uppercase would change the original grid");
        return result;
    }

    private static boolean hasVariable(String text) {
        for (String variable : VARIABLES) if (text.contains(variable)) return true;
        return false;
    }

    /** Mirrors the consumers' default-locale uppercase, before measuring. The old <p>
     * delimiter is formatter syntax, not display text, so uppercase each paragraph separately. */
    public static List<DialogueGrid.Page> pages(String finalText, int q, double width, PixelLayout.Metrics metrics) {
        Locale locale = Locale.getDefault();
        StringBuilder upper = new StringBuilder();
        String[] paragraphs = finalText.split("<p>", -1);
        for (int i = 0; i < paragraphs.length; i++) {
            if (i != 0) upper.append("<p>");
            String value = paragraphs[i].toUpperCase(locale);
            if (!value.equals(value.toUpperCase(locale)))
                throw new IllegalArgumentException("Dialogue uppercase is not idempotent");
            upper.append(value);
        }
        List<DialogueGrid.Page> result = DialogueGrid.format(upper.toString(), metrics, q, 3, width);
        for (DialogueGrid.Page page : result)
            if (!page.grid.equals(page.grid.toUpperCase(locale)))
                throw new IllegalArgumentException("Post-wrap uppercase would change the original grid");
        return result;
    }

    @SuppressWarnings({"rawtypes", "unchecked"})
    private static aEO list(List<Object> values) {
        aEO out = aFC.MODULE$;
        for (int i = values.size() - 1; i >= 0; i--) out = new aEg(values.get(i), out);
        return out;
    }

    private static final class FontHolder {
        static final PixelLayout.Metrics VALUE = loadResource();
    }
    private static PixelLayout.Metrics metrics() { return FontHolder.VALUE; }
    private static PixelLayout.Metrics loadResource() {
        try (InputStream input = DialogueWrap.class.getResourceAsStream("/bbc2.fnt")) {
            if (input == null) throw new IOException("Missing pinned /bbc2.fnt");
            return readMetrics(input);
        } catch (IOException e) { throw new IllegalStateException("Dialogue font unavailable", e); }
    }

    /** Offline metrics injection for fixtures; production only reads the pinned JAR resource. */
    public static PixelLayout.Metrics readMetrics(InputStream input) throws IOException {
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        byte[] buffer = new byte[8192];
        for (int n; (n = input.read(buffer)) != -1;) bytes.write(buffer, 0, n);
        byte[] raw = bytes.toByteArray();
        try {
            StringBuilder hash = new StringBuilder();
            for (byte b : MessageDigest.getInstance("SHA-256").digest(raw)) hash.append(String.format("%02x", b & 255));
            if (!FONT_SHA256.equals(hash.toString())) throw new IOException("Unpinned dialogue font SHA256");
        } catch (java.security.NoSuchAlgorithmException e) { throw new AssertionError(e); }
        final Map<Integer, PixelLayout.Glyph> glyphs = new HashMap<Integer, PixelLayout.Glyph>();
        final Map<Long, Integer> kern = new HashMap<Long, Integer>();
        int declared = -1, declaredKern = 0;
        boolean size10 = false;
        for (String line : new String(raw, StandardCharsets.UTF_8).split("\\r?\\n")) {
            Map<String, Integer> fields = fields(line);
            if (line.startsWith("info ")) size10 = number(fields, "size") == 10;
            else if (line.startsWith("chars ")) declared = number(fields, "count");
            else if (line.startsWith("kernings ")) declaredKern = number(fields, "count");
            else if (line.startsWith("char ")) {
                int id = number(fields, "id");
                PixelLayout.Glyph glyph = new PixelLayout.Glyph(number(fields, "xadvance"), number(fields, "xoffset"),
                    number(fields, "yoffset"), number(fields, "width"), number(fields, "height"));
                if (glyphs.put(id, glyph) != null) throw new IOException("Duplicate glyph " + id);
            } else if (line.startsWith("kerning ")) {
                long pair = pair(number(fields, "first"), number(fields, "second"));
                if (kern.put(pair, number(fields, "amount")) != null) throw new IOException("Duplicate kerning");
            }
        }
        if (!size10 || declared != glyphs.size() || declaredKern != kern.size()
            || !glyphs.containsKey(32) || glyphs.get(32).xAdvance != 8)
            throw new IOException("Invalid pinned 10px BMFont metrics");
        return new PixelLayout.Metrics() {
            public PixelLayout.Glyph glyph(int cp) {
                PixelLayout.Glyph glyph = glyphs.get(cp);
                if (glyph == null) throw new IllegalArgumentException("Missing dialogue glyph U+" + Integer.toHexString(cp));
                return glyph;
            }
            public double kerning(int left, int right) {
                Integer amount = kern.get(pair(left, right));
                return amount == null ? 0 : amount;
            }
        };
    }
    private static long pair(int first, int second) { return ((long)first << 32) | (second & 0xffffffffL); }
    private static final Pattern NUMBER = Pattern.compile("(?:^|\\s)([A-Za-z]+)=(-?\\d+)(?=\\s|$)");
    private static Map<String, Integer> fields(String line) {
        Map<String, Integer> out = new HashMap<String, Integer>();
        Matcher matcher = NUMBER.matcher(line);
        while (matcher.find()) out.put(matcher.group(1), Integer.valueOf(matcher.group(2)));
        return out;
    }
    private static int number(Map<String, Integer> fields, String key) throws IOException {
        Integer value = fields.get(key);
        if (value == null) throw new IOException("Missing BMFont field " + key);
        return value;
    }
}
