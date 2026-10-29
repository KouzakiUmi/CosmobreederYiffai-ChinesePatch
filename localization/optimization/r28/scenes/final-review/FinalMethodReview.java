import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Read-only archive audit; no game class loading, no patcher/apply invocation.
 * Independent inverse-whitelist checks on in-memory parsed candidate nodes. */
public final class FinalMethodReview implements Opcodes {
    static final List<String> TARGETS=Arrays.asList("PRG/amn","PRG/LY","PRG/Mb","PRG/Mn","PRG/Le","PRG/Lb","PRG/Lg","PRG/Ew","PRG/Jm","PRG/kn","PRG/Lx","PRG/Po","PRG/Kc");
    static final List<Object> failures=new ArrayList<Object>();
    static final Map<String,List<Object>> operations=new LinkedHashMap<String,List<Object>>();
    static String key(String c,String n,String d){return c+"."+n+d;}
    static Map<String,Object> map(Object... a){Map<String,Object> m=new LinkedHashMap<String,Object>();for(int i=0;i<a.length;i+=2)m.put((String)a[i],a[i+1]);return m;}
    static String json(Object value){
        if(value==null)return "null";if(value instanceof Number||value instanceof Boolean)return value.toString();
        if(value instanceof Map){StringBuilder b=new StringBuilder("{");for(Object e:((Map)value).entrySet()){Map.Entry p=(Map.Entry)e;if(b.length()>1)b.append(',');b.append(json(p.getKey())).append(':').append(json(p.getValue()));}return b.append('}').toString();}
        if(value instanceof Iterable){StringBuilder b=new StringBuilder("[");for(Object e:(Iterable)value){if(b.length()>1)b.append(',');b.append(json(e));}return b.append(']').toString();}
        StringBuilder b=new StringBuilder("\"");for(char c:value.toString().toCharArray()){if(c=='\"'||c=='\\')b.append('\\').append(c);else if(c<32)b.append(String.format("\\u%04x",(int)c));else b.append(c);}return b.append('\"').toString();
    }
    static String sha(byte[] bytes)throws Exception{StringBuilder s=new StringBuilder();for(byte b:MessageDigest.getInstance("SHA-256").digest(bytes))s.append(String.format("%02x",b&255));return s.toString();}
    static List<AbstractInsnNode> code(MethodNode m){List<AbstractInsnNode> out=new ArrayList<AbstractInsnNode>();for(AbstractInsnNode i:m.instructions)if(i.getOpcode()>=0)out.add(i);return out;}
    static String constant(Object o){if(o==null)return "null";return o.getClass().getName()+":"+o.toString();}
    static List<String> canonical(MethodNode m){
        List<String> out=new ArrayList<String>();
        out.add("METHOD "+m.name+m.desc+" access="+m.access+" signature="+m.signature+" exceptions="+m.exceptions);
        Map<LabelNode,Integer> positions=new IdentityHashMap<LabelNode,Integer>();int at=0;
        for(AbstractInsnNode i:m.instructions){if(i instanceof LabelNode)positions.put((LabelNode)i,at);if(i.getOpcode()>=0)at++;}
        for(AbstractInsnNode i:code(m)){
            String s=i.getOpcode()+":";
            if(i instanceof VarInsnNode)s+=((VarInsnNode)i).var;
            else if(i instanceof IntInsnNode)s+=((IntInsnNode)i).operand;
            else if(i instanceof TypeInsnNode)s+=((TypeInsnNode)i).desc;
            else if(i instanceof FieldInsnNode){FieldInsnNode n=(FieldInsnNode)i;s+=n.owner+"."+n.name+n.desc;}
            else if(i instanceof MethodInsnNode){MethodInsnNode n=(MethodInsnNode)i;s+=n.owner+"."+n.name+n.desc+" itf="+n.itf;}
            else if(i instanceof InvokeDynamicInsnNode){InvokeDynamicInsnNode n=(InvokeDynamicInsnNode)i;s+=n.name+n.desc+" bsm="+n.bsm;for(Object b:n.bsmArgs)s+=" | "+constant(b);}
            else if(i instanceof JumpInsnNode)s+=positions.get(((JumpInsnNode)i).label);
            else if(i instanceof LdcInsnNode)s+=constant(((LdcInsnNode)i).cst);
            else if(i instanceof IincInsnNode){IincInsnNode n=(IincInsnNode)i;s+=n.var+","+n.incr;}
            else if(i instanceof TableSwitchInsnNode){TableSwitchInsnNode n=(TableSwitchInsnNode)i;s+=n.min+","+n.max+","+positions.get(n.dflt);for(LabelNode l:n.labels)s+=","+positions.get(l);}
            else if(i instanceof LookupSwitchInsnNode){LookupSwitchInsnNode n=(LookupSwitchInsnNode)i;s+=positions.get(n.dflt);for(int j=0;j<n.keys.size();j++)s+=","+n.keys.get(j)+"->"+positions.get(n.labels.get(j));}
            else if(i instanceof MultiANewArrayInsnNode){MultiANewArrayInsnNode n=(MultiANewArrayInsnNode)i;s+=n.desc+","+n.dims;}
            out.add(s);
        }
        for(TryCatchBlockNode t:m.tryCatchBlocks)out.add("CATCH "+positions.get(t.start)+","+positions.get(t.end)+","+positions.get(t.handler)+","+t.type);
        return out;
    }
    static Map<String,MethodNode> methods(ClassNode c){Map<String,MethodNode> m=new LinkedHashMap<String,MethodNode>();for(MethodNode n:c.methods)m.put(n.name+n.desc,n);return m;}
    static MethodNode need(ClassNode c,String name,String desc){MethodNode m=methods(c).get(name+desc);if(m==null)throw new IllegalStateException("Missing "+c.name+name+desc);return m;}
    static ClassNode node(byte[] b){ClassNode c=new ClassNode(ASM8);new ClassReader(b).accept(c,ClassReader.EXPAND_FRAMES);return c;}
    static AbstractInsnNode previousCode(AbstractInsnNode n){do{n=n.getPrevious();}while(n!=null&&n.getOpcode()<0);return n;}
    static void record(String key,Object row){operations.computeIfAbsent(key,k->new ArrayList<Object>()).add(row);}
    /** Assert exact new call and its inserted extra receiver, then invert only it. */
    static void inverse(Map<String,ClassNode> classes,String c,String method,String desc,String helper,String hname,String hdesc,int count,int oldOp,String owner,String oldName,String oldDesc,int insertedLocal){
        MethodNode m=need(classes.get(c),method,desc);List<MethodInsnNode> matches=new ArrayList<MethodInsnNode>();
        for(AbstractInsnNode i:m.instructions)if(i instanceof MethodInsnNode){MethodInsnNode n=(MethodInsnNode)i;if(n.getOpcode()==INVOKESTATIC&&n.owner.equals(helper)&&n.name.equals(hname)&&n.desc.equals(hdesc)&&!n.itf)matches.add(n);}
        if(matches.size()!=count)throw new IllegalStateException("Whitelist call count "+key(c,method,desc)+" "+hname+" "+matches.size()+" != "+count);
        for(MethodInsnNode n:matches){
            if(insertedLocal>=0){AbstractInsnNode p=previousCode(n);if(!(p instanceof VarInsnNode)||p.getOpcode()!=ALOAD||((VarInsnNode)p).var!=insertedLocal)throw new IllegalStateException("Inserted ALOAD mismatch");m.instructions.remove(p);}
            m.instructions.set(n,new MethodInsnNode(oldOp,owner,oldName,oldDesc,oldOp==INVOKEINTERFACE));
        }
        record(key(c,method,desc),map("kind","call_replacement","count",count,"candidate",helper+"."+hname+hdesc,"baseline",owner+"."+oldName+oldDesc,"inserted_aload_local",insertedLocal));
    }
    static final String F="(Ljava/lang/String;LPRG/amq;LPRG/amv;Z)Ljava/lang/String;";
    static final String FH="(LPRG/amw;Ljava/lang/String;LPRG/amq;LPRG/amv;Z)Ljava/lang/String;";
    static final String P="(Ljava/lang/String;IILjava/lang/String;)V";
    static final String PH="(LPRG/SN;Ljava/lang/String;IILjava/lang/String;)V";
    static void scene(Map<String,ClassNode> c,String cl,String mn,String md,String hn,String hd,int count,int oldOp,String oo,String on,String od,int local){inverse(c,cl,mn,md,"PRG/SceneText",hn,hd,count,oldOp,oo,on,od,local);}
    static void reverseWhitelist(Map<String,ClassNode> c,Map<String,ClassNode> base){
        inverse(c,"PRG/amn","a","(DZ)I","PRG/DialogueWrap","terminalText","(LPRG/amr$e;Ljava/lang/String;)Ljava/lang/String;",1,INVOKEVIRTUAL,"PRG/amr$e","c","(Ljava/lang/String;)Ljava/lang/String;",-1);
        for(String[] s:new String[][]{{"PRG/LY","saveRow"},{"PRG/LY","saveLower"},{"PRG/Mb","name"}})
            inverse(c,s[0],"b","(LPRG/SN;)V","PRG/CompactFields",s[1],"(LPRG/Id;LPRG/SN;Ljava/lang/String;II)V",1,INVOKEVIRTUAL,"PRG/Id","a","(LPRG/SN;Ljava/lang/String;II)V",-1);
        inverse(c,"PRG/Mb","b","(LPRG/SN;)V","PRG/CompactFields","nameCursor","(LPRG/SN;Ljava/lang/String;IIIILPRG/Mb;)V",1,INVOKEINTERFACE,"PRG/SN","a","(Ljava/lang/String;IIII)V",0);
        inverse(c,"PRG/Mn","b","(LPRG/SN;)V","PRG/CompactFields","letter",PH,1,INVOKEINTERFACE,"PRG/SN","a",P,-1);
        inverse(c,"PRG/Mn","a","(LPRG/SN;LPRG/aab;)V","PRG/CompactFields","selectedLetter","(LPRG/SN;Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V",1,INVOKEINTERFACE,"PRG/SN","a","(Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V",-1);
        for(String[] s:new String[][]{{"Lg","registerName"},{"Lb","registerDescription"}})
            inverse(c,"PRG/Le","<init>","(LPRG/apr;)V","PRG/ItemFont8",s[1],"(LPRG/"+s[0]+";LPRG/Le;)V",1,INVOKESTATIC,"PRG/ItemFont8",s[1],"(LPRG/"+s[0]+";)V",0);
        for(String[] s:new String[][]{{"Lb","update"},{"Lg","updateName"}}){
            MethodNode m=need(c.get("PRG/"+s[0]),"a","(F)V");List<AbstractInsnNode> ins=code(m);
            if(ins.size()!=4||!(ins.get(0) instanceof VarInsnNode)||ins.get(0).getOpcode()!=ALOAD||((VarInsnNode)ins.get(0)).var!=0||!(ins.get(1) instanceof VarInsnNode)||ins.get(1).getOpcode()!=FLOAD||((VarInsnNode)ins.get(1)).var!=1||!(ins.get(2) instanceof MethodInsnNode)||ins.get(3).getOpcode()!=RETURN)throw new IllegalStateException("Clock-hook exact shape");
            MethodInsnNode n=(MethodInsnNode)ins.get(2);
            if(n.getOpcode()!=INVOKESTATIC||!n.owner.equals("PRG/ItemFont8")||!n.name.equals(s[1])||!n.desc.equals("(LPRG/"+s[0]+";F)V")||n.itf)throw new IllegalStateException("Clock-hook target");
            for(int i=0;i<3;i++)m.instructions.remove(ins.get(i));
            record(key("PRG/"+s[0],"a","(F)V"),map("kind","clock_hook_only","added",Arrays.asList("ALOAD 0","FLOAD 1",n.owner+"."+n.name+n.desc),"original_return_preserved",true));
        }
        String ew="(LPRG/SN;Z)V";
        scene(c,"PRG/Ew","a",ew,"breedAffinity",FH.replace(")","LPRG/SN;)"),1,INVOKEVIRTUAL,"PRG/amw","a",F,1);
        scene(c,"PRG/Ew","a",ew,"breedNeeds",FH.replace(")","LPRG/SN;)"),1,INVOKEVIRTUAL,"PRG/amw","a",F,1);
        scene(c,"PRG/Ew","a",ew,"breedDraw",PH,2,INVOKEINTERFACE,"PRG/SN","a",P,-1);
        scene(c,"PRG/Ew","a","(LPRG/SN;ILPRG/aAJ;)V","breedDraw",PH,1,INVOKEINTERFACE,"PRG/SN","a",P,-1);
        String jm="(LPRG/Jm;LPRG/SN;LPRG/At;)V";
        scene(c,"PRG/Jm","a",jm,"cardFormat",FH,2,INVOKEVIRTUAL,"PRG/amw","a",F,-1);
        scene(c,"PRG/Jm","a",jm,"cardDraw",PH,1,INVOKEINTERFACE,"PRG/SN","a",P,-1);
        scene(c,"PRG/Jm","a","(LPRG/Jm;LPRG/SN;ILPRG/aAJ;)V","cardDraw",PH,1,INVOKEINTERFACE,"PRG/SN","a",P,-1);
        scene(c,"PRG/kn","a","(Ljava/lang/String;LPRG/SH;LPRG/km;LPRG/SN;D)V","achievementFormat",FH,1,INVOKEVIRTUAL,"PRG/amw","a",F,-1);
        scene(c,"PRG/kn","a","(LPRG/km;LPRG/SN;LPRG/aAJ;)V","achievementDraw",PH,1,INVOKEINTERFACE,"PRG/SN","a",P,-1);
        scene(c,"PRG/kn","a","(LPRG/ka;LPRG/SH;LPRG/SN;D)V","achievementDraw","(LPRG/SN;Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V",1,INVOKEINTERFACE,"PRG/SN","a","(Ljava/lang/String;IILPRG/aBa;Ljava/lang/String;)V",-1);
        scene(c,"PRG/Lx","a","(LPRG/SN;Z)V","mapCenter","(LPRG/SN;Ljava/lang/String;ILjava/lang/String;)I",1,INVOKEINTERFACE,"PRG/SN","a","(Ljava/lang/String;ILjava/lang/String;)I",-1);
        scene(c,"PRG/Po","a","(LPRG/apr;LPRG/SH;LPRG/SN;I)V","mapDraw",PH,1,INVOKEINTERFACE,"PRG/SN","a",P,-1);
        // Kc is the single tail replacement, independently prove prefix through
        // the sole full-source ASTORE9 and the exact new 8-instruction tail.
        MethodNode now=need(c.get("PRG/Kc"),"b","(LPRG/SN;ZI)V"),old=need(base.get("PRG/Kc"),"b","(LPRG/SN;ZI)V");
        List<String> n=canonical(now),b=canonical(old);int cut=-1,oldCut=-1;
        for(int i=0;i<n.size();i++)if(n.get(i).equals(ASTORE+":9")){if(cut>=0)throw new IllegalStateException("Kc duplicate source");cut=i;}
        for(int i=0;i<b.size();i++)if(b.get(i).equals(ASTORE+":9")){if(oldCut>=0)throw new IllegalStateException("Kc baseline duplicate source");oldCut=i;}
        List<String> tail=Arrays.asList(ALOAD+":1",ALOAD+":9",ILOAD+":2",ILOAD+":4",ILOAD+":6",ILOAD+":3",INVOKESTATIC+":PRG/SceneText.dataBlock(LPRG/SN;Ljava/lang/String;ZIII)V itf=false",RETURN+":");
        boolean prefix=cut==oldCut&&cut>=0&&n.subList(0,cut+1).equals(b.subList(0,oldCut+1));
        boolean exactTail=cut>=0&&n.subList(cut+1,n.size()).equals(tail);
        record(key("PRG/Kc","b","(LPRG/SN;ZI)V"),map("kind","full_source_tail_only","prefix_including_source_store_identical",prefix,"prefix_logical_instructions",cut,"exact_eight_instruction_tail",exactTail,"tail",tail,"baseline_removed_tail",b.subList(oldCut+1,b.size())));
        if(!prefix||!exactTail)throw new IllegalStateException("Kc prefix/tail whitelist");
        // For uniform all-method comparison below use only the already-verified
        // original method for this one tail. No archive is ever emitted.
        int index=c.get("PRG/Kc").methods.indexOf(now);c.get("PRG/Kc").methods.set(index,old);
    }
    static String meta(ClassNode c){StringBuilder s=new StringBuilder();s.append(c.version).append('|').append(c.access).append('|').append(c.name).append('|').append(c.superName).append('|').append(c.signature).append('|').append(c.interfaces).append('|').append(c.outerClass).append('|').append(c.outerMethod).append('|').append(c.outerMethodDesc).append('|').append(c.nestHostClass).append('|').append(c.nestMembers);
        for(FieldNode f:c.fields)s.append("\nFIELD ").append(f.access).append('|').append(f.name).append('|').append(f.desc).append('|').append(f.signature).append('|').append(constant(f.value));
        for(InnerClassNode n:c.innerClasses)s.append("\nINNER ").append(n.name).append('|').append(n.outerName).append('|').append(n.innerName).append('|').append(n.access);
        return s.toString();}
    static Map<String,byte[]> archive(Path path)throws Exception{Map<String,byte[]> out=new TreeMap<String,byte[]>();try(JarFile jar=new JarFile(path.toFile())){Enumeration<JarEntry> e=jar.entries();while(e.hasMoreElements()){JarEntry n=e.nextElement();if(n.getName().endsWith(".class"))out.put(n.getName(),jar.getInputStream(n).readAllBytes());}}return out;}
    public static void main(String[] args)throws Exception{
        if(args.length!=3)throw new IllegalArgumentException("r27.jar candidate.jar NEW-review.json");
        Path first=Paths.get(args[0]).toRealPath(),last=Paths.get(args[1]).toRealPath(),output=Paths.get(args[2]).toAbsolutePath().normalize();
        if(Files.exists(output)||!output.startsWith(Paths.get("localization/optimization/r28/scenes/final-review").toAbsolutePath().normalize()))throw new IllegalArgumentException("New audit-only output");
        Map<String,byte[]> a=archive(first),z=archive(last);List<String> changed=new ArrayList<String>(),added=new ArrayList<String>(),removed=new ArrayList<String>();
        for(String k:a.keySet())if(!z.containsKey(k))removed.add(k);else if(!Arrays.equals(a.get(k),z.get(k)))changed.add(k);
        for(String k:z.keySet())if(!a.containsKey(k))added.add(k);
        List<String> actualTargets=new ArrayList<String>();for(String t:TARGETS)actualTargets.add(t+".class");Collections.sort(actualTargets);
        // Existing layout helpers are source-recompiled and not target rewrites.
        List<String> targetChanges=new ArrayList<String>(),helperChanges=new ArrayList<String>();
        Set<String> knownHelpers=new HashSet<String>(Arrays.asList("PRG/DialogueWrap.class","PRG/DialogueWrap$1.class","PRG/DialogueWrap$FontHolder.class","PRG/SubtitleLayout.class","PRG/SubtitleLayout$Font.class","PRG/SubtitleLayout$PageCommand.class","PRG/StoryFont12.class","PRG/StoryFont12$Font.class","PRG/StoryFont12$Metrics.class","PRG/EndingReportLayout.class","PRG/ItemFont8.class"));
        for(String k:changed){if(actualTargets.contains(k))targetChanges.add(k);else if(knownHelpers.contains(k)||k.startsWith("cosmoloc/layout/"))helperChanges.add(k);else failures.add("Unexpected preexisting class change "+k);}
        if(!targetChanges.equals(actualTargets)||!removed.isEmpty())failures.add("Target set mismatch or removed class");
        Map<String,ClassNode> base=new LinkedHashMap<String,ClassNode>(),finals=new LinkedHashMap<String,ClassNode>(),reversed=new LinkedHashMap<String,ClassNode>();
        for(String t:TARGETS){base.put(t,node(a.get(t+".class")));finals.put(t,node(z.get(t+".class")));reversed.put(t,node(z.get(t+".class")));}
        try{reverseWhitelist(reversed,base);}catch(Exception e){failures.add(e.toString());}
        List<Object> records=new ArrayList<Object>();int same=0,different=0;
        for(String t:TARGETS){ClassNode before=base.get(t),after=finals.get(t),undo=reversed.get(t);Map<String,MethodNode> old=methods(before),now=methods(after),rev=methods(undo);boolean metadata=meta(before).equals(meta(after)),sets=old.keySet().equals(now.keySet());
            if(!metadata||!sets)failures.add(t+" metadata/method set changed");List<Object> rows=new ArrayList<Object>();
            for(String k:old.keySet()){MethodNode m=old.get(k),v=now.get(k),r=rev.get(k);List<String> left=canonical(m),right=v==null?Collections.emptyList():canonical(v);boolean equal=left.equals(right),inverted=r!=null&&left.equals(canonical(r));String id=key(t,m.name,m.desc);boolean listed=operations.containsKey(id);
                if(equal)same++;else different++;
                if(!equal&&(!listed||!inverted))failures.add("Unwhitelisted method difference "+id);
                if(equal&&listed)failures.add("Whitelist unexpectedly no-op "+id);
                rows.add(map("method",m.name,"descriptor",m.desc,"baseline_logic_sha256",sha(String.join("\n",left).getBytes(StandardCharsets.UTF_8)),"candidate_logic_sha256",sha(String.join("\n",right).getBytes(StandardCharsets.UTF_8)),"identical",equal,"whitelisted",listed,"exact_match_after_independent_inverse",inverted,"changes",operations.get(id),"baseline_instructions",equal?null:left,"candidate_instructions",equal?null:right));
            }
            records.add(map("class",t,"baseline_raw_sha256",sha(a.get(t+".class")),"candidate_raw_sha256",sha(z.get(t+".class")),"class_metadata_and_field_schema_identical",metadata,"method_descriptor_set_identical",sets,"methods",rows));
        }
        List<Object> guards=new ArrayList<Object>();for(String t:Arrays.asList("PRG/Mf","PRG/Iu","PRG/Mc","PRG/Id","PRG/It","PRG/LX","PRG/GB","PRG/FM","PRG/Hi")){boolean eq=a.containsKey(t+".class")&&Arrays.equals(a.get(t+".class"),z.get(t+".class"));guards.add(map("class",t,"raw_bytes_identical",eq));if(!eq)failures.add("Protected class changed/missing "+t);}
        Map<String,Object> report=map("status",failures.isEmpty()?"PASS_STATIC_METHOD_WHITELIST":"FAIL","baseline_jar",first.toString(),"candidate_jar",last.toString(),"baseline_jar_sha256",sha(Files.readAllBytes(first)),"candidate_jar_sha256",sha(Files.readAllBytes(last)),"method_normalization","Ignore debug/frame/max_stack/max_locals/constant-pool numbering; retain opcode, all operands, owner/name/descriptor/itf, handles/bootstrap arguments, branch/switch logical instruction destinations, try/catch boundaries, access/signature/exceptions.","review_scope","13 existing target classes; compare all methods and inverse only independently enumerated draw/format/clock hooks. No apply() or candidate mutation; only in-memory audit nodes normalized.","same_methods",same,"changed_methods",different,"whitelist_methods",operations.size(),"preexisting_target_changes",targetChanges,"existing_helper_changes_outside_target_scope",helperChanges,"added_class_entries",added,"removed_class_entries",removed,"protected_classes",guards,"failures",failures,"classes",records);
        Files.write(output,json(report).getBytes(StandardCharsets.UTF_8));System.out.println("METHOD_REVIEW "+report.get("status")+" identical="+same+" changed="+different+" whitelist="+operations.size()+" failures="+failures.size());if(!failures.isEmpty())throw new AssertionError(failures.toString());
    }
}
