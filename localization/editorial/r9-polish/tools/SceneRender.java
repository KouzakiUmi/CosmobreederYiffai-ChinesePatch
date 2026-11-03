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
 * Both containers are covered, because a row's container depends on its call
 * site and they differ substantially:
 *
 *   story   PRG/Nb -> DialogueWrap.story -> storyPages  (story12, 240px, 20 Han)
 *   radio   PRG/JR -> DialogueWrap.radio -> pages       (bbc2,   150px, 15 Han)
 *
 * Usage:
 *   SceneRender <candidate.jar> <input.tsv> <out.json>
 *
 * Input TSV: `key \t container \t archive \t entry \t line \t body`
 * container is `story` or `radio`. `\u2028` and `\n` are decoded here.
 *
 * Output JSON: per case, the pages the engine produces — grid, lines, the
 * measured pixel width, and the break pairs between lines.
 */
@SuppressWarnings({"rawtypes", "unchecked"})
public final class SceneRender {
    static PixelLayout.Metrics radioMetrics;

    static String unescape(String s) {
        return s.replace("\\u2028", "\u2028").replace("\\u2029", "\u2029")
                .replace("\\n", "\n").replace("\\t", "\t");
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

    static void emit(StringBuilder out, List<DialogueGrid.Page> pages, String container,
                     double budget) throws IOException {
        out.append("{\"container\": ").append(q(container));
        out.append(", \"budget\": ").append(budget);
        out.append(", \"pages\": [");
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
    }

    public static void main(String[] args) throws Exception {
        try (InputStream in = SceneRender.class.getResourceAsStream("/bbc2.fnt")) {
            if (in == null) throw new IllegalStateException("Missing /bbc2.fnt");
            radioMetrics = DialogueWrap.readMetrics(in);
        }
        List<String[]> rows = new ArrayList<>();
        try (BufferedReader r = new BufferedReader(new InputStreamReader(
                new FileInputStream(args[1]), "UTF-8"))) {
            String line;
            while ((line = r.readLine()) != null) {
                if (line.isEmpty() || line.startsWith("#")) continue;
                String[] f = line.split("\t", -1);
                if (f.length < 6) continue;
                rows.add(f);
            }
        }

        StringBuilder out = new StringBuilder("{\n");
        for (int i = 0; i < rows.size(); i++) {
            String[] f = rows.get(i);
            String container = f[1];
            String body = unescape(f[5]);
            out.append("  ").append(q(f[0] + "\t" + container + "\t" + f[2] + "\t" + f[3])).append(": ");
            try {
                if (container.equals("story")) {
                    emit(out, DialogueWrap.storyPages(body), "story", 240.0);
                } else if (container.equals("radio")) {
                    emit(out, DialogueWrap.pages(body, 20, 150.0, radioMetrics), "radio", 150.0);
                } else if (container.equals("subtitle")) {
                    // VSN `text:` lines go through SubtitleLayout, width 240.
                    emit(out, SubtitleLayout.pages(body, 240), "subtitle", 240.0);
                } else {
                    throw new IllegalArgumentException("unknown container " + container);
                }
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
