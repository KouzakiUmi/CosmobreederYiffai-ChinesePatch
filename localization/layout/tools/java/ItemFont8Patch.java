import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-only ASM patch. Caller SHA-checks INPUT_SHA256 against original JAR
 * bytes BEFORE any other patch, then passes EXPAND_FRAMES nodes. All targets are
 * structurally preflighted before the first mutation. Emit COMPUTE_FRAMES/MAXS.
 * Compatible with additive BridgePatch on Yg; NOT with ItemMenuPatch prototype.
 */
public final class ItemFont8Patch implements Opcodes {
    public static final Map<String, String> INPUT_SHA256;
    public static final String[] HELPER_INVENTORY = {"PRG/ItemFont8.class"};
    /** Final minimal variant consumes EXISTING classic8; no new assets/roles. */
    public static final String[] ASSET_INVENTORY = {};
    public static final String EXISTING_FNT_SHA256 = "a456bb96b944b2c443868b5ea02d2b458744eb795e161d6835a2d490a67c2510";
    private static final String HELPER = "PRG/ItemFont8";
    static {
        Map<String,String> pins = new LinkedHashMap<String,String>();
        pins.put("PRG/Le", "6e0a0f8d826cb42810354ac753fb609d766d3e487a423692f51c2809b103e86d");
        pins.put("PRG/Lg", "426f0c4be7947b096e421fb62a387e5b43a9e5b8f084475dd7464cf9f50e1240");
        pins.put("PRG/Lb", "c753a5df061b665c502f265fd3d340f33f52803c193daa787f294aa43cba4ae1");
        INPUT_SHA256 = Collections.unmodifiableMap(pins);
    }
    private ItemFont8Patch() { }

