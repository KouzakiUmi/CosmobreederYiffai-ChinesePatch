import java.util.*;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** JDK17 build tool. Caller MUST pin original bytes with INPUT_SHA256 before
 * parsing, and write with archive-aware COMPUTE_FRAMES | COMPUTE_MAXS.
 * This adapter does NOT patch global amw, amn, jo, Id, menus or input. */
public final class SubtitlePatch implements Opcodes {
    private SubtitlePatch() { }
    public static final String CREATE = "(LPRG/anh;LPRG/amX;)LPRG/anh;";
    private static final String FORMAT = "(Ljava/lang/String;LPRG/amq;LPRG/amv;)LPRG/aEO;";
    public static final Map<String, String> INPUT_SHA256;
    static {
        Map<String, String> pins = new LinkedHashMap<String, String>();
        pins.put("PRG/amH", "642429e8ee6b4f4297335fcf05cfd692cc5b7e458140b6f622656c38349f872d");
        pins.put("PRG/anp", "0ad473941da05fec7704ec23831b1d9cb80c333f84b90aa512c18e3bc477f9d3");
        INPUT_SHA256 = Collections.unmodifiableMap(pins);
    }
    private static final String[] HASHES = {
        "212281e67f6bbe28b67d7297d25380979a755ce9c991f88be61de285bb95d39b",
        "d0b62b5bc3411fbc6530a73d9e58690010e96081c4700707568fa2e622c61993"
    };
    public static void apply(Map<String, ClassNode> classes) {
        List<MethodNode> methods = new ArrayList<MethodNode>();
        List<MethodInsnNode> calls = new ArrayList<MethodInsnNode>();
        List<AbstractInsnNode> returns = new ArrayList<AbstractInsnNode>();
        int index = 0;
        for (String name : INPUT_SHA256.keySet()) {
            ClassNode c = classes.get(name);
            if (c == null || !name.equals(c.name) || c.version != V1_8) fail("missing/version " + name);
            MethodNode m = VsnPatch.method(c, "a", CREATE);
            if (m.access != ACC_PUBLIC || m.maxLocals != 18 || !m.tryCatchBlocks.isEmpty()
                || !HASHES[index++].equals(VsnPatch.fingerprint(m))) fail("original method " + name);
            List<AbstractInsnNode> code = new ArrayList<AbstractInsnNode>();
            for (AbstractInsnNode n : m.instructions) if (n.getOpcode() >= 0) code.add(n);
            MethodInsnNode found = null;
            for (int i = 0; i < code.size(); i++) {
                AbstractInsnNode n = code.get(i);
                if (!call(n, "PRG/amw", "a", FORMAT)) continue;
                if (found != null || i < 6 || i + 4 >= code.size()
                    || !field(code.get(i-6), "PRG/amw", "MODULE$", "LPRG/amw;")
                    || !var(code.get(i-5), ALOAD, 3) || !var(code.get(i-4), ALOAD, 2)
                    || !call(code.get(i-3), "PRG/amX", "e", "()LPRG/amq;")
                    || !var(code.get(i-2), ALOAD, 2)
                    || !call(code.get(i-1), "PRG/amX", "f", "()LPRG/amv;")
                    || !call(code.get(i+1), "PRG/aEO", "s", "()Ljava/lang/Object;")
                    || !(code.get(i+2) instanceof TypeInsnNode)
                    || code.get(i+2).getOpcode() != CHECKCAST
                    || !((TypeInsnNode)code.get(i+2)).desc.equals("PRG/amr$d")
                    || !call(code.get(i+3), "PRG/amr$d", "a", "()Ljava/lang/String;")
                    || !var(code.get(i+4), ASTORE, 4)) fail("exact formatter boundary " + name);
                found = (MethodInsnNode)n;
            }
            if (found == null || code.get(code.size()-1).getOpcode() != ARETURN
                || !call(code.get(code.size()-2), "PRG/anh", "a",
                    "(LPRG/ane;DLPRG/azK;LPRG/aEO;LPRG/aEO;LPRG/TV;ZLPRG/amK;LPRG/amR;LPRG/aEO;LPRG/azK;)LPRG/anh;"))
                fail("formatter/return " + name);
            methods.add(m); calls.add(found); returns.add(code.get(code.size()-1));
        }
        // BOTH complete preflights passed before touching either ClassNode.
        index = 0;
        for (String name : INPUT_SHA256.keySet()) {
            MethodNode m = methods.get(index);
            MethodInsnNode original = calls.get(index);
            MethodInsnNode helper = new MethodInsnNode(INVOKESTATIC, "PRG/SubtitleLayout", "format",
                "(LPRG/amw;Ljava/lang/String;LPRG/amq;LPRG/amv;)LPRG/aEO;", false);
            m.instructions.set(original, helper);
            // Capture the ENTIRE list; the original s(), animation and deadline
            // construction remain unchanged. Local18 is new (old maxLocals18).
            InsnList capture = new InsnList();
            capture.add(new InsnNode(DUP)); capture.add(new VarInsnNode(ASTORE, 18));
            m.instructions.insert(helper, capture);
            InsnList finish = new InsnList();
            finish.add(new VarInsnNode(ALOAD, 18)); finish.add(new VarInsnNode(ALOAD, 0));
            finish.add(new MethodInsnNode(INVOKESTATIC, "PRG/SubtitleLayout", "finish",
                "(LPRG/anh;LPRG/aEO;L" + name + ";)LPRG/anh;", false));
            m.instructions.insertBefore(returns.get(index), finish);
            for (AbstractInsnNode n : m.instructions.toArray()) if (n instanceof FrameNode) m.instructions.remove(n);
            index++;
        }
    }
    private static boolean call(AbstractInsnNode n, String owner, String name, String desc) {
        if (!(n instanceof MethodInsnNode)) return false;
        MethodInsnNode m = (MethodInsnNode)n;
        return n.getOpcode() == INVOKEVIRTUAL && owner.equals(m.owner) && name.equals(m.name)
            && desc.equals(m.desc) && !m.itf;
    }
    private static boolean field(AbstractInsnNode n, String owner, String name, String desc) {
        if (!(n instanceof FieldInsnNode)) return false;
        FieldInsnNode f = (FieldInsnNode)n;
        return n.getOpcode() == GETSTATIC && owner.equals(f.owner) && name.equals(f.name) && desc.equals(f.desc);
    }
    private static boolean var(AbstractInsnNode n, int op, int local) {
        return n instanceof VarInsnNode && n.getOpcode() == op && ((VarInsnNode)n).var == local;
    }
    private static void fail(String why) { throw new IllegalStateException("Subtitle patch refused: " + why); }
}
