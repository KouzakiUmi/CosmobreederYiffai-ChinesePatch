import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-only. Raw INPUT_SHA256 checks belong BEFORE every patcher in the
 * unified builder. Then EXPAND_FRAMES -> all-target preflight -> apply ->
 * COMPUTE_FRAMES | MAXS. BridgePatch's additive Yg accessor is compatible.
 * No Id/SN/global default method is patched, only two exact story consumers.
 */
public final class StoryFont12Patch implements Opcodes {
    public static final Map<String,String> INPUT_SHA256;
    public static final String[] HELPER_INVENTORY = {"PRG/StoryFont12.class", "PRG/StoryFont12$Font.class", "PRG/StoryFont12$Metrics.class"};
    public static final String[] ASSET_INVENTORY = {"story12.fnt", "story12/story12.manifest.json", "story12/story12.coverage.json",
        "story12/OFL.txt", "story12/NOTICE.txt", "story12/LICENSES/ark-pixel/OFL.txt", "story12/LICENSES/cubic-11/OFL.txt", "story12/LICENSES/galmuri/LICENSE.txt"};
    public static final String SHARED_PNG_SOURCE = "localization/runtime/story12/bbc2-shared-story12.png";
    public static final String FONT_SHA256 = "972d49918484e3e5521a7da58dbe94f6c6c604e4f486844b75f5b3be87fa2546";
    public static final String PNG_SHA256 = "9ebe032708a9d141f1ea8a46497e25f10d26b17a0a8f6522a915f04ce4c354c4";
    private static final String HELPER = "PRG/StoryFont12";
    private static final String BOOLEAN_DRAW = "(LPRG/SN;ZLjava/lang/String;II)V";
    private static final String REPLACEMENT = "(LPRG/Id;LPRG/SN;ZLjava/lang/String;IILjava/lang/String;)V";
    static {
        Map<String,String> pins = new LinkedHashMap<String,String>();
        pins.put("PRG/Yg", "dc6c7964df17ba744ab0397d9a01be3ac97c711954c876d6b72a6d606a1d3859");
        pins.put("PRG/jo", "7d9209e5275c9333bb581c94028034beab553716e222e97cd93418d53d41fa76");
        pins.put("PRG/Na", "81c053cff955d5958e22c31283fe5e74070bed168407a091dad7d0c127843318");
        INPUT_SHA256 = Collections.unmodifiableMap(pins);
    }
    private StoryFont12Patch() { }
    public static void apply(Map<String,ClassNode> classes) {
        ClassNode yg = require(classes,"PRG/Yg"), jo = require(classes,"PRG/jo"), na = require(classes,"PRG/Na");
        for (ClassNode c : new ClassNode[] {yg,jo,na}) for(MethodNode m:c.methods)
            for(AbstractInsnNode n:m.instructions.toArray()) if(n instanceof MethodInsnNode && ((MethodInsnNode)n).owner.equals(HELPER))
                fail("already patched "+c.name);
        MethodNode ctor = method(yg,"<init>","(LPRG/ars;LPRG/Ym;LPRG/Yq;)V");
        FieldInsnNode resource = uniqueField(ctor,PUTFIELD,"PRG/Yg","c","LPRG/Yq;");
        requireVar(previous(resource),ALOAD,3);
        AbstractInsnNode end=null;
        for(AbstractInsnNode n:ctor.instructions.toArray()) if(n.getOpcode()==RETURN) {
            if(end!=null) fail("multiple Yg ctor returns"); end=n;
        }
        if(end==null) fail("missing Yg ctor return");
        requireCall(previous(end),"PRG/ars","a","(II)V");
        requireInteger(previous(previous(end)),771);
        if(previous(previous(previous(end))).getOpcode()!=ICONST_1) fail("Yg blend tail");
        requireVar(previous(previous(previous(previous(end)))),ALOAD,1);
        MethodNode subtitle=method(jo,"a","(LPRG/jo;Ljava/lang/String;LPRG/aAJ;)V");
        MethodNode story=method(na,"a","(LPRG/Na;LPRG/Na$a;LPRG/SN;IILPRG/aAJ;)V");
        MethodInsnNode subtitleDraw=uniqueCall(subtitle,"PRG/Id","a",BOOLEAN_DRAW);
        MethodInsnNode storyDraw=uniqueCall(story,"PRG/Id","a",BOOLEAN_DRAW);
        if(subtitleDraw.getOpcode()!=INVOKEVIRTUAL || storyDraw.getOpcode()!=INVOKEVIRTUAL) fail("original Id call opcode");
        uniqueField(subtitle,GETFIELD,"PRG/jo","d","LPRG/SN;");
        uniqueField(subtitle,GETFIELD,"PRG/jo","e","I");
        uniqueField(subtitle,GETFIELD,"PRG/jo","f","I");
        int fox=0,hard=0;
        for(AbstractInsnNode n:subtitle.instructions.toArray()) if(n instanceof LdcInsnNode) {
            if("Fox".equals(((LdcInsnNode)n).cst)) fox++;
            if("HardFox".equals(((LdcInsnNode)n).cst)) hard++;
        }
        if(fox!=1 || hard!=1) fail("Fox/HardFox original branch identity");
        requireSixteenStep(subtitleDraw); requireSixteenStep(storyDraw);
        uniqueCall(story,"PRG/amr$e","e","(Ljava/lang/String;)Ljava/lang/String;");
        // All identities checked. Original bool calculations, line suppliers,
        // y/16-step, patterns, state/input/animation and all other methods stay.
        InsnList register=new InsnList(); register.add(new VarInsnNode(ALOAD,3));
        register.add(new MethodInsnNode(INVOKESTATIC,HELPER,"register","(LPRG/Yq;)V",false));
        ctor.instructions.insertBefore(end,register);
        InsnList fullSubtitle=new InsnList();
        fullSubtitle.add(new VarInsnNode(ALOAD,0));
        fullSubtitle.add(new FieldInsnNode(GETFIELD,"PRG/jo","a","LPRG/anh;"));
        fullSubtitle.add(new MethodInsnNode(INVOKEVIRTUAL,"PRG/anh","s","()LPRG/azK;",false));
        fullSubtitle.add(new MethodInsnNode(INVOKEVIRTUAL,"PRG/azK","f","()Ljava/lang/Object;",false));
        fullSubtitle.add(new TypeInsnNode(CHECKCAST,"PRG/amG"));
        fullSubtitle.add(new MethodInsnNode(INVOKEVIRTUAL,"PRG/amG","a","()LPRG/amn;",false));
        fullSubtitle.add(new MethodInsnNode(INVOKEVIRTUAL,"PRG/amn","a","()Ljava/lang/String;",false));
        subtitle.instructions.insertBefore(subtitleDraw,fullSubtitle);
        subtitle.instructions.set(subtitleDraw,new MethodInsnNode(INVOKESTATIC,HELPER,"drawSubtitle",REPLACEMENT,false));
        InsnList fullStory=new InsnList(); fullStory.add(new VarInsnNode(ALOAD,1));
        fullStory.add(new MethodInsnNode(INVOKEVIRTUAL,"PRG/Na$a","a","()LPRG/amn;",false));
        fullStory.add(new MethodInsnNode(INVOKEVIRTUAL,"PRG/amn","a","()Ljava/lang/String;",false));
        story.instructions.insertBefore(storyDraw,fullStory);
        story.instructions.set(storyDraw,new MethodInsnNode(INVOKESTATIC,HELPER,"drawStory",REPLACEMENT,false));
    }
    private static void requireSixteenStep(AbstractInsnNode draw) {
        AbstractInsnNode n=previous(draw);
        if(n.getOpcode()!=ISUB || previous(n).getOpcode()!=IMUL) fail("original16px line step tail");
        requireInteger(previous(previous(previous(n))),16);
    }
    private static ClassNode require(Map<String,ClassNode> all,String name) {
        ClassNode c=all.get(name); if(c==null || !c.name.equals(name) || c.version!=V1_8) fail("missing/version "+name); return c;
    }
    private static MethodNode method(ClassNode c,String name,String desc) {
        MethodNode result=null; for(MethodNode m:c.methods) if(m.name.equals(name)&&m.desc.equals(desc)) {
            if(result!=null) fail("duplicate method "+c.name+name); result=m;
        }
        if(result==null) fail("missing method "+c.name+name+desc); return result;
    }
    private static MethodInsnNode uniqueCall(MethodNode m,String owner,String name,String desc) {
        MethodInsnNode result=null;
        for(AbstractInsnNode n:m.instructions.toArray()) if(n instanceof MethodInsnNode) {
            MethodInsnNode c=(MethodInsnNode)n;
            if(c.owner.equals(owner)&&c.name.equals(name)&&c.desc.equals(desc)) { if(result!=null) fail("duplicate call "+owner+name); result=c; }
        }
        if(result==null) fail("missing call "+owner+name+desc); return result;
    }
    private static FieldInsnNode uniqueField(MethodNode m,int op,String owner,String name,String desc) {
        FieldInsnNode result=null;
        for(AbstractInsnNode n:m.instructions.toArray()) if(n instanceof FieldInsnNode) {
            FieldInsnNode f=(FieldInsnNode)n;
            if(f.getOpcode()==op&&f.owner.equals(owner)&&f.name.equals(name)&&f.desc.equals(desc)) { if(result!=null) fail("duplicate field "+name); result=f; }
        }
        if(result==null) fail("missing field "+owner+name); return result;
    }
    private static void requireCall(AbstractInsnNode n,String owner,String name,String desc) {
        if(!(n instanceof MethodInsnNode)) fail("expected call "+name);
        MethodInsnNode c=(MethodInsnNode)n; if(!c.owner.equals(owner)||!c.name.equals(name)||!c.desc.equals(desc)) fail("call identity "+name);
    }
    private static void requireVar(AbstractInsnNode n,int op,int local) {
        if(!(n instanceof VarInsnNode)||n.getOpcode()!=op||((VarInsnNode)n).var!=local) fail("variable identity");
    }
    private static void requireInteger(AbstractInsnNode n,int value) {
        if(!(n instanceof IntInsnNode)||((IntInsnNode)n).operand!=value) fail("constant "+value);
    }
    private static AbstractInsnNode previous(AbstractInsnNode n) {
        do { n=n.getPrevious(); } while(n!=null&&n.getOpcode()<0); if(n==null) fail("unexpected start"); return n;
    }
    private static void fail(String why) { throw new IllegalStateException("story12 preflight: "+why); }
}
