import java.util.*;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Incremental frozen-r27 adapter. Caller verifies every INPUT_SHA256 before
 * applying. All sites preflight before any mutation; emit COMPUTE_FRAMES/MAXS.
 * Does NOT patch Mf/Iu/It/Id/Mc or enable SaveMenuLayout's single-card prototype.
 */
public final class CompactFieldsPatch implements Opcodes {
    public static final String[] HELPER_INVENTORY={"PRG/CompactFields.class"};
    public static final Map<String,String> INPUT_SHA256;
    static {
        Map<String,String> p=new LinkedHashMap<String,String>();
        p.put("PRG/LY","daf1134310a20f66ebbf6b409cc07829ccebe520ec51fc60ba280fe1dbc6e2de");
        p.put("PRG/Mb","39a1dd0a221b75514d9a320ebb88e9fa9fc21fd0c95c783ec33b73999e5f8e31");
        p.put("PRG/Mn","1cbc6fe691709045077e132f4edd8d2a163f10df3220bcb379a03350d3fb7f09");
        INPUT_SHA256=Collections.unmodifiableMap(p);
    }
    private static final String H="PRG/CompactFields";
    public static void apply(Map<String,ClassNode> classes) {
        ClassNode ly=need(classes,"PRG/LY"),mb=need(classes,"PRG/Mb"),mn=need(classes,"PRG/Mn");
        for(ClassNode c:new ClassNode[]{ly,mb,mn}) for(MethodNode m:c.methods)
            for(AbstractInsnNode i:m.instructions.toArray()) if(i instanceof MethodInsnNode &&
                (((MethodInsnNode)i).owner.equals(H)||((MethodInsnNode)i).owner.equals("PRG/SaveMenuLayout"))) fail("already patched/conflicting "+c.name);
        MethodNode sy=method(ly,"b","(LPRG/SN;)V"),nm=method(mb,"b","(LPRG/SN;)V");
        List<MethodInsnNode> rows=calls(sy,"PRG/Id","a","(LPRG/SN;Ljava/lang/String;II)V",2);
        List<MethodInsnNode> names=calls(nm,"PRG/Id","a","(LPRG/SN;Ljava/lang/String;II)V",3);
        MethodInsnNode cursor=calls(nm,"PRG/SN","a","(Ljava/lang/String;IIII)V",1).get(0);
        MethodNode normal=method(mn,"b","(LPRG/SN;)V"),selected=method(mn,"a","(LPRG/SN;LPRG/aab;)V");
        MethodInsnNode n=calls(normal,"PRG/SN","a","(Ljava/lang/String;IILjava/lang/String;)V",1).get(0);
        MethodInsnNode s=calls(selected,"PRG/SN","a","(Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V",1).get(0);
        // No modifications until all six draw sites and the cursor are proven.
        replace(sy,rows.get(0),"saveRow","(LPRG/Id;LPRG/SN;Ljava/lang/String;II)V");
        replace(sy,rows.get(1),"saveLower","(LPRG/Id;LPRG/SN;Ljava/lang/String;II)V");
        replace(nm,names.get(0),"name","(LPRG/Id;LPRG/SN;Ljava/lang/String;II)V");
        nm.instructions.insertBefore(cursor,new VarInsnNode(ALOAD,0));
        replace(nm,cursor,"nameCursor","(LPRG/SN;Ljava/lang/String;IIIILPRG/Mb;)V");
        replace(normal,n,"letter","(LPRG/SN;Ljava/lang/String;IILjava/lang/String;)V");
        replace(selected,s,"selectedLetter","(LPRG/SN;Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V");
    }
    private static void replace(MethodNode m,MethodInsnNode n,String name,String desc) {m.instructions.set(n,new MethodInsnNode(INVOKESTATIC,H,name,desc,false));}
    private static ClassNode need(Map<String,ClassNode> c,String n){ClassNode r=c.get(n);if(r==null||!n.equals(r.name))fail("missing "+n);return r;}
    private static MethodNode method(ClassNode c,String n,String d){MethodNode r=null;for(MethodNode m:c.methods)if(m.name.equals(n)&&m.desc.equals(d)){if(r!=null)fail("duplicate method");r=m;}if(r==null)fail(c.name+n+d);return r;}
    private static List<MethodInsnNode> calls(MethodNode m,String o,String n,String d,int count){List<MethodInsnNode> r=new ArrayList<MethodInsnNode>();for(AbstractInsnNode i:m.instructions.toArray())if(i instanceof MethodInsnNode){MethodInsnNode c=(MethodInsnNode)i;if(c.owner.equals(o)&&c.name.equals(n)&&c.desc.equals(d))r.add(c);}if(r.size()!=count)fail("site count "+o+n+" "+r.size());return r;}
    private static void fail(String s){throw new IllegalStateException("compact preflight: "+s);}
}