    public static void apply(Map<String,ClassNode> classes) {
        ClassNode le = require(classes, "PRG/Le"), lg = require(classes, "PRG/Lg"), lb = require(classes, "PRG/Lb");
        for (ClassNode c : new ClassNode[] {le, lg, lb})
            for (MethodNode m : c.methods)
                for (AbstractInsnNode n : m.instructions.toArray())
                    if (n instanceof MethodInsnNode && (((MethodInsnNode)n).owner.equals(HELPER)
                            || ((MethodInsnNode)n).owner.equals("PRG/ItemMenuLayout")))
                        fail("already patched or conflicting prototype: " + c.name);
        MethodNode ctor = method(le, "<init>", "(LPRG/apr;)V");
        FieldInsnNode name = field(ctor, PUTFIELD, "PRG/Le", "u", "LPRG/Lg;");
        FieldInsnNode description = field(ctor, PUTFIELD, "PRG/Le", "v", "LPRG/Lb;");
        requireCall(previous(name), "PRG/Lg", "<init>", "(LPRG/azy;LPRG/azy;LPRG/azy;)V");
        requireCall(previous(description), "PRG/Lb", "<init>", "(LPRG/azy;LPRG/azy;LPRG/azy;)V");
        MethodNode nameSupplier = method(le, "b", "(LPRG/Le;)Ljava/lang/String;");
        uniqueCall(nameSupplier, "PRG/aDJ", "a", "(Ljava/lang/String;IC)Ljava/lang/String;");
        MethodInsnNode oldCut = uniqueCall(nameSupplier, "PRG/aDJ", "b", "(Ljava/lang/String;I)Ljava/lang/String;");
        if (!(previous(oldCut) instanceof IntInsnNode) || ((IntInsnNode)previous(oldCut)).operand != 8)
            fail("original equipment 8-character cut changed");
        int plus = 0;
        for (AbstractInsnNode n : nameSupplier.instructions.toArray())
            if (n instanceof LdcInsnNode && "+".equals(((LdcInsnNode)n).cst)) plus++;
        if (plus != 1) fail("equipment suffix identity");
        MethodNode drawName = method(lg, "b", "(LPRG/SN;)V");
        uniqueCall(drawName, "PRG/amr$d", "a", "()Ljava/lang/String;");
        MethodInsnNode sn = uniqueCall(drawName, "PRG/SN", "a", "(Ljava/lang/String;IILjava/lang/String;)V");
        MethodNode drawDescription = method(lb, "b", "(LPRG/SN;)V");
        MethodInsnNode source = uniqueCall(drawDescription, "PRG/amr$d", "a", "()Ljava/lang/String;");
        MethodInsnNode format = uniqueCall(drawDescription, "PRG/amw", "a", "(Ljava/lang/String;LPRG/amq;LPRG/amv;Z)Ljava/lang/String;");
        requireField(first(drawDescription), GETSTATIC, "PRG/amw", "MODULE$", "LPRG/amw;");
        requireField(next(source), GETSTATIC, "PRG/NZ", "MODULE$", "LPRG/NZ;");
        requireField(next(next(source)), GETSTATIC, "PRG/Oa", "MODULE$", "LPRG/Oa;");
        if (next(next(next(source))).getOpcode() != ICONST_0 || next(next(next(next(source)))) != format)
            fail("description original format input span");
        uniqueCall(drawDescription, "PRG/amr$e", "a", "(Ljava/lang/String;I)LPRG/aCj;");
        // PRECHECK COMPLETE. No mutation, allocation hook or partial registration above.
        register(ctor, name, "registerName", "Lg");
        register(ctor, description, "registerDescription", "Lb");
        drawName.instructions.insertBefore(sn, new VarInsnNode(ALOAD, 0));
        drawName.instructions.set(sn, call("drawName", "(LPRG/SN;Ljava/lang/String;IILjava/lang/String;LPRG/Lg;)V"));
        int local = Math.max(drawDescription.maxLocals, 3);
        LabelNode legacy = new LabelNode();
        InsnList consume = new InsnList();
        consume.add(new VarInsnNode(ASTORE, local));
        consume.add(new InsnNode(POP)); // old amw receiver, full supplier evaluated once
        consume.add(new VarInsnNode(ALOAD, 0)); consume.add(new VarInsnNode(ALOAD, 1));
        consume.add(new VarInsnNode(ALOAD, local));
        consume.add(call("drawDescription", "(LPRG/Lb;LPRG/SN;Ljava/lang/String;)Z"));
        consume.add(new JumpInsnNode(IFEQ, legacy)); consume.add(new InsnNode(RETURN));
        consume.add(legacy);
        consume.add(new FieldInsnNode(GETSTATIC, "PRG/amw", "MODULE$", "LPRG/amw;"));
        consume.add(new VarInsnNode(ALOAD, local));
        drawDescription.instructions.insert(source, consume);
        drawDescription.maxLocals = local + 1;
    }
    private static void register(MethodNode m, FieldInsnNode field, String name, String type) {
        InsnList code = new InsnList(); code.add(new InsnNode(DUP));
        code.add(call(name, "(LPRG/" + type + ";)V")); m.instructions.insertBefore(field, code);
    }
    private static MethodInsnNode call(String name, String desc) {
        return new MethodInsnNode(INVOKESTATIC, HELPER, name, desc, false);
    }
    private static ClassNode require(Map<String,ClassNode> classes, String name) {
        ClassNode node = classes.get(name);
        if (node == null || !node.name.equals(name)) fail("missing class " + name);
        return node;
    }
    private static MethodNode method(ClassNode c, String name, String desc) {
        MethodNode result = null;
        for (MethodNode m : c.methods) if (m.name.equals(name) && m.desc.equals(desc)) {
            if (result != null) fail("duplicate method " + c.name + name); result = m;
        }
        if (result == null) fail("missing method " + c.name + name + desc);
        return result;
    }
    private static MethodInsnNode uniqueCall(MethodNode m, String owner, String name, String desc) {
        MethodInsnNode result = null;
        for (AbstractInsnNode n : m.instructions.toArray()) if (n instanceof MethodInsnNode) {
            MethodInsnNode c = (MethodInsnNode)n;
            if (c.owner.equals(owner) && c.name.equals(name) && c.desc.equals(desc)) {
                if (result != null) fail("duplicate call " + owner + name); result = c;
            }
        }
        if (result == null) fail("missing call " + owner + name + desc);
        return result;
    }
    private static FieldInsnNode field(MethodNode m, int opcode, String owner, String name, String desc) {
        FieldInsnNode result = null;
        for (AbstractInsnNode n : m.instructions.toArray()) if (n instanceof FieldInsnNode) {
            FieldInsnNode f = (FieldInsnNode)n;
            if (f.getOpcode() == opcode && f.owner.equals(owner) && f.name.equals(name) && f.desc.equals(desc)) {
                if (result != null) fail("duplicate field assignment " + owner + name); result = f;
            }
        }
        if (result == null) fail("missing field assignment " + owner + name);
        return result;
    }
    private static void requireField(AbstractInsnNode n, int op, String owner, String name, String desc) {
        if (!(n instanceof FieldInsnNode)) fail("expected field " + name);
        FieldInsnNode f = (FieldInsnNode)n;
        if (f.getOpcode() != op || !f.owner.equals(owner) || !f.name.equals(name) || !f.desc.equals(desc)) fail("field identity " + name);
    }
    private static void requireCall(AbstractInsnNode n, String owner, String name, String desc) {
        if (!(n instanceof MethodInsnNode)) fail("expected call " + name);
        MethodInsnNode c = (MethodInsnNode)n;
        if (!c.owner.equals(owner) || !c.name.equals(name) || !c.desc.equals(desc)) fail("call identity " + name);
    }
    private static void requireVar(AbstractInsnNode n, int op, int local) {
        if (!(n instanceof VarInsnNode) || n.getOpcode() != op || ((VarInsnNode)n).var != local) fail("variable identity");
    }
    private static AbstractInsnNode next(AbstractInsnNode n) {
        do { n = n.getNext(); } while (n != null && n.getOpcode() < 0);
        if (n == null) fail("unexpected instruction end"); return n;
    }
    private static AbstractInsnNode previous(AbstractInsnNode n) {
        do { n = n.getPrevious(); } while (n != null && n.getOpcode() < 0);
        if (n == null) fail("unexpected instruction start"); return n;
    }
    private static AbstractInsnNode first(MethodNode m) {
        AbstractInsnNode n = m.instructions.getFirst(); while (n != null && n.getOpcode() < 0) n = n.getNext();
        if (n == null) fail("empty method"); return n;
    }
    private static void fail(String message) { throw new IllegalStateException("item8 preflight: " + message); }
}
