import cosmoloc.layout.DialogueGrid;
import cosmoloc.layout.PixelLayout;
import java.util.List;

/** Pure CPU tests for the fixed-grid serializer; no game classes or user data. */
public final class DialogueGridTest {
    private static int checks;
    private static final PixelLayout.Metrics FONT = new PixelLayout.Metrics() {
        public PixelLayout.Glyph glyph(int cp) {
            int advance = Character.UnicodeScript.of(cp) == Character.UnicodeScript.HAN ? 10 : 8;
            return new PixelLayout.Glyph(advance, 0, 0, cp == ' ' ? 0 : advance, cp == ' ' ? 0 : 10);
        }
        public double kerning(int a, int b) { return a == 'A' && b == 'V' ? -1 : 0; }
    };
    private static void ok(boolean value, String message) {
        checks++; if (!value) throw new AssertionError(message);
    }
    private static void rejects(Runnable action) {
        boolean thrown = false;
        try { action.run(); } catch (IllegalArgumentException expected) { thrown = true; }
        ok(thrown, "invalid input must be explicit");
    }
    private static void check(String text, int q, int rows, int limit) {
        List<DialogueGrid.Page> pages = DialogueGrid.format(text, FONT, q, rows, limit * 10);
        StringBuilder recovered = new StringBuilder();
        for (DialogueGrid.Page page : pages) {
            ok(page.grid.length() == q * rows, "consumer shape");
            ok(page.lines.size() == rows, "logical row count");
            for (int row = 0; row < rows; row++) {
                String line = page.lines.get(row);
                ok(line.length() <= q, "UTF-16 bound");
                PixelLayout.Plan measured = PixelLayout.layout(line, FONT,
                    new PixelLayout.Profile(new PixelLayout.Rect(0, 0, limit * 10, 32), 16, PixelLayout.Insets.NONE));
                ok(!measured.overflow, "pixel bound");
                String serialized = page.grid.substring(row * q, (row + 1) * q);
                ok(serialized.startsWith(line), "row starts with full text");
                for (int at = line.length(); at < q; at++) ok(serialized.charAt(at) == ' ', "padding only");
                recovered.append(line);
            }
        }
        ok(recovered.toString().equals(text.replace("<p>", "").replace("\r\n", "").replace("\n", "").replace("\r", "").replace("\u2028", "").replace("\u2029", "")), "text/space conservation without new hyphens");
    }
    public static void main(String[] args) {
        String radio = "[就——是这样！卫星 R18 一直在把你的近场数据传回总部。]";
        String story = "一件我已经不怎么穿的衣服。它大概会刚——刚好合身！";
        check(radio, 20, 3, 15); check(story, 28, 3, 20);
        check("[如果你碰上任何新生物，尽管用频率27.850呼叫我。]", 20, 3, 15);
        check("很简单：你把在外头找到的那些花哨芯片带给我，我就替你黑开门！显然，这是双赢！", 28, 3, 20);
        check("如果 A VERY LONG ENGLISH WORD APPEARS 就按真实宽度排版。", 20, 3, 15);
        check("甲乙丙丁戊己庚辛壬癸甲乙丙丁戊。标点不被删除。", 20, 3, 15);
        check("  前面的空格和 中间 空格都保留。  ", 20, 3, 15);
        check("上一段<p>下一段", 28, 3, 20);
        check("第一行\n第二行\r\n第三行", 28, 3, 20);
        check("第一行\u2028第二行\u2029第三行", 28, 3, 20);
        check("", 28, 3, 20);
        for (int n = 1; n <= 200; n++) {
            StringBuilder text = new StringBuilder();
            for (int i = 0; i < n; i++) text.append("中文排版".charAt(i % 4));
            check(text.toString(), 20, 3, 15); check(text.toString(), 28, 3, 20);
        }
        ok(DialogueGrid.format("甲<p>乙", FONT, 28, 3, 200).size() == 2, "explicit paragraph remains a page boundary");
        ok(DialogueGrid.format("AV", FONT, 20, 3, 15).get(0).lines.get(0).equals("AV"), "kerning honored");
        rejects(() -> DialogueGrid.format("中文\t", FONT, 20, 3, 150));
        rejects(() -> DialogueGrid.format("中文", FONT, 0, 3, 150));
        rejects(() -> DialogueGrid.format("中文", FONT, 20, 3, Double.NaN));
        rejects(() -> DialogueGrid.format("中文", FONT, 20, 3, 5));
        rejects(() -> DialogueGrid.format("ABCD", FONT, 2, 3, 150));
        ok(DialogueGrid.hasHan(story), "Han detection"); ok(!DialogueGrid.hasHan("R18 27.850"), "non-Han detection");
        System.out.println("DIALOGUE_GRID_OK checks=" + checks);
    }
}
