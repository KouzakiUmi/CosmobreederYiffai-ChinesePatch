import PRG.SaveMenuLayout;
import cosmoloc.layout.PixelLayout;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.zip.ZipFile;
import jdk.internal.org.objectweb.asm.ClassReader;
import jdk.internal.org.objectweb.asm.tree.*;

/** Pure field/layout tests plus original-class ASM shape checks; no game startup. */
public final class SaveMenuLayoutTest {
    private static int passed;
    private static void check(boolean ok, String label) {
        if (!ok) throw new AssertionError(label);
        passed++;
    }
    private static final PixelLayout.Metrics METRICS = new PixelLayout.Metrics() {
        public PixelLayout.Glyph glyph(int cp) {
            int advance = cp >= 0x3000 ? 10 : 8;
            return new PixelLayout.Glyph(advance, 0, 0, cp == 32 ? 0 : advance, cp == 32 ? 0 : 10);
        }
        public double kerning(int a, int b) { return 0; }
    };
    private static void reject(Runnable action, String label) {
        boolean rejected = false;
        try { action.run(); } catch (IllegalArgumentException | IllegalStateException expected) { rejected = true; }
        check(rejected, label);
    }
    public static void main(String[] args) throws Exception {
        if (args.length == 1 && args[0].equals("--property-probe")) {
            check(SaveMenuLayout.prototypeEnabled(), "JVM property activates candidate");
            SaveMenuLayout.validateGeometry();
            SaveMenuLayout.disablePrototype();
            check(!SaveMenuLayout.prototypeEnabled(), "API overrides the startup property");
            System.out.println("SaveMenuLayoutTest property PASS " + passed + "; G3 blocked");
            return;
        }
        check(!SaveMenuLayout.prototypeEnabled(), "prototype disabled by default");
        SaveMenuLayout.begin(null, null); // Disabled begin performs no renderer/scene access.
        SaveMenuLayout.end();
        check(true, "disabled begin never clears or draws the background");
        SaveMenuLayout.configurePrototype();
        check(SaveMenuLayout.prototypeEnabled(), "explicit prototype opt-in");
        SaveMenuLayout.disablePrototype();
        check(!SaveMenuLayout.prototypeEnabled(), "prototype can be disabled");
        SaveMenuLayout.validateGeometry();
        check(true, "all field/icon/cursor rectangles stay in the registered candidate panel");
        reject(() -> SaveMenuLayout.requireCandidateRect(249, 104, 2, 8), "right panel boundary");
        reject(() -> SaveMenuLayout.requireCandidateRect(24, 103, 8, 8), "lower panel boundary");
        PixelLayout.Metrics offsets = new PixelLayout.Metrics() {
            public PixelLayout.Glyph glyph(int cp) { return new PixelLayout.Glyph(8, -1, -10, 9, 10); }
            public double kerning(int a, int b) { return 0; }
        };
        PixelLayout.Plan offsetPlan = SaveMenuLayout.planField("AB", offsets, 20);
        check(offsetPlan.lines.get(0).originX == 1 && offsetPlan.lines.get(0).originY == 10,
                "measured plan pen offsets are retained for draw conversion");
        check(offsetPlan.effectBounds.left == 0 && offsetPlan.effectBounds.top == 0,
                "translated field bounds are measured at the translated pen");
        String name = "中文名字测试八字";
        String first = name + "  LVL123 TRY999 ABCD";
        String second = "          测试地点     050% 1234";
        String[] fields = SaveMenuLayout.fields(name, first, second);
        check(fields[0].equals(name), "full eight-CJK name");
        check(fields[1].equals("LVL123 TRY999"), "numeric metadata unchanged");
        check(fields[2].equals("测试地点     050%"), "area and percentage preserved");
        check(fields[3].equals("ABCD1234"), "both original hexadecimal halves preserved");
        SaveMenuLayout.requireSingleLine(fields[0], METRICS, 84);
        SaveMenuLayout.requireSingleLine(fields[1] + " " + fields[3], METRICS, 224);
        SaveMenuLayout.requireSingleLine(fields[2], METRICS, 224);
        check(true, "representative four-line fields fit synthetic 10/8px metrics");
        SaveMenuLayout.requireSingleLine("中中中中中中中中", METRICS, 80);
        reject(() -> SaveMenuLayout.requireSingleLine("中中中中中中中中", METRICS, 79), "minus-one width overflow");
        reject(() -> SaveMenuLayout.fields(name, first.replace("TRY999", "TRYxxx"), second), "format drift rejected");
        reject(() -> SaveMenuLayout.fields(name, first, second.replace("1234", "1Z34")), "hex drift rejected");
        reject(() -> SaveMenuLayout.fields("别的名字", first, second), "name-prefix identity checked");
        String longName = "中中中中中中中中中";
        String[] longFields = SaveMenuLayout.fields(longName, "中中中中中中中中  LVL123 TRY999 ABCD", second);
        check(longFields[0].equals(longName), "out-of-rule stored name never truncated");
        reject(() -> SaveMenuLayout.requireSingleLine(longFields[0], METRICS, 84), "long stored name explicit overflow");
        reject(() -> SaveMenuLayout.requireSingleLine("中中中中中中中中中中中中中中中中中中中中中中中", METRICS, 224),
                "long location explicit overflow");
        check(SaveMenuLayout.slotId(new Object()) == -1, "non-slot index is not slot identity");
        check(SaveMenuLayout.TOP - 3 * SaveMenuLayout.STEP == 132, "fourth original SN anchor");
        check(132 - 8 >= SaveMenuLayout.PANEL_Y && 132 <= 146 - 14,
                "symbol row does not overlap preceding full line box");
        if (args.length != 1) throw new IllegalArgumentException("Pass original JAR for ASM shape tests");
        Map<String,ClassNode> nodes = new LinkedHashMap<String,ClassNode>();
        try (ZipFile zip = new ZipFile(args[0])) {
            for (String nameClass : new String[] {"Mf", "LY", "LX", "Iu"}) {
                String key = "PRG/" + nameClass;
                ClassNode node = new ClassNode();
                new ClassReader(zip.getInputStream(zip.getEntry(key + ".class"))).accept(node, 0);
                nodes.put(key, node);
            }
        }
        int methodsBefore = 0;
        for (ClassNode node : nodes.values()) methodsBefore += node.methods.size();
        SaveMenuPatch.apply(nodes);
        int methodsAfter = 0, calls = 0, cursorCalls = 0, ends = 0;
        for (ClassNode node : nodes.values()) {
            methodsAfter += node.methods.size();
            for (MethodNode method : node.methods) for (AbstractInsnNode insn : method.instructions.toArray())
                if (insn instanceof MethodInsnNode && ((MethodInsnNode)insn).owner.equals("PRG/SaveMenuLayout")) {
                    calls++;
                    if (((MethodInsnNode)insn).name.equals("cursor")) cursorCalls++;
                    if (((MethodInsnNode)insn).name.equals("end")) ends++;
                }
        }
        check(methodsBefore == methodsAfter, "no original method removed or renamed");
        check(calls == 6 && cursorCalls == 1 && ends == 2, "exact four targeted method hooks");
        reject(() -> SaveMenuPatch.apply(nodes), "double transform rejected");
        check(Files.size(Paths.get(args[0])) > 0, "original archive read only");
        System.out.println("SaveMenuLayoutTest PASS " + passed + "; no game/native/render/input execution; G3 blocked");
    }
}
