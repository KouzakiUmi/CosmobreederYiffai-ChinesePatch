import java.util.Map;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-only Java 17/internal ASM adapter; never packaged as a runtime class. */
public final class SaveMenuPatch implements Opcodes {
    private static final String BRIDGE = "PRG/SaveMenuLayout";
    private SaveMenuPatch() { }

    public static void apply(Map<String, ClassNode> classes) {
        ClassNode mf = require(classes, "PRG/Mf");
        MethodNode draw = method(mf, "b", "(LPRG/SN;)V");
        MethodInsnNode bg = null;
        int backgrounds = 0, originalDraws = 0;
        for (AbstractInsnNode n : draw.instructions.toArray()) {
            if (n instanceof LdcInsnNode && "CosmoSaveMenuBG".equals(((LdcInsnNode)n).cst)) backgrounds++;
            if (n instanceof MethodInsnNode) {
                MethodInsnNode call = (MethodInsnNode)n;
                if (call.owner.equals("PRG/SN") && call.name.equals("a")
                        && call.desc.equals("(Ljava/lang/String;II)V")) bg = call;
                if (call.owner.equals("PRG/ZJ") && call.name.equals("a")
                        && call.desc.equals("(LPRG/ZJ;LPRG/SN;)V")) originalDraws++;
                if (call.owner.equals(BRIDGE)) throw new IllegalStateException("Already patched Mf");
            }
        }
        if (backgrounds != 1 || bg == null || originalDraws != 1)
            throw new IllegalStateException("Mf save draw identity mismatch");
        LabelNode start = new LabelNode(), end = new LabelNode(), handler = new LabelNode();
        InsnList enter = new InsnList();
        enter.add(start);
        enter.add(new VarInsnNode(ALOAD, 0)); enter.add(new VarInsnNode(ALOAD, 1));
        enter.add(new MethodInsnNode(INVOKESTATIC, BRIDGE, "begin", "(LPRG/Mf;LPRG/SN;)V", false));
        draw.instructions.insert(bg, enter);
        for (AbstractInsnNode n : draw.instructions.toArray()) {
            if (n.getOpcode() == RETURN) {
                InsnList leave = new InsnList();
                leave.add(new MethodInsnNode(INVOKESTATIC, BRIDGE, "end", "()V", false));
                draw.instructions.insertBefore(n, leave);
            }
        }
        draw.instructions.add(end); draw.instructions.add(handler);
        int exception = Math.max(draw.maxLocals, 2);
        draw.instructions.add(new VarInsnNode(ASTORE, exception));
        draw.instructions.add(new MethodInsnNode(INVOKESTATIC, BRIDGE, "end", "()V", false));
        draw.instructions.add(new VarInsnNode(ALOAD, exception)); draw.instructions.add(new InsnNode(ATHROW));
        draw.tryCatchBlocks.add(new TryCatchBlockNode(start, end, handler, null));
        draw.maxLocals = exception + 1;
        guard(require(classes, "PRG/LY"), "b", "(LPRG/SN;)V", "full", "(LPRG/LY;LPRG/SN;)Z", false);
        guard(require(classes, "PRG/LX"), "b", "(LPRG/SN;)V", "empty", "(LPRG/LX;LPRG/SN;)Z", false);
        guard(require(classes, "PRG/Iu"), "a", "(LPRG/SN;LPRG/ZH;F)V", "cursor",
                "(LPRG/Iu;LPRG/SN;LPRG/ZH;F)Z", true);
        // Driver must emit with COMPUTE_FRAMES | COMPUTE_MAXS against the original hierarchy.
    }

    private static void guard(ClassNode owner, String name, String desc, String bridgeName,
                              String bridgeDesc, boolean cursor) {
        MethodNode m = method(owner, name, desc);
        for (AbstractInsnNode n : m.instructions.toArray())
            if (n instanceof MethodInsnNode && ((MethodInsnNode)n).owner.equals(BRIDGE))
                throw new IllegalStateException("Already patched " + owner.name);
        LabelNode old = new LabelNode();
        InsnList prologue = new InsnList();
        prologue.add(new VarInsnNode(ALOAD, 0)); prologue.add(new VarInsnNode(ALOAD, 1));
        if (cursor) { prologue.add(new VarInsnNode(ALOAD, 2)); prologue.add(new VarInsnNode(FLOAD, 3)); }
        prologue.add(new MethodInsnNode(INVOKESTATIC, BRIDGE, bridgeName, bridgeDesc, false));
        prologue.add(new JumpInsnNode(IFEQ, old)); prologue.add(new InsnNode(RETURN)); prologue.add(old);
        m.instructions.insert(prologue);
    }

    private static ClassNode require(Map<String,ClassNode> classes, String name) {
        ClassNode result = classes.get(name);
        if (result == null || !name.equals(result.name)) throw new IllegalStateException("Missing class " + name);
        return result;
    }
    private static MethodNode method(ClassNode owner, String name, String desc) {
        MethodNode result = null;
        for (MethodNode m : owner.methods) if (m.name.equals(name) && m.desc.equals(desc)) {
            if (result != null) throw new IllegalStateException("Duplicate target " + owner.name + name + desc);
            result = m;
        }
        if (result == null) throw new IllegalStateException("Missing method " + owner.name + name + desc);
        return result;
    }
}
