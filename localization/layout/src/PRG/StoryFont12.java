package PRG;

import cosmoloc.layout.PixelLayout;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** Entry-local story12. Borrows the original Yq bbc2 atlas texture, never owns or
 * scales a texture/font. Original default/classic/dingbats maps remain untouched.
 * Font source: pinned official Fusion Pixel12 native BDF; ASCII records/pixels
 * and baseline/padding are copied unchanged from default10 to stabilize masks.
 */
public final class StoryFont12 {
    public static final String ROLE = "story12";
    public static final String FONT_SHA256 = "972d49918484e3e5521a7da58dbe94f6c6c604e4f486844b75f5b3be87fa2546";
    public static final int LINE_WIDTH = 240, LINE_HEIGHT = 16;
    private StoryFont12() { }

    /** Uses the COMPLETE page/caption, not its current animation mask/line.
     * Range contract matches build_story_font12.wide for the sealed corpus.
     * Independent Chinese quotes/dashes/ellipsis select12 even without Han.
     */
    public static boolean uses12(String fullCaption) {
        if (fullCaption == null) throw new NullPointerException("full story page");
        for (int i = 0; i < fullCaption.length(); i++) if (wide(fullCaption.charAt(i))) return true;
        return false;
    }
    private static boolean wide(int cp) {
        return cp == 0xb7 || cp == 0x2014 || cp == 0x2018 || cp == 0x2019
            || cp == 0x201c || cp == 0x201d || cp == 0x2026
            || (cp >= 0x1100 && cp <= 0x115f) || cp == 0x2329 || cp == 0x232a
            || (cp >= 0x2e80 && cp <= 0xa4cf) || (cp >= 0xac00 && cp <= 0xd7a3)
            || (cp >= 0xf900 && cp <= 0xfaff) || (cp >= 0xfe10 && cp <= 0xfe19)
            || (cp >= 0xfe30 && cp <= 0xfe6f) || (cp >= 0xff01 && cp <= 0xff60)
            || (cp >= 0xffe0 && cp <= 0xffe6);
    }
    private static final class Font {
        static final PixelLayout.Metrics METRICS = load();
        static PixelLayout.Metrics load() {
            try (InputStream input = StoryFont12.class.getResourceAsStream("/story12.fnt")) {
                if (input == null) throw new IOException("Missing pinned /story12.fnt");
                return readMetrics(input);
            } catch (IOException e) { throw new IllegalStateException("Story12 metrics unavailable", e); }
        }
    }
    public static PixelLayout.Metrics metrics() { return Font.METRICS; }

    /** Called once per original Yq resource owner at the end of Yg's actual
     * (ars,Ym,Yq) constructor. Many Yg instances may share it. Existing role
     * re-entry validates, but does NOT allocate/replace. Like iF's three fonts,
     * arp(file, existingRegion, false) has ownsTexture=false: original atlas
     * lifecycle owns all pixels, with no extra GL shutdown/disposal framework.
     */
    public static synchronized void register(Yq resources) {
        metrics(); // SHA-check root FNT before any allocation or map mutation.
        if (resources.f().e(ROLE).h()) {
            validate(((Yq.b)resources.f().apply(ROLE)).a());
            return;
        }
        aqX handle = apQ.e.b("story12.fnt");
        // Internal FileHandle may prefer a loose file over a JAR resource.
        // Seal the bytes ACTUALLY consumed by arp, not just the metrics copy.
        try (InputStream input = handle.e()) { readMetrics(input); }
        catch (IOException e) { throw new IllegalStateException("Unsealed story12 FileHandle", e); }
        arp font = new arp(handle, resources.i("bbc2"), false);
        validate(font);
        resources.a(ROLE, font, LINE_HEIGHT);
    }
    private static void validate(arp font) {
        arp.b han = font.a.a('\u4e2d');
        if (font.a.o != 1 || font.a.p != 1 || font.a.q || font.a.i != LINE_HEIGHT
                || han == null || han.d != 12 || han.e != 12 || han.l != 12
                || font.a.a('A') == null || font.a.a('A').l != 8)
            throw new IllegalStateException("story12 requires sealed unscaled native12/CJK + original8/ASCII");
    }

