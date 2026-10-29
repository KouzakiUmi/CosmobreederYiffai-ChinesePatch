import java.util.*;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-only adapter; pin original input classes in the integration driver first. */
public final class RadioLabelsPatch implements Opcodes {
    private static final String LOOKUP = "(Ljava/lang/String;LPRG/apr;)Ljava/lang/String;";
    private static final String DISPLAY = "(Ljava/lang/String;)Ljava/lang/String;";
    private RadioLabelsPatch() {}

    public static void apply(Map<String, ClassNode> classes) {
        // Preflight the complete pass before changing any shared node.
        List<MethodInsnNode> calls = new ArrayList<MethodInsnNode>();
        collect(classes, "PRG/JM", "b", "(LPRG/SN;)V", 2, calls);
        collect(classes, "PRG/JM", "a", "(LPRG/JM;LPRG/abF;LPRG/SN;ILPRG/aAJ;)V", 1, calls);
        collect(classes, "PRG/JQ", "a", "(LPRG/JQ;DLPRG/SN;IILPRG/JQ$a;)V", 1, calls);
        List<MethodInsnNode> draws = new ArrayList<MethodInsnNode>();
        for (MethodInsnNode call : calls) {
            MethodInsnNode draw = null;
            for (AbstractInsnNode n = call.getNext(); n != null; n = n.getNext()) {
                if (!(n instanceof MethodInsnNode)) continue;
                MethodInsnNode c = (MethodInsnNode)n;
                if ("PRG/SN".equals(c.owner) && "a".equals(c.name)
                        && ("(Ljava/lang/String;IILjava/lang/String;)V".equals(c.desc)
                         || "(Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V".equals(c.desc))) {
                    draw = c; break;
                }
            }
            if (draw == null || draws.contains(draw)) throw new IllegalStateException("Radio draw site drift");
            draws.add(draw);
        }
        for (MethodInsnNode call : calls) {
            for (ClassNode cls : classes.values()) for (MethodNode method : cls.methods) {
                for (AbstractInsnNode n : method.instructions.toArray()) if (n == call) {
                    method.instructions.insert(call, new MethodInsnNode(INVOKESTATIC,
                        "PRG/RadioLabels", "display", DISPLAY, false));
                    break;
                }
            }
        }
        for (MethodInsnNode draw : draws) {
            boolean tint = draw.desc.contains("LPRG/aBa;");
            draw.setOpcode(INVOKESTATIC);
            draw.owner = "PRG/RadioLabels";
            draw.name = tint ? "drawTint" : "draw";
            draw.desc = "(LPRG/SN;" + draw.desc.substring(1);
            draw.itf = false;
        }
    }

    private static void collect(Map<String, ClassNode> classes, String owner, String name,
                                String desc, int expected, List<MethodInsnNode> calls) {
        ClassNode cls = classes.get(owner);
        if (cls == null || !owner.equals(cls.name)) throw new IllegalArgumentException("Missing radio target " + owner);
        MethodNode found = null;
        for (MethodNode method : cls.methods) if (name.equals(method.name) && desc.equals(method.desc)) {
            if (found != null) throw new IllegalStateException("Duplicate radio method " + owner + desc);
            found = method;
        }
        if (found == null) throw new IllegalStateException("Missing radio method " + owner + name + desc);
        int count = 0;
        for (AbstractInsnNode insn : found.instructions.toArray()) if (insn instanceof MethodInsnNode) {
            MethodInsnNode call = (MethodInsnNode) insn;
            if ("PRG/RadioLabels".equals(call.owner)) throw new IllegalStateException("Radio labels already patched");
            if (call.getOpcode() == INVOKEVIRTUAL && "PRG/JF".equals(call.owner)
                    && "a".equals(call.name) && LOOKUP.equals(call.desc)) {
                calls.add(call); count++;
            }
        }
        if (count != expected) throw new IllegalStateException("Radio lookup count " + owner + name + desc + ": " + count + " != " + expected);
    }
}
