import PRG.RadioLabels;
import PRG.SN;
import java.lang.reflect.*;
import java.util.*;
import java.util.jar.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.util.regex.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

public final class RadioLabelsTest {
    static void check(boolean b, String m) { if (!b) throw new AssertionError(m); }
    static Map<String,ClassNode> readTargets(String path) throws Exception {
        Map<String,ClassNode> nodes=new LinkedHashMap<String,ClassNode>();
        try(JarFile jar=new JarFile(path)) {
            for(String n:new String[]{"PRG/JM","PRG/JQ"}) {
                JarEntry entry=jar.getJarEntry(n+".class");check(entry!=null,"missing target "+n);
                ClassNode c=new ClassNode();new ClassReader(jar.getInputStream(entry)).accept(c,0);nodes.put(n,c);
            }
        }
        return nodes;
    }
    static void checkCounts(Map<String,ClassNode> nodes,String context) {
        int lookup=0,display=0,draw=0,tint=0;
        for(ClassNode c:nodes.values())for(MethodNode m:c.methods)for(AbstractInsnNode n:m.instructions.toArray())if(n instanceof MethodInsnNode) {
            MethodInsnNode x=(MethodInsnNode)n;
            if(x.owner.equals("PRG/JF")&&x.name.equals("a")&&x.desc.equals("(Ljava/lang/String;LPRG/apr;)Ljava/lang/String;"))lookup++;
            if(x.owner.equals("PRG/RadioLabels")) {
                if(x.name.equals("display"))display++;
                if(x.name.equals("draw"))draw++;
                if(x.name.equals("drawTint"))tint++;
            }
        }
        check(lookup==4&&display==4&&draw==3&&tint==1,context+": lookup="+lookup+" display="+display+" draw="+draw+" tint="+tint);
    }
    public static void main(String[] args) throws Exception {
        if(args.length!=1&&args.length!=3)throw new IllegalArgumentException("base.jar [candidate.jar classic.fnt]");
        List<String[]> rows=new ArrayList<String[]>();
        Set<String> ids=new HashSet<String>();
        StringBuilder required=new StringBuilder();
        for(String line:Files.readAllLines(Paths.get("localization/editorial/r3-names/generated/radio-names.tsv"),StandardCharsets.UTF_8)) {
            if(line.startsWith("#")||line.startsWith("name_id"))continue;
            String[] row=line.split("\t",-1);check(row.length==4,"TSV columns");
            rows.add(row);ids.add(row[0]);required.append(row[2]);
        }
        check(ids.size()==36&&rows.size()==37,"36 names and Yifany alias");
        if(args.length==3) {
            Path candidate=Paths.get(args[1]).toRealPath();
            Path loaded=Paths.get(RadioLabels.class.getProtectionDomain().getCodeSource().getLocation().toURI()).toRealPath();
            check(candidate.equals(loaded),"RadioLabels must load from candidate.jar, not helper/classes/base: "+loaded);
            checkCounts(readTargets(args[1]),"actual candidate");
            Map<Integer,Map<String,Integer>> glyphs=new HashMap<Integer,Map<String,Integer>>();
            Pattern attribute=Pattern.compile("(\\w+)=(-?\\d+)");
            for(String line:Files.readAllLines(Paths.get(args[2]),StandardCharsets.UTF_8)) {
                if(!line.startsWith("char "))continue;
                Matcher matcher=attribute.matcher(line);
                Map<String,Integer> fields=new HashMap<String,Integer>();
                while(matcher.find())fields.put(matcher.group(1),Integer.valueOf(matcher.group(2)));
                check(fields.containsKey("id"),"font char id");
                check(glyphs.put(fields.get("id"),fields)==null,"duplicate font glyph");
            }
            for(char cp:required.toString().toCharArray()) {
                if(cp<128)continue;
                Map<String,Integer> g=glyphs.get((int)cp);
                check(g!=null,"required radio glyph "+Integer.toHexString(cp));
                check(Integer.valueOf(8).equals(g.get("width"))&&Integer.valueOf(8).equals(g.get("height"))
                    &&Integer.valueOf(8).equals(g.get("xadvance"))&&Integer.valueOf(0).equals(g.get("xoffset"))
                    &&Integer.valueOf(0).equals(g.get("yoffset")),"classic8 glyph metrics "+Integer.toHexString(cp));
            }
            for(char cp:(required.toString().toUpperCase(Locale.ROOT)+"[] :27.550").toCharArray()) {
                Map<String,Integer> g=glyphs.get((int)cp);
                check(g!=null&&Integer.valueOf(8).equals(g.get("xadvance")),"frequency ASCII grid advance");
            }
            System.out.println("RADIO_CANDIDATE_OK code_source=candidate names=36 classic8=8x8 advance=8 offsets=0");
        }
        final List<Object[]> draws=new ArrayList<Object[]>();
        SN sn=(SN)Proxy.newProxyInstance(SN.class.getClassLoader(),new Class<?>[]{SN.class},
            (p,m,a)->{draws.add(a);return null;});
        for(String[] row:rows)for(String name:new String[]{row[1],row[1].toUpperCase(Locale.ROOT),row[1].toLowerCase(Locale.ROOT)}) {
            boolean preserve=Boolean.parseBoolean(row[3]);
            String target=preserve?name:row[2];
            check(target.equals(RadioLabels.display(name)),"ledger mapping "+name);
            if(preserve)check(RadioLabels.display(name)==name,"preserve original case and identity");
            boolean chinese=target.chars().anyMatch(cp->cp>127);
            for(String role:new String[]{"default","classic","tint","glyph9"}) {
                String label="["+target+"]";
                RadioLabels.draw(sn,label,31,72,role);
                Object[] d=draws.get(draws.size()-1);
                check(d[0].equals(label)&&d[1].equals(31)&&d[2].equals(72)&&d[3].equals(chinese?"classic":role),"draw text/font/geometry "+name);
                check(target.length()<=6&&(target.length()+2)*8<=64,"bracket width");
                String field=target;while(field.length()<6)field+=" ";
                String frequency=field+":27.550";
                for(PRG.aBa color:new PRG.aBa[]{new PRG.aBa(1f,0f,0f,1f),new PRG.aBa(0f,1f,0.5f,0.25f)}) {
                    RadioLabels.drawTint(sn,frequency,12,20,color,role);
                    d=draws.get(draws.size()-1);
                    check(d[0].equals(frequency)&&d[1].equals(12)&&d[2].equals(20)&&d[3]==color&&d[4].equals(chinese?"classic":role),"tint text/color/font/geometry");
                }
                RadioLabels.drawTint(sn,frequency,-3,-7,null,role);
                d=draws.get(draws.size()-1);
                check(d[1].equals(-3)&&d[2].equals(-7)&&d[3]==null,"null tint and signed geometry");
                check(frequency.indexOf(':')*8==48&&frequency.length()*8==104,"frequency columns unchanged");
            }
        }
        for(String s:new String[]{"Mauser.Area0_map13_b","UNKNOWN","[MAUSER]","毛瑟","??????","JF","JM","JQ","static","Queen","High Lady",""})
            check(RadioLabels.display(s)==s,"unknown/script keys retain identity");
        check(RadioLabels.display(null)==null,"null");
        for(String text:new String[]{"UNKNOWN","??????","[??????]","??????:27.550",null}) {
            RadioLabels.draw(sn,text,1,2,"glyph9");
            check(draws.get(draws.size()-1)[3].equals("glyph9"),"unknown/hidden/null main font unchanged");
            RadioLabels.drawTint(sn,text,1,2,null,"glyph9");
            check(draws.get(draws.size()-1)[4].equals("glyph9"),"unknown/hidden/null tinted main font unchanged");
        }
        Map<String,ClassNode> nodes=new LinkedHashMap<String,ClassNode>();
        try(JarFile jar=new JarFile(args[0])) {
            for(String n:new String[]{"PRG/JM","PRG/JQ"}) {
                ClassNode c=new ClassNode();new ClassReader(jar.getInputStream(jar.getJarEntry(n+".class"))).accept(c,0);nodes.put(n,c);
            }
        }
        Map<String,ClassNode> incomplete=new LinkedHashMap<String,ClassNode>();
        incomplete.put("PRG/JM",nodes.get("PRG/JM"));
        boolean missing=false;try{RadioLabelsPatch.apply(incomplete);}catch(IllegalArgumentException e){missing=true;}
        check(missing,"missing target fails before mutation");
        Map<String,byte[]> original=new LinkedHashMap<String,byte[]>();
        for(ClassNode c:nodes.values()){ClassWriter w=new ClassWriter(0);c.accept(w);original.put(c.name,w.toByteArray());}
        RadioLabelsPatch.apply(nodes);
        int lookup=0,display=0,draw=0,tint=0;
        for(ClassNode c:nodes.values())for(MethodNode m:c.methods)for(AbstractInsnNode n:m.instructions.toArray())if(n instanceof MethodInsnNode) {
            MethodInsnNode x=(MethodInsnNode)n;
            if(x.owner.equals("PRG/JF")&&x.desc.equals("(Ljava/lang/String;LPRG/apr;)Ljava/lang/String;"))lookup++;
            if(x.owner.equals("PRG/RadioLabels")) {
                if(x.name.equals("display"))display++;
                if(x.name.equals("draw"))draw++;
                if(x.name.equals("drawTint"))tint++;
            }
        }
        check(lookup==4&&display==4&&draw==3&&tint==1,"exactly four lookup results, three labels and one frequency draw");
        boolean rejected=false;try{RadioLabelsPatch.apply(nodes);}catch(IllegalStateException e){rejected=true;}
        check(rejected,"double patch fails closed");
        // Undo only the documented four insertions/four draw adaptations. Every
        // other instruction, including ID lookup arguments and control flow, must match.
        for(ClassNode c:nodes.values()) {
            for(MethodNode m:c.methods)for(AbstractInsnNode n:m.instructions.toArray())if(n instanceof MethodInsnNode) {
                MethodInsnNode x=(MethodInsnNode)n;
                if(!x.owner.equals("PRG/RadioLabels"))continue;
                if(x.name.equals("display")){m.instructions.remove(x);continue;}
                x.setOpcode(Opcodes.INVOKEINTERFACE);x.owner="PRG/SN";x.name="a";
                x.desc="("+x.desc.substring("(LPRG/SN;".length());x.itf=true;
            }
            ClassWriter w=new ClassWriter(0);c.accept(w);
            check(Arrays.equals(original.get(c.name),w.toByteArray()),"unrelated bytecode unchanged: "+c.name);
        }
        System.out.println("RADIO_LABELS_OK names=36 aliases=37 displays=4 draws=3 tint=1 geometry=8px/48px/104px");
    }
}
