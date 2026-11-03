import PRG.*;
import cosmoloc.layout.*;
import java.io.*;
import java.util.*;

/**
 * Offline scene render: drive the candidate's real layout classes and dump what
 * the player would actually see, page by page.
 *
 * This exists because the earlier batches verified wrap rules reimplemented in
 * Python, and got them wrong twice. Calling the shipped classes removes that
 * whole class of error: the rule being measured is the rule that runs.
 *
 * Usage:
 *   SceneRender <candidate.jar> <input.tsv> <out.json>
 *
 * Input TSV: one row per case, `key \t archive \t entry \t line \t body`
 * (body is the text without the speaker prefix; `\u2028` written as the two
 * characters `\u2028` are decoded here).
 *
 * Output JSON: per case, the pages the engine produces — grid, lines, pixel
 * width, and the break pairs between lines.
 */
@SuppressWarnings({"rawtypes", "unchecked"})
public final class SceneRender {
    static String unescape(String s) {
        return s.replace("\\u2028", "\u2028").replace("\\u2029", "\u2029")
                .replace("\\n", "\n").replace("\\t", "\t");
    }

    static aEO one(Object x) {
        return new aEg(x, (aEO) aFC.MODULE$);
    }

    static String q(String s) {
        StringBuilder b = new StringBuilder("\"");
        for (char c : s.toCharArray()) {
            switch (c) {
                case '"': b.append("\\\""); break;
                case '\\': b.append("\\\\"); break;
                case '\n': b.append("\\n"); break;
                case '\r': b.append("\\r"); break;
                case '\t': b.append("\\t"); break;
                case '\u2028': b.append("\\u2028"); break;
                case '\u2029': b.append("\\u2029"); break;
                default:
                    if (c < 0x20) b.append(String.format("\\u%04x", (int) c));
                    else b.append(c);
            }
        }
        return b.append('"').toString();
    }

    public static void main(String[] args) throws Exception {
        // The candidate jar is already first on the classpath, so the real
        // classes and fonts resolve straight out of it.
        List<String> keys = new ArrayList<>();
        List<String[]> rows = new ArrayList<>();
        try (BufferedReader r = new BufferedReader(new InputStreamReader(
                new FileInputStream(args[1]), "UTF-8"))) {
            String line;
            while ((line = r.readLine()) != null) {
                if (line.isEmpty() || line.startsWith("#")) continue;
                String[] f = line.split("\t", -1);
                if (f.length < 5) continue;
                keys.add(f[0] + "\t" + f[1] + "\t" + f[2] + "\t" + f[3]);
                rows.add(f);
            }
        }

        StringBuilder out = new StringBuilder("{\n");
        for (int i = 0; i < rows.size(); i++) {
            String[] f = rows.get(i);
            String body = unescape(f[4]);
            out.append("  ").append(q(keys.get(i))).append(": ");
            try {
                List<DialogueGrid.Page> pages = DialogueWrap.storyPages(body);
                out.append("{\"pages\": [");
                for (int p = 0; p < pages.size(); p++) {
                    DialogueGrid.Page page = pages.get(p);
                    if (p != 0) out.append(", ");
                    out.append("{\"grid\": ").append(q(page.grid));
                    out.append(", \"pixelWidth\": ").append(page.pixelWidth);
                    out.append(", \"lines\": [");
                    for (int l = 0; l < page.lines.size(); l++) {
                        if (l != 0) out.append(", ");
                        out.append(q(page.lines.get(l)));
                    }
                    out.append("], \"breaks\": [");
                    List<String> ls = page.lines;
                    boolean first = true;
                    for (int l = 0; l + 1 < ls.size(); l++) {
                        String a = ls.get(l), b = ls.get(l + 1);
                        if (a.isEmpty() || b.isEmpty()) continue;
                        if (!first) out.append(", ");
                        first = false;
                        out.append(q("" + a.charAt(a.length() - 1) + b.charAt(0)));
                    }
                    out.append("]}");
                }
                out.append("], \"ok\": true}");
            } catch (Throwable t) {
                out.append("{\"ok\": false, \"error\": ").append(q(t.toString())).append("}");
            }
            out.append(i + 1 < rows.size() ? ",\n" : "\n");
        }
        out.append("}\n");
        try (Writer w = new OutputStreamWriter(new FileOutputStream(args[2]), "UTF-8")) {
            w.write(out.toString());
        }
        System.out.println("rendered " + rows.size() + " cases");
    }
}
