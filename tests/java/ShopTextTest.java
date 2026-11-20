import java.lang.reflect.*;
import java.nio.file.*;
import java.util.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;
import PRG.SN;
import PRG.SceneText;

/**
 * Regression for the shop list 8px-row / 10px-glyph overlap fix (PRG/ME).
 *
 * <p>PRG/ME renders each shop row name at 8px row steps (y+32/40/48/56) with the
 * default 10px font (sn.b()). ShopTextPatch routes ONLY that per-row name call to
 * PRG/SceneText.dataName, which uses the 8px "classic" role for CJK text (same
 * proven fix as the PRG/Kc data book). This test:
 *   1. re-applies ShopTextPatch to the FROZEN base PRG/ME and asserts the exact
 *      single call site becomes INVOKESTATIC PRG/SceneText.dataName;
 *   2. asserts the BUILT candidate PRG/ME already carries that static call and no
 *      longer has the raw INVOKEINTERFACE SN.a(String,int,int,String);
 *   3. functionally checks SceneText.dataName selects "classic" for CJK and keeps
 *      the caller role for ASCII.
 *
 * args: <baseJar> <candidateJar>
 */
public final class ShopTextTest {
    private static final String ROW_METHOD = "(LPRG/SN;LPRG/MS;IILPRG/MQ;LPRG/apr;)V";
    private static final String SN_PLAIN = "(Ljava/lang/String;IILjava/lang/String;)V";
    private static final String DATANAME = "(LPRG/SN;Ljava/lang/String;IILjava/lang/String;)V";
    private static int failures = 0;
    static void check(boolean ok, String msg) { if (!ok) { failures++; System.out.println("FAIL: " + msg); } }

    static ClassNode load(Path jar, String entry) throws Exception {
        try (JarFile jf = new JarFile(jar.toFile())) {
            JarEntry je = jf.getJarEntry(entry + ".class");
            if (je == null) throw new IllegalStateException("missing " + entry + " in " + jar);
            byte[] raw = jf.getInputStream(je).readAllBytes();
            ClassNode cn = new ClassNode();
            new ClassReader(raw).accept(cn, ClassReader.EXPAND_FRAMES);
            return cn;
        }
    }

    static MethodNode row(ClassNode c) {
        MethodNode found = null;
        for (MethodNode m : c.methods)
            if (m.name.equals("a") && m.desc.equals(ROW_METHOD)) {
                if (found != null) throw new IllegalStateException("duplicate row method");
                found = m;
            }
        return found;
    }

    static int countCall(MethodNode m, int opcode, String owner, String name, String desc) {
        int n = 0;
        for (AbstractInsnNode node : m.instructions)
            if (node instanceof MethodInsnNode) {
                MethodInsnNode c = (MethodInsnNode) node;
                if (c.getOpcode() == opcode && c.owner.equals(owner) && c.name.equals(name) && c.desc.equals(desc)) n++;
            }
        return n;
    }

    /** Record the role passed to sn.a(String,int,int,String). */
    static final class Recorder implements InvocationHandler {
        String role;
        public Object invoke(Object proxy, Method m, Object[] a) {
            if (m.getName().equals("a") && a != null && a.length == 4 && a[0] instanceof String) role = (String) a[3];
            return null;
        }
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 2) throw new IllegalArgumentException("usage: ShopTextTest baseJar candidateJar");
        Path base = Paths.get(args[0]);
        Path candidate = Paths.get(args[1]);

        // 1) Re-apply patch to frozen base and inspect the mutation.
        ClassNode baseMe = load(base, "PRG/ME");
        Map<String, ClassNode> nodes = new LinkedHashMap<String, ClassNode>();
        nodes.put("PRG/ME", baseMe);
        ShopTextPatch.apply(nodes);
        MethodNode baseRow = row(baseMe);
        check(baseRow != null, "base PRG/ME missing row method");
        check(countCall(baseRow, Opcodes.INVOKESTATIC, "PRG/SceneText", "dataName", DATANAME) == 1,
                "patch did not redirect the row name call to SceneText.dataName");
        check(countCall(baseRow, Opcodes.INVOKEINTERFACE, "PRG/SN", "a", SN_PLAIN) == 0,
                "raw product-name call still present after patch");

        // 2) Candidate jar must already be patched.
        ClassNode candMe = load(candidate, "PRG/ME");
        MethodNode candRow = row(candMe);
        check(candRow != null, "candidate PRG/ME missing row method");
        check(countCall(candRow, Opcodes.INVOKESTATIC, "PRG/SceneText", "dataName", DATANAME) == 1,
                "candidate PRG/ME row name not routed to SceneText.dataName");
        check(countCall(candRow, Opcodes.INVOKEINTERFACE, "PRG/SN", "a", SN_PLAIN) == 0,
                "candidate PRG/ME still has raw product-name draw");

        // 3) Functional: Chinese -> classic (8px), ASCII -> caller role.
        Recorder rec = new Recorder();
        SN proxy = (SN) Proxy.newProxyInstance(ShopTextTest.class.getClassLoader(), new Class[]{SN.class}, rec);
        SceneText.dataName(proxy, "\u9e21\u817f", 0, 0, "default");
        check("classic".equals(rec.role), "CJK shop name must use classic role, got " + rec.role);
        rec.role = null;
        SceneText.dataName(proxy, "Meat", 0, 0, "default");
        check("default".equals(rec.role), "ASCII shop name must keep caller role, got " + rec.role);

        if (failures != 0) throw new IllegalStateException("ShopTextTest failures: " + failures);
        System.out.println("PASS ShopTextTest: PRG/ME row names use SceneText.dataName (classic for CJK 8px rows)");
    }
}
