import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-only JDK17 internal ASM. Driver SHA-pins Le/Lg/Lb BEFORE apply and emits
 * COMPUTE_FRAMES | COMPUTE_MAXS against the original hierarchy plus helpers.
 * No grid, input, original string suppliers, global amw or category labels change.
 */
public final class ItemMenuPatch implements Opcodes {
    private static final String BRIDGE = "PRG/ItemMenuLayout";
    private static final String WIDGET_CTOR = "(LPRG/azy;LPRG/azy;LPRG/azy;)V";
    private ItemMenuPatch() { }

    public static void apply(Map<String, ClassNode> classes) {
        ClassNode le = require(classes, "PRG/Le"), lg = require(classes, "PRG/Lg"), lb = require(classes, "PRG/Lb");
        for (ClassNode c : new ClassNode[] {le, lg, lb})
            for (MethodNode m : c.methods)
                for (AbstractInsnNode n : m.instructions.toArray())
                    if (n instanceof MethodInsnNode && ((MethodInsnNode)n).owner.equals(BRIDGE))
                        throw new IllegalStateException("Already patched " + c.name);

        MethodNode ctor = method(le, "<init>", "(LPRG/apr;)V");
        FieldInsnNode nameField = assignment(ctor, "u", "PRG/Lg");
        FieldInsnNode descriptionField = assignment(ctor, "v", "PRG/Lb");
        MethodNode name = method(le, "b", "(LPRG/Le;)Ljava/lang/String;");
        MethodInsnNode fullName = uniqueCall(name, "PRG/amr$d", "a", "()Ljava/lang/String;");
        AbstractInsnNode storeFull = next(fullName);
        requireVar(storeFull, ASTORE, 2, "Le complete name local2");
        MethodInsnNode cut = uniqueCall(name, "PRG/aDJ", "b", "(Ljava/lang/String;I)Ljava/lang/String;");
        List<AbstractInsnNode> part = new ArrayList<AbstractInsnNode>();
        AbstractInsnNode start = cut;
        for (int i = 0; i < 11; i++) start = previous(start);
        for (AbstractInsnNode n = start; n != next(cut); n = next(n)) part.add(n);
        if (part.size() != 12) fail("Le equipment formatting span");
        requireField(part.get(0), GETSTATIC, "PRG/aDJ", "MODULE$", "LPRG/aDJ;");
        requireField(part.get(1), GETSTATIC, "PRG/azQ", "MODULE$", "LPRG/azQ;");
        requireField(part.get(2), GETSTATIC, "PRG/aDJ", "MODULE$", "LPRG/aDJ;");
        requireField(part.get(3), GETSTATIC, "PRG/azQ", "MODULE$", "LPRG/azQ;");
        requireVar(part.get(4), ALOAD, 2, "Le equipment complete name");
        requireCall(part.get(5), "PRG/azQ", "b", "(Ljava/lang/String;)Ljava/lang/String;");
        requireInt(part.get(6), 8); requireInt(part.get(7), 32);
        requireCall(part.get(8), "PRG/aDJ", "a", "(Ljava/lang/String;IC)Ljava/lang/String;");
        requireCall(part.get(9), "PRG/azQ", "b", "(Ljava/lang/String;)Ljava/lang/String;");
        requireInt(part.get(10), 8);
        requireVar(next(cut), ASTORE, 3, "Le equipment local3");
        int plus = 0;
        for (AbstractInsnNode n : name.instructions.toArray())
            if (n instanceof LdcInsnNode && "+".equals(((LdcInsnNode)n).cst)) plus++;
        if (plus != 1) fail("Le equipment suffix identity");

        MethodNode labelDraw = method(lg, "b", "(LPRG/SN;)V");
        uniqueCall(labelDraw, "PRG/amr$d", "a", "()Ljava/lang/String;");
        MethodInsnNode sn = uniqueCall(labelDraw, "PRG/SN", "a", "(Ljava/lang/String;IILjava/lang/String;)V");
        MethodNode description = method(lb, "b", "(LPRG/SN;)V");
        MethodInsnNode fullDescription = uniqueCall(description, "PRG/amr$d", "a", "()Ljava/lang/String;");
        MethodInsnNode oldFormat = uniqueCall(description, "PRG/amw", "a",
                "(Ljava/lang/String;LPRG/amq;LPRG/amv;Z)Ljava/lang/String;");
        uniqueCall(description, "PRG/amr$e", "a", "(Ljava/lang/String;I)LPRG/aCj;");
        AbstractInsnNode descStart = first(description);
        requireField(descStart, GETSTATIC, "PRG/amw", "MODULE$", "LPRG/amw;");
        requireField(next(fullDescription), GETSTATIC, "PRG/NZ", "MODULE$", "LPRG/NZ;");
        requireField(next(next(fullDescription)), GETSTATIC, "PRG/Oa", "MODULE$", "LPRG/Oa;");
        if (next(next(next(fullDescription))).getOpcode() != ICONST_0
                || next(next(next(next(fullDescription)))) != oldFormat)
            fail("Lb original amw input span");
        // All identities are checked before any mutation.
        register(ctor, nameField, "registerName", "Lg");
        register(ctor, descriptionField, "registerDescription", "Lb");
        InsnList observe = new InsnList();
        observe.add(new VarInsnNode(ALOAD, 0)); observe.add(new VarInsnNode(ALOAD, 2));
        observe.add(call("observeFullName", "(LPRG/Le;Ljava/lang/String;)V"));
        name.instructions.insert(storeFull, observe);
        LabelNode legacy = new LabelNode(), store = new LabelNode();
        InsnList choose = new InsnList();
        choose.add(call("prototypeEnabled", "()Z")); choose.add(new JumpInsnNode(IFEQ, legacy));
        choose.add(new VarInsnNode(ALOAD, 2)); choose.add(new JumpInsnNode(GOTO, store)); choose.add(legacy);
        name.instructions.insertBefore(start, choose);
        name.instructions.insert(cut, store);
        // Existing '+' append, ams transformation and empty/blink returns remain untouched.
        labelDraw.instructions.insertBefore(sn, new VarInsnNode(ALOAD, 0));
        labelDraw.instructions.set(sn, call("drawName", "(LPRG/SN;Ljava/lang/String;IILjava/lang/String;LPRG/Lg;)V"));

        int local = Math.max(description.maxLocals, 3);
        LabelNode original = new LabelNode();
        InsnList consume = new InsnList();
        consume.add(new VarInsnNode(ASTORE, local));
        consume.add(new InsnNode(POP)); // original amw receiver; original supplier ran exactly once
        consume.add(new VarInsnNode(ALOAD, 0)); consume.add(new VarInsnNode(ALOAD, 1));
        consume.add(new VarInsnNode(ALOAD, local));
        consume.add(call("drawDescription", "(LPRG/Lb;LPRG/SN;Ljava/lang/String;)Z"));
        consume.add(new JumpInsnNode(IFEQ, original)); consume.add(new InsnNode(RETURN));
        consume.add(original);
        consume.add(new FieldInsnNode(GETSTATIC, "PRG/amw", "MODULE$", "LPRG/amw;"));
        consume.add(new VarInsnNode(ALOAD, local));
        description.instructions.insert(fullDescription, consume);
        description.maxLocals = local + 1;
    }

