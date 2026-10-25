import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.ArrayList;
import java.util.Collections;
import java.util.IdentityHashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import jdk.internal.org.objectweb.asm.Handle;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-time only, JDK 17 internal ASM. The caller writes COMPUTE_FRAMES |
 * COMPUTE_MAXS using its archive-aware common-superclass resolver. No main.
 */
public final class VsnPatch implements Opcodes {
    private VsnPatch() { }
    public static final String CALLBACK = "(LPRG/jo;Ljava/lang/String;LPRG/azK;LPRG/amn;ILjava/lang/String;Z)V";
    public static final String COMPOSE = "(LPRG/ZJ;LPRG/amq;IIZIILPRG/SN;LPRG/anh;LPRG/amU;)V";
    public static final String CREATE = "(LPRG/anh;LPRG/amX;)LPRG/anh;";
    public static final String COPY = "(Ljava/lang/String;DLPRG/azK;F)LPRG/amn;";
    public static final String LEGACY = "cosmoloc$legacyBody";
    public static final Map<String, String> INPUT_SHA256;
    static {
        Map<String, String> m = new LinkedHashMap<String, String>();
        m.put("PRG/jo", "7d9209e5275c9333bb581c94028034beab553716e222e97cd93418d53d41fa76");
        m.put("PRG/jl", "a07da6c75311bf5ebc84c53f854f998dd32aade0fd06b55666acabd9b853ac08");
        m.put("PRG/amH", "642429e8ee6b4f4297335fcf05cfd692cc5b7e458140b6f622656c38349f872d");
        m.put("PRG/amn", "1e1351fac324d6f948abb1594594c751acde21b7368f04809672ea10ce56f4bc");
        INPUT_SHA256 = Collections.unmodifiableMap(m);
    }
    // Canonical symbolic instruction hashes ignore only debug nodes/StackMap
    // representation, allowing either normal or EXPAND_FRAMES ClassReader.
    private static final String JO = "1ff8f77f97595586444b051762e3512c3a5a600609be29e00e35f4f1211cf183";
    private static final String JL = "6f27b4d0cd92a132f757b2e9f85746f894964a3caea23447af53f0e7c87b54e2";
    private static final String AMH = "212281e67f6bbe28b67d7297d25380979a755ce9c991f88be61de285bb95d39b";

    private static final String AMN = "5f0481cec40eb76b303b7ceebe3302f291da1867d55f112a1e98379ca6fbf200";

