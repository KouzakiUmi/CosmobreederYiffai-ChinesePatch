import java.util.Map;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** One additive, narrow accessor; no existing renderer method is replaced. */
public final class BridgePatch implements Opcodes {
    public static void apply(Map<String, ClassNode> classes) {
        ClassNode node = classes.get("PRG/Yg");
        if (node == null) throw new IllegalArgumentException("Missing pinned Yg");
        if (node.interfaces.contains("cosmoloc/layout/FontAccess"))
            throw new IllegalArgumentException("Already patched Yg");
        for (MethodNode method : node.methods)
            if (method.name.equals("cosmo$layoutFont"))
                throw new IllegalArgumentException("Accessor name collision");
        node.interfaces.add("cosmoloc/layout/FontAccess");
        MethodNode bridge = new MethodNode(ACC_PUBLIC | ACC_FINAL | ACC_SYNTHETIC,
                "cosmo$layoutFont", "(Ljava/lang/String;)Ljava/lang/Object;", null, null);
        InsnList code = bridge.instructions;
        code.add(new VarInsnNode(ALOAD, 0));
        code.add(new FieldInsnNode(GETFIELD, "PRG/Yg", "c", "LPRG/Yq;"));
        code.add(new MethodInsnNode(INVOKEVIRTUAL, "PRG/Yq", "f", "()LPRG/aFh;", false));
        code.add(new VarInsnNode(ALOAD, 1));
        code.add(new MethodInsnNode(INVOKEINTERFACE, "PRG/aFh", "apply",
                "(Ljava/lang/Object;)Ljava/lang/Object;", true));
        code.add(new TypeInsnNode(CHECKCAST, "PRG/Yq$b"));
        code.add(new MethodInsnNode(INVOKEVIRTUAL, "PRG/Yq$b", "a", "()LPRG/arp;", false));
        code.add(new InsnNode(ARETURN));
        node.methods.add(bridge);
    }
}