    private static void register(MethodNode m, FieldInsnNode field, String name, String type) {
        InsnList code = new InsnList();
        code.add(new InsnNode(DUP2)); code.add(call(name, "(LPRG/Le;LPRG/" + type + ";)V"));
        m.instructions.insertBefore(field, code);
    }
    private static MethodInsnNode call(String name, String desc) {
        return new MethodInsnNode(INVOKESTATIC, BRIDGE, name, desc, false);
    }
    private static FieldInsnNode assignment(MethodNode ctor, String field, String type) {
        FieldInsnNode found = null;
        for (AbstractInsnNode n : ctor.instructions.toArray())
            if (n instanceof FieldInsnNode) {
                FieldInsnNode f = (FieldInsnNode)n;
                if (f.getOpcode() == PUTFIELD && f.owner.equals("PRG/Le") && f.name.equals(field)
                        && f.desc.equals("L" + type + ";")) {
                    if (found != null) fail("Duplicate Le." + field);
                    requireCall(previous(f), type, "<init>", WIDGET_CTOR);
                    found = f;
                }
            }
        if (found == null) fail("Missing Le." + field);
        return found;
    }
    private static MethodInsnNode uniqueCall(MethodNode method, String owner, String name, String desc) {
        MethodInsnNode found = null;
        for (AbstractInsnNode n : method.instructions.toArray())
            if (n instanceof MethodInsnNode) {
                MethodInsnNode c = (MethodInsnNode)n;
                if (c.owner.equals(owner) && c.name.equals(name) && c.desc.equals(desc)) {
                    if (found != null) fail("Duplicate call " + owner + "." + name + desc);
                    found = c;
                }
            }
        if (found == null) fail("Missing call " + owner + "." + name + desc);
        return found;
    }
    private static void requireCall(AbstractInsnNode n, String owner, String name, String desc) {
        if (!(n instanceof MethodInsnNode)) fail("Expected call " + owner + "." + name);
        MethodInsnNode c = (MethodInsnNode)n;
        if (!c.owner.equals(owner) || !c.name.equals(name) || !c.desc.equals(desc)) fail("Call identity " + owner + "." + name);
    }
    private static void requireField(AbstractInsnNode n, int opcode, String owner, String name, String desc) {
        if (!(n instanceof FieldInsnNode)) fail("Expected field " + owner + "." + name);
        FieldInsnNode f = (FieldInsnNode)n;
        if (f.getOpcode() != opcode || !f.owner.equals(owner) || !f.name.equals(name) || !f.desc.equals(desc))
            fail("Field identity " + owner + "." + name);
    }
    private static void requireVar(AbstractInsnNode n, int opcode, int local, String identity) {
        if (!(n instanceof VarInsnNode) || n.getOpcode() != opcode || ((VarInsnNode)n).var != local) fail(identity);
    }
    private static void requireInt(AbstractInsnNode n, int value) {
        if (!(n instanceof IntInsnNode) || ((IntInsnNode)n).operand != value || n.getOpcode() != BIPUSH)
            fail("Equipment constant " + value);
    }
    private static AbstractInsnNode next(AbstractInsnNode n) {
        do { n = n.getNext(); } while (n != null && n.getOpcode() < 0);
        if (n == null) fail("Unexpected end of instructions");
        return n;
    }
    private static AbstractInsnNode previous(AbstractInsnNode n) {
        do { n = n.getPrevious(); } while (n != null && n.getOpcode() < 0);
        if (n == null) fail("Unexpected beginning of instructions");
        return n;
    }
    private static AbstractInsnNode first(MethodNode m) {
        AbstractInsnNode n = m.instructions.getFirst();
        while (n != null && n.getOpcode() < 0) n = n.getNext();
        if (n == null) fail("Empty target");
        return n;
    }
    private static ClassNode require(Map<String, ClassNode> classes, String name) {
        ClassNode c = classes.get(name);
        if (c == null || !name.equals(c.name)) fail("Missing class " + name);
        return c;
    }
    private static MethodNode method(ClassNode owner, String name, String desc) {
        MethodNode result = null;
        for (MethodNode m : owner.methods) if (m.name.equals(name) && m.desc.equals(desc)) {
            if (result != null) fail("Duplicate method " + owner.name + "." + name);
            result = m;
        }
        if (result == null) fail("Missing method " + owner.name + "." + name + desc);
        return result;
    }
    private static void fail(String message) { throw new IllegalStateException("Item menu patch identity mismatch: " + message); }
}