    public static void apply(Map<String, ClassNode> classes) {
        ClassNode jo = required(classes, "PRG/jo"), jl = required(classes, "PRG/jl");
        ClassNode amH = required(classes, "PRG/amH"), amn = required(classes, "PRG/amn");
        MethodNode callback = method(jo, "a", CALLBACK);
        MethodNode compose = method(jl, "a", COMPOSE);
        MethodNode create = method(amH, "a", CREATE);
        MethodNode copier = method(amn, "a", COPY);
        check(callback, JO); check(compose, JL); check(create, AMH); check(copier, AMN);
        List<AbstractInsnNode> copyCode = code(copier);
        if (copyCode.size() != 8 || copyCode.get(7).getOpcode() != ARETURN
            || !copier.tryCatchBlocks.isEmpty()) fail("unexpected amn copier boundary");
        for (MethodNode m : jo.methods) if (m.name.equals(LEGACY)) fail("already patched jo");
        for (ClassNode c : new ClassNode[] { jo, jl, amH, amn }) {
            for (MethodNode m : c.methods) for (AbstractInsnNode n : m.instructions)
                if (n instanceof MethodInsnNode && ((MethodInsnNode)n).owner.equals("PRG/VsnLayout"))
                    fail("already patched " + c.name);
        }
        List<AbstractInsnNode> body = code(callback);
        int stop = -1;
        for (int i = 0; i < body.size(); i++) {
            AbstractInsnNode n = body.get(i);
            if (n instanceof MethodInsnNode) {
                MethodInsnNode call = (MethodInsnNode)n;
                if (call.owner.equals("PRG/aEO") && call.name.equals("f")
                    && call.desc.equals("(LPRG/azz;)V")) { stop = i + 1; break; }
            }
        }
        if (stop != 14 || !callback.tryCatchBlocks.isEmpty()) fail("unexpected jo body boundary");
        AbstractInsnNode captureAt = null;
        for (AbstractInsnNode n : create.instructions) {
            if (n instanceof MethodInsnNode) {
                MethodInsnNode call = (MethodInsnNode)n;
                if (call.owner.equals("PRG/amo") && call.name.equals("a")
                    && call.desc.equals("(Ljava/lang/String;DF)LPRG/amn;")) {
                    AbstractInsnNode next = n.getNext();
                    while (next != null && next.getOpcode() < 0) next = next.getNext();
                    if (!(next instanceof VarInsnNode) || next.getOpcode() != ASTORE
                        || ((VarInsnNode)next).var != 5) fail("unexpected amH capture local");
                    if (captureAt != null) fail("duplicate amH construction");
                    captureAt = next;
                }
            }
        }
        if (captureAt == null) fail("missing amH capture site");
        // All validation precedes the first mutation: mismatch cannot leave a
        // partially patched class map for an unwary build driver to package.
        MethodNode legacy = new MethodNode(ACC_PRIVATE | ACC_STATIC | ACC_SYNTHETIC,
            LEGACY, "(LPRG/jo;Ljava/lang/String;Ljava/lang/String;)V", null, null);
        for (int i = 0; i < stop; i++) {
            AbstractInsnNode copy = body.get(i).clone(new IdentityHashMap<LabelNode, LabelNode>());
            if (copy instanceof VarInsnNode) {
                VarInsnNode v = (VarInsnNode)copy;
                if (v.var == 5) v.var = 2;
                else if (v.var == 7) v.var = 3;
            }
            legacy.instructions.add(copy);
        }
        legacy.instructions.add(new InsnNode(RETURN));
        legacy.maxLocals = 4; legacy.maxStack = 4;
        jo.methods.add(legacy);
        LabelNode tail = new LabelNode();
        InsnList replacement = new InsnList();
        field(replacement, "a", "LPRG/anh;"); field(replacement, "d", "LPRG/SN;");
        replacement.add(new VarInsnNode(ALOAD, 1)); field(replacement, "c", "Z");
        replacement.add(new VarInsnNode(ALOAD, 3)); replacement.add(new VarInsnNode(ILOAD, 4));
        replacement.add(new VarInsnNode(ALOAD, 5)); field(replacement, "e", "I"); field(replacement, "f", "I");
        replacement.add(new MethodInsnNode(INVOKESTATIC, "PRG/VsnLayout", "draw",
            "(LPRG/anh;LPRG/SN;Ljava/lang/String;ZLPRG/amn;ILjava/lang/String;II)Z", false));
        replacement.add(new JumpInsnNode(IFNE, tail));
        replacement.add(new VarInsnNode(ALOAD, 0)); replacement.add(new VarInsnNode(ALOAD, 1));
        replacement.add(new VarInsnNode(ALOAD, 5));
        replacement.add(new MethodInsnNode(INVOKESTATIC, "PRG/jo", LEGACY,
            "(LPRG/jo;Ljava/lang/String;Ljava/lang/String;)V", false));
        replacement.add(tail);
        callback.instructions.insertBefore(body.get(0), replacement);
        for (int i = 0; i < stop; i++) callback.instructions.remove(body.get(i));
        InsnList observation = new InsnList();
        observation.add(new VarInsnNode(ALOAD, 8)); observation.add(new VarInsnNode(ALOAD, 9));
        observation.add(new MethodInsnNode(INVOKESTATIC, "PRG/VsnLayout", "observe",
            "(LPRG/anh;LPRG/amU;)V", false));
        compose.instructions.insert(observation);
        InsnList capture = new InsnList();
        capture.add(new VarInsnNode(ALOAD, 0)); capture.add(new VarInsnNode(ALOAD, 3));
        capture.add(new VarInsnNode(ALOAD, 5));
        capture.add(new MethodInsnNode(INVOKESTATIC, "PRG/VsnLayout", "capture",
            "(LPRG/amH;Ljava/lang/String;LPRG/amn;)V", false));
        create.instructions.insert(captureAt, capture);
        // Preserve the fresh child on stack and pass the explicit receiver as
        // parent. inherit returns that same child; original ARETURN is retained.
        InsnList inheritance = new InsnList();
        inheritance.add(new VarInsnNode(ALOAD, 0));
        inheritance.add(new InsnNode(SWAP));
        inheritance.add(new MethodInsnNode(INVOKESTATIC, "PRG/VsnLayout", "inherit",
            "(LPRG/amn;LPRG/amn;)LPRG/amn;", false));
        copier.instructions.insertBefore(copyCode.get(7), inheritance);
        // Existing frames no longer describe inserted branch/local states.
        // The driver's COMPUTE_FRAMES is mandatory, not an optional optimization.
        for (MethodNode m : new MethodNode[] {callback, compose, create, copier}) {
            for (AbstractInsnNode n : m.instructions.toArray())
                if (n instanceof FrameNode) m.instructions.remove(n);
        }
    }
    private static void field(InsnList out, String name, String desc) {
        out.add(new VarInsnNode(ALOAD, 0));
        out.add(new FieldInsnNode(GETFIELD, "PRG/jo", name, desc));
    }
    private static ClassNode required(Map<String, ClassNode> map, String name) {
        ClassNode c = map.get(name);
        if (c == null || !name.equals(c.name) || c.version != V1_8) fail("missing/version " + name);
        return c;
    }
    public static MethodNode method(ClassNode c, String name, String desc) {
        MethodNode found = null;
        for (MethodNode m : c.methods) if (m.name.equals(name) && m.desc.equals(desc)) {
            if (found != null) fail("duplicate " + c.name + name + desc);
            found = m;
        }
        if (found == null) fail("missing " + c.name + name + desc);
        return found;
    }
    private static void check(MethodNode m, String expected) {
        if (!fingerprint(m).equals(expected)) fail("instruction fingerprint " + m.name + m.desc
            + ": expected " + expected + ", got " + fingerprint(m));
    }
    private static List<AbstractInsnNode> code(MethodNode m) {
        List<AbstractInsnNode> out = new ArrayList<AbstractInsnNode>();
        for (AbstractInsnNode n : m.instructions) if (n.getOpcode() >= 0) out.add(n);
        return out;
    }
    public static String fingerprint(MethodNode m) {
        StringBuilder s = new StringBuilder(m.name).append(m.desc).append(':').append(m.access);
        Map<LabelNode, Integer> labels = new IdentityHashMap<LabelNode, Integer>();
        int offset = 0;
        for (AbstractInsnNode n : m.instructions) {
            if (n instanceof LabelNode) labels.put((LabelNode)n, offset);
            if (n.getOpcode() >= 0) offset++;
        }
        for (AbstractInsnNode n : code(m)) {
            s.append('\n').append(n.getOpcode()).append(':');
            if (n instanceof VarInsnNode) s.append(((VarInsnNode)n).var);
            else if (n instanceof IntInsnNode) s.append(((IntInsnNode)n).operand);
            else if (n instanceof FieldInsnNode) {
                FieldInsnNode f = (FieldInsnNode)n; s.append(f.owner).append('.').append(f.name).append(f.desc);
            } else if (n instanceof MethodInsnNode) {
                MethodInsnNode f = (MethodInsnNode)n;
                s.append(f.owner).append('.').append(f.name).append(f.desc).append(f.itf);
            } else if (n instanceof TypeInsnNode) s.append(((TypeInsnNode)n).desc);
            else if (n instanceof LdcInsnNode) s.append(((LdcInsnNode)n).cst);
            else if (n instanceof JumpInsnNode) s.append(labels.get(((JumpInsnNode)n).label));
            else if (n instanceof IincInsnNode) {
                IincInsnNode i = (IincInsnNode)n; s.append(i.var).append(',').append(i.incr);
            } else if (n instanceof InvokeDynamicInsnNode) {
                InvokeDynamicInsnNode i = (InvokeDynamicInsnNode)n;
                s.append(i.name).append(i.desc).append(i.bsm);
                for (Object arg : i.bsmArgs) s.append('|').append(arg);
            } else if (n instanceof TableSwitchInsnNode || n instanceof LookupSwitchInsnNode
                || n instanceof MultiANewArrayInsnNode) fail("unsupported fingerprint node");
        }
        for (TryCatchBlockNode t : m.tryCatchBlocks)
            s.append("catch:").append(labels.get(t.start)).append(',').append(labels.get(t.end))
                .append(',').append(labels.get(t.handler)).append(',').append(t.type);
        try {
            byte[] hash = MessageDigest.getInstance("SHA-256").digest(s.toString().getBytes(StandardCharsets.UTF_8));
            StringBuilder hex = new StringBuilder();
            for (byte b : hash) hex.append(String.format("%02x", b & 255));
            return hex.toString();
        } catch (java.security.NoSuchAlgorithmException impossible) { throw new AssertionError(impossible); }
    }
    private static void fail(String message) { throw new IllegalStateException("VSN patch refused: " + message); }
}
