import PRG.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import cosmoloc.layout.*;

/** Frozen-r27 parser + actual anp/amH/amn/anh/jo integration; never runs Main/GL. */
@SuppressWarnings({"rawtypes", "unchecked"})
public final class VsnJoinIntegrationTest {
    static List<String> controls(aEO parsed) {
        List<String> out = new ArrayList<String>();
        for(aEO rest=parsed;!rest.b();rest=(aEO)rest.E()) {
            Object cmd=rest.s();
            if(!(cmd instanceof anp) && !(cmd instanceof amH))
                out.add(cmd.getClass().getName()+":"+cmd.toString());
        }
        return out;
    }
    static List<String> automatic(aEO parsed) {
        List<String> out = new ArrayList<String>();
        for(aEO rest=parsed;!rest.b();rest=(aEO)rest.E()) {
            Object cmd=rest.s();
            if(cmd instanceof amH) {
                amH a=(amH)cmd;
                out.add(a.e()+"/"+a.f()+"/"+ams.MODULE$.a(a.a(),amr.i.MODULE$.a()));
            }
        }
        return out;
    }
    public static void main(String[] args)throws Exception {
        try(java.io.InputStream in=new java.io.FileInputStream(args[0])) {
            VsnRuntimeAssertions.metrics=DialogueWrap.readMetrics(in);
        }
        VsnRuntimeAssertions.storyMetrics=StoryFont12.metrics();
        int files=0,oldTexts=0,newTexts=0,autoCount=0,controlCount=0;
        for(String row:Files.readAllLines(Paths.get(args[1]),StandardCharsets.UTF_8)) {
            String[] f=row.split("\t");
            String root=f[0];
            String original=new String(Files.readAllBytes(Paths.get(f[1])),StandardCharsets.UTF_8);
            String rewritten=new String(Files.readAllBytes(Paths.get(f[2])),StandardCharsets.UTF_8);
            aEO old=VsnRuntimeAssertions.parse(root,original), after=VsnRuntimeAssertions.parse(root,rewritten);
            VsnRuntimeAssertions.eq(controls(old),controls(after),"real parser ordered staging/actor/sound/sync events "+root);
            controlCount+=controls(old).size();
            VsnRuntimeAssertions.eq(automatic(old),automatic(after),"real parser complete auto duration/text/style unchanged "+root);
            autoCount+=automatic(old).size();
            List<String> expected=new ArrayList<String>();
            for(String line:rewritten.split("\\r\\n|\\r|\\n")) {
                if(line.startsWith("text: ") || line.startsWith("lang(") || line.startsWith("auto("))
                    expected.add(line.substring(line.indexOf(":")+1).trim());
            }
            for(aEO rest=old;!rest.b();rest=(aEO)rest.E())
                if(rest.s() instanceof anp || rest.s() instanceof amH)oldTexts++;
            int at=0;
            for(aEO rest=after;!rest.b();rest=(aEO)rest.E()) {
                Object cmd=rest.s();
                if(!(cmd instanceof anp) && !(cmd instanceof amH))continue;
                amr.h h=cmd instanceof amH?((amH)cmd).a():((anp)cmd).a();
                String text=ams.MODULE$.a(h,amr.i.MODULE$.a());
                VsnRuntimeAssertions.eq(text,expected.get(at++),"full real parser payload conserved "+root);
                VsnRuntimeAssertions.run((amW)cmd,text,"r28/"+root);
                newTexts++;
            }
            VsnRuntimeAssertions.eq(at,expected.size(),"all physical text commands parsed, no swallowed rows "+root);
            files++;
        }
        VsnRuntimeAssertions.eq(files,67,"all canonical PAK scripts");
        VsnRuntimeAssertions.eq(oldTexts,2388,"original real parser text count");
        VsnRuntimeAssertions.eq(newTexts,2064,"exact 324 reviewed text boundaries removed");
        VsnRuntimeAssertions.eq(autoCount,8,"all eight timed captions untouched");
        VsnRuntimeAssertions.tail();
        System.out.println("PASS VSN joins r27 parser integration: files="+files+" beforeText="+oldTexts+
            " afterText="+newTexts+" orderedControlNodes="+controlCount+" unchangedAuto="+autoCount+
            " actualJoPages="+VsnRuntimeAssertions.renderedPages+" manualOverflow="+VsnRuntimeAssertions.manualOverflow+
            " autoOverflow="+VsnRuntimeAssertions.autoOverflow+" checks="+VsnRuntimeAssertions.checks+
            "; exact parsed staging equality; every reveal/mask/skip/completion; original tail event once after last manual page; no game/GL/clip/CRT claim");
    }
}