    /** Stack-compatible local replacement of the jo/Na Id boolean overload.
     * Dingbats and ASCII-only WHOLE pages use the exact original role/anchor.
     * Even an all-space current mask uses12/x8 if its full page is Chinese.
     */
    public static void drawSubtitle(Id original, SN sn, boolean pattern, String maskedLine,
                                    int x, int y, String fullPage) {
        draw(original, sn, pattern, maskedLine, x, y, fullPage);
    }
    public static void drawStory(Id original, SN sn, boolean pattern, String maskedLine,
                                 int x, int y, String fullPage) {
        draw(original, sn, pattern, maskedLine, x, y, fullPage);
    }
    private static void draw(Id original, SN sn, boolean pattern, String maskedLine,
                              int x, int y, String fullPage) {
        if (pattern || !uses12(fullPage)) { original.a(sn, pattern, maskedLine, x, y); return; }
        // Grid padding is not visible ink; do not count its trailing spaces as
        // another64px after an exactly20-Han row. Interior mask spaces stay8px.
        int end = maskedLine.length(); while (end > 0 && maskedLine.charAt(end-1) == ' ') end--;
        int width = 0;
        PixelLayout.Metrics font = metrics();
        for (int i = 0; i < end; i++) width += (int)font.glyph(maskedLine.charAt(i)).xAdvance;
        if (width > LINE_WIDTH) throw new IllegalArgumentException("story12 line exceeds240px: " + maskedLine);
        sn.a(maskedLine, Math.subtractExact(x, 8), y, ROLE);
    }

    /** CPU/test parser and production lazy loader share the SAME SHA/size gate. */
    public static PixelLayout.Metrics readMetrics(InputStream input) throws IOException {
        ByteArrayOutputStream output = new ByteArrayOutputStream(); byte[] buffer = new byte[8192];
        for (int count; (count = input.read(buffer)) >= 0;) output.write(buffer, 0, count);
        byte[] raw = output.toByteArray();
        try {
            StringBuilder sha = new StringBuilder();
            for (byte b : MessageDigest.getInstance("SHA-256").digest(raw)) sha.append(String.format("%02x", b & 255));
            if (!FONT_SHA256.equals(sha.toString())) throw new IOException("Unpinned story12 FNT SHA");
        } catch (java.security.NoSuchAlgorithmException e) { throw new AssertionError(e); }
        Map<Integer,PixelLayout.Glyph> glyphs = new HashMap<Integer,PixelLayout.Glyph>();
        boolean size = false, common = false; int declared = -1;
        for (String line : new String(raw,StandardCharsets.UTF_8).split("\\r?\\n")) {
            Map<String,Integer> fields = fields(line);
            if (line.startsWith("info ")) size = number(fields,"size") == 12;
            else if (line.startsWith("common ")) common = number(fields,"lineHeight") == 16 && number(fields,"base") == 8
                    && number(fields,"pages") == 1 && number(fields,"scaleW") == 2048 && number(fields,"scaleH") == 2048;
            else if (line.startsWith("chars ")) declared = number(fields,"count");
            else if (line.startsWith("kernings ") && number(fields,"count") != 0) throw new IOException("Unexpected story kerning");
            else if (line.startsWith("char ")) {
                int cp=number(fields,"id"), advance=number(fields,"xadvance"), width=number(fields,"width"), height=number(fields,"height");
                if (wide(cp) && (advance!=12 || width!=12 || height!=12)) throw new IOException("Not a real12 glyph U+"+Integer.toHexString(cp));
                if (cp>=32 && cp<127 && advance!=8) throw new IOException("ASCII advance drift");
                PixelLayout.Glyph glyph = new PixelLayout.Glyph(advance,number(fields,"xoffset"),number(fields,"yoffset"),width,height);
                if (glyphs.put(cp,glyph)!=null) throw new IOException("Duplicate story glyph");
            }
        }
        if (!size || !common || declared != glyphs.size() || !glyphs.containsKey(0x4e2d)) throw new IOException("Invalid sealed story12 metrics");
        return new Metrics(glyphs);
    }
    private static final class Metrics implements PixelLayout.Metrics {
        private final Map<Integer,PixelLayout.Glyph> glyphs;
        Metrics(Map<Integer,PixelLayout.Glyph> glyphs) { this.glyphs = glyphs; }
        public PixelLayout.Glyph glyph(int cp) {
            PixelLayout.Glyph value = glyphs.get(cp);
            if (value == null) throw new IllegalArgumentException("Missing story12 glyph U+"+Integer.toHexString(cp));
            return value;
        }
        public double kerning(int left, int right) { return 0; }
    }
    private static final Pattern NUMBER = Pattern.compile("(?:^|\\s)([A-Za-z]+)=(-?\\d+)(?=\\s|$)");
    private static Map<String,Integer> fields(String line) {
        Map<String,Integer> out = new HashMap<String,Integer>(); Matcher matcher = NUMBER.matcher(line);
        while (matcher.find()) out.put(matcher.group(1),Integer.valueOf(matcher.group(2)));
        return out;
    }
    private static int number(Map<String,Integer> values,String key) throws IOException {
        Integer value = values.get(key); if(value==null) throw new IOException("Missing story FNT "+key); return value;
    }
}
