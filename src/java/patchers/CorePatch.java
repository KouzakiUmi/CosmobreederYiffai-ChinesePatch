import java.util.*;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-time only. Pin PRG/amn bytes before parsing. Applies on frozen r27
 * or the identical original amn; requires VsnPatch and frame-aware writer.
 * Only terminal trim changes. Constructor/index table/deadlines/input stay exact. */
public final class CorePatch implements Opcodes {
    private CorePatch() { }
    public static final Map<String,String> INPUT_SHA256 = Collections.singletonMap(
        "PRG/amn", "1e1351fac324d6f948abb1594594c751acde21b7368f04809672ea10ce56f4bc");
    private static final String METHOD = "1b7385462c5b24da0c93c2dd0145031d537c4e5bd0f94a1b77d7f77d0f9a2719";
    public static void apply(Map<String,ClassNode> classes) {
        ClassNode c=classes.get("PRG/amn");
        if(c==null || !"PRG/amn".equals(c.name) || c.version!=V1_8)
            throw new IllegalStateException("CorePatch: missing/version amn");
        MethodNode m=VsnPatch.method(c,"a","(DZ)I");
        if(!METHOD.equals(VsnPatch.fingerprint(m)))
            throw new IllegalStateException("CorePatch: amn a(DZ) fingerprint");
        MethodInsnNode found=null;
        for(AbstractInsnNode n:m.instructions) if(n instanceof MethodInsnNode) {
            MethodInsnNode call=(MethodInsnNode)n;
            if(call.getOpcode()==INVOKEVIRTUAL && "PRG/amr$e".equals(call.owner)
                && "c".equals(call.name) && "(Ljava/lang/String;)Ljava/lang/String;".equals(call.desc)) {
                if(found!=null) throw new IllegalStateException("CorePatch: duplicate trim");
                found=call;
            }
        }
        if(found==null) throw new IllegalStateException("CorePatch: missing trim");
        m.instructions.set(found,new MethodInsnNode(INVOKESTATIC,"PRG/DialogueWrap","terminalText",
            "(LPRG/amr$e;Ljava/lang/String;)Ljava/lang/String;",false));
    }
}
