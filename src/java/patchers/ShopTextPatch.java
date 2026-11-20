import java.util.*;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-time only. PRG/ME draws each shop list row name with the default 10px
 * font (sn.b()) while the row baseline steps are 8px (y+32/40/48/56), so CJK item
 * names overlap vertically. Route ONLY that per-row name call through
 * PRG/SceneText.dataName, which chooses the 8px classic role for wide text
 * (identical to the proven PRG/Kc data-book fix). Nothing else changes. */
public final class ShopTextPatch implements Opcodes {
    private ShopTextPatch() { }
    /** Raw SHA of PRG/ME in the frozen r27 base. The driver identity-checks it. */
    public static final Map<String,String> INPUT_SHA256;
    static {
        Map<String,String> raw = new LinkedHashMap<String,String>();
        raw.put("PRG/ME", "e7af3be1c73172313a3777c5fc98dd1d680db887a74da27ec24905d68ee965fc");
        INPUT_SHA256 = Collections.unmodifiableMap(raw);
    }
    // Single-row shop renderer: a(SN, MS item, int x, int y, MQ, apr)
    private static final String ROW_METHOD = "(LPRG/SN;LPRG/MS;IILPRG/MQ;LPRG/apr;)V";
    private static final String SN_PLAIN = "(Ljava/lang/String;IILjava/lang/String;)V";
    private static final String DATANAME = "(LPRG/SN;Ljava/lang/String;IILjava/lang/String;)V";

    public static void apply(Map<String,ClassNode> classes) {
        ClassNode c = classes.get("PRG/ME");
        if (c == null || !"PRG/ME".equals(c.name) || c.version != 52)
            throw new IllegalStateException("ShopTextPatch: missing/version PRG/ME");
        MethodNode row = null;
        for (MethodNode m : c.methods)
            if (m.name.equals("a") && m.desc.equals(ROW_METHOD)) {
                if (row != null) throw new IllegalStateException("ShopTextPatch: duplicate row method");
                row = m;
            }
        if (row == null) throw new IllegalStateException("ShopTextPatch: missing row method");
        MethodInsnNode target = null;
        int count = 0;
        for (AbstractInsnNode n : row.instructions) {
            if (!(n instanceof MethodInsnNode)) continue;
            MethodInsnNode call = (MethodInsnNode) n;
            if (call.getOpcode() == INVOKEINTERFACE && "PRG/SN".equals(call.owner)
                    && "a".equals(call.name) && SN_PLAIN.equals(call.desc)) {
                target = call;
                count++;
            }
        }
        if (count != 1)
            throw new IllegalStateException("ShopTextPatch: expected exactly one product-name call, found " + count);
        // The instance receiver (SN) is already the first stack operand, so swapping
        // the interface call for a static helper with SN as parameter 0 needs no
        // extra ALOAD and leaves the stack shape identical.
        row.instructions.set(target,
            new MethodInsnNode(INVOKESTATIC, "PRG/SceneText", "dataName", DATANAME, false));
        System.out.println("PATCH ShopTextPatch: PRG/ME row name -> SceneText.dataName (classic for CJK 8px rows)");
    }
}
