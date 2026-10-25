import PRG.*;
import cosmoloc.layout.*;
import java.io.*;
import java.lang.reflect.*;
import java.nio.file.*;
import java.util.*;
import java.util.zip.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Isolated fixtures: never starts the game or loads native graphics. */
public final class VsnLayoutTest {
    static final String[] TEXTS = {
        "这是超光速航行与先进赛博机器人技术的时代。",
        "[3P组织]已成为推动太空探索的一股重要力量。",
        "[3P组织]派出英勇之士，前往各地收集情报。",
        "这些被称为[宇宙育种者]的英雄，让文明得以繁荣。",
        "穿行群星，探寻未知，这就是冒险的人生。",
        "人人敬仰，许多孩子梦想长大后成为[宇宙育种者]。",
        "然而，离开安稳的家园、踏上星际旅途，绝非胆小者所能为。",
        "毕竟，谁又能说清遥远的未知星球上潜藏着什么危险……"
    };
    static String fontPath;
    static amH[] fixtureCommands;
    public static void main(String[] args) throws Exception {
        if (args.length > 0 && args[0].equals("--fnt")) fontPath = args[1];
        if (args.length > 0 && args[0].equals("--parse")) {
            parserTrace(args[1]); return;
        }
        if (args.length > 0 && args[0].equals("--fingerprints")) {
            Map<String, ClassNode> nodes = nodes(args[1]);
            System.out.println("JO=" + VsnPatch.fingerprint(VsnPatch.method(nodes.get("PRG/jo"), "a", VsnPatch.CALLBACK)));
            System.out.println("JL=" + VsnPatch.fingerprint(VsnPatch.method(nodes.get("PRG/jl"), "a", VsnPatch.COMPOSE)));
            System.out.println("AMH=" + VsnPatch.fingerprint(VsnPatch.method(nodes.get("PRG/amH"), "a", VsnPatch.CREATE)));
            System.out.println("AMN=" + VsnPatch.fingerprint(VsnPatch.method(nodes.get("PRG/amn"), "a", VsnPatch.COPY)));
            return;
        }
        if (args.length > 0 && args[0].equals("--transform")) {
            transform(args[1], Paths.get(args[2])); return;
        }
        if (args.length > 0 && args[0].equals("--baseline")) {
            fixtureCommands = parserTrace(args[1]);
            for (int i = 0; i < 8; i++) eq(ams.MODULE$.a(fixtureCommands[i].a(), amr.i.MODULE$.a()), TEXTS[i], "real r21 parser final text " + i);
            if (args.length > 3) fontPath = args[3];
        }
        formatterAndReveal();
        runtime();
        if (args.length > 0 && args[0].equals("--baseline")) englishNonTarget(parserTrace(args[2]));
        System.out.println("VSN tests PASS: original formatter + all 85 reveal positions x8, exact-parent copy/skip propagation, negative copy/event gates, identity/role/profile gates, bounded ASM/tail and JVM verification");
    }
    static void formatterAndReveal() throws Exception {
        PixelLayout.Metrics ten = new PixelLayout.Metrics() {
            public PixelLayout.Glyph glyph(int cp) { return new PixelLayout.Glyph(cp < 128 ? 8 : 10, 0, 0, cp == 32 ? 0 : cp < 128 ? 8 : 10, 10); }
            public double kerning(int a, int b) { return 0; }
        };
        if (fontPath != null) ten = LayoutBridge.metrics(font());
        PixelLayout.Profile p = new PixelLayout.Profile(new PixelLayout.Rect(0, 0, 224, 48), 16, PixelLayout.Insets.NONE);
        for (int i = 0; i < TEXTS.length; i++) {
            String value = ((amr.d) amw.MODULE$.a(TEXTS[i], Ol.MODULE$, Om.MODULE$).s()).a();
            eq(value, VsnLayout.expectedAnimated(i), "actual formatter trace " + i);
            PixelLayout.Plan plan = PixelLayout.layout(TEXTS[i], ten, p, VsnLayout.sourceMap(i));
            check(!plan.overflow, "candidate fits offline profile");
            StringBuilder complete = new StringBuilder();
            for (PixelLayout.Line line : plan.lines) complete.append(TEXTS[i].substring(line.display.start, line.display.end));
            eq(complete.toString(), TEXTS[i], "content conservation");
            for (int r = 0; r <= value.length(); r++) {
                String originalMask = amw.MODULE$.a(value, r);
                StringBuilder displayed = new StringBuilder();
                for (PixelLayout.VisiblePrefix visible : plan.visiblePrefixes(r)) {
                    displayed.append(TEXTS[i].substring(visible.line.display.start, visible.displayEnd));
                    check(visible.line.originX == plan.lines.get(visible.line.index).originX, "fixed x");
                    check(visible.line.originY == plan.lines.get(visible.line.index).originY, "fixed y");
                }
                int expected = Math.min(TEXTS[i].length(), r);
                if (i == 7 && expected == TEXTS[i].length() - 1) expected--; // atomic six-dot ellipsis
                eq(displayed.toString(), TEXTS[i].substring(0, expected), "original UTF16 reveal map " + i + "/" + r);
                // Every retained source character must be present at its mapped original coordinate.
                for (PixelLayout.SourceRange range : VsnLayout.sourceMap(i))
                    if (range.source.end <= r) check(originalMask.charAt(range.source.start) == TEXTS[i].charAt(range.display.start), "source mask agreement");
            }
        }
    }
    static void runtime() throws Exception {
        amH[] commands = new amH[8];
        int[] offsets = {86, 120, 220, 255, 356, 389, 520, 571};
        for (int i = 0; i < 8; i++) commands[i] = new amH(new amr.h(TEXTS[i], "vsn.ClassicPreTitle." + offsets[i]), 8.0, "default");
        if (fixtureCommands != null) commands = fixtureCommands;
        aEO<amW> list = (aEO<amW>)(aEO<?>)aFC.MODULE$;
        for (int i = 7; i >= 0; i--) list = list.b((amW)commands[i]);
        amU source = new amU("ClassicPreTitle", null, null, null, list);
        anh state = new anh(null, 100.0, null, null, null, null, true, null, null, null, null);
        VsnLayout.observe(state, source);
        List<String> draws = new ArrayList<String>();
        List<String> order = new ArrayList<String>();
        arp font = font();
        SN sn = (SN)Proxy.newProxyInstance(VsnLayoutTest.class.getClassLoader(), new Class<?>[]{SN.class, FontAccess.class}, (proxy, method, arguments) -> {
            if (method.getName().equals("cosmo$layoutFont")) return font;
            if (method.getName().equals("b") && method.getParameterCount() == 0) return "default";
            if (method.getName().equals("a") && method.getParameterCount() == 4 && method.getParameterTypes()[0] == String.class) {
                draws.add(arguments[0] + "@" + arguments[1] + "," + arguments[2]); order.add("text"); return null;
            }
            if (method.getName().equals("a") && method.getParameterCount() == 5 && "WhiteFill".equals(arguments[0])) { order.add("hint"); return null; }
            if (method.getReturnType() == boolean.class) return false;
            if (method.getReturnType() == int.class) return 0;
            return null;
        });
        amn animated = null;
        amn[] animations = new amn[8];
        amX metadata = new amX(null, Ol.MODULE$, Om.MODULE$, null);
        for (int i = 0; i < 8; i++) {
            anh result = commands[i].a(state, metadata);
            amn captured = ((amG)result.f().f()).a();
            eq(captured.a(), VsnLayout.expectedAnimated(i), "real amH -> amn trace");
            eq(VsnLayout.status(captured), "CAPTURED_UNBOUND_SOURCE", "ASM amH capture hook executed");
            animations[i] = captured;
            if (i == 0) animated = captured;
        }
        final amn active = animated;
        String mask = amw.MODULE$.a(animated.a(), 84);
        check(!VsnLayout.draw(state, sn, "", false, animated, 84, mask, 16, 54), "unknown rect stays OFF");
        eq(VsnLayout.status(animated), "BLOCKED_UNVERIFIED_RECT", "explicit blocked status");
        PixelLayout.Profile p = new PixelLayout.Profile("ClassicPreTitle", "offline-candidate", new PixelLayout.Rect(0, 0, 224, 48), 16, PixelLayout.Insets.NONE);
        System.setProperty("cosmo.layout.vsn.prototype", "true");
        expectFailure(() -> VsnLayout.observe(state, source), "property profile must be complete");
        String[] keys = {"x", "y", "width", "height", "lineStep", "effectLeft", "effectTop", "effectRight", "effectBottom"};
        String[] values = {"0", "0", "224", "48", "16", "0", "0", "0", "0"};
        for (int i = 0; i < keys.length; i++) System.setProperty("cosmo.layout.vsn." + keys[i], values[i]);
        VsnLayout.observe(state, source);
        check(VsnLayout.draw(state, sn, "", false, animated, 84, mask, 16, 54), "actual property activation path");
        VsnLayout.disablePrototype(source);
        for (String key : keys) System.clearProperty("cosmo.layout.vsn." + key);
        System.clearProperty("cosmo.layout.vsn.prototype");
        VsnLayout.enablePrototype(source, p, "synthetic offline fixture; NOT scene verified");
        check(VsnLayout.draw(state, sn, "", false, animated, 84, mask, 16, 54), "explicit prototype");
        check(!draws.isEmpty(), "actual SN line draw bridge invoked");
        anh composed = new anh(null, 100.0, null, null, null, null, true, null, null, null, null);
        Method compose = jl.class.getDeclaredMethod("a", ZJ.class, amq.class, int.class, int.class,
            boolean.class, int.class, int.class, SN.class, anh.class, amU.class);
        try {
            compose.invoke(null, null, Ol.MODULE$, 16, 54, false, 0, 0, sn, composed, source);
            throw new AssertionError("SV-less composition fixture must stop before graphics");
        } catch (InvocationTargetException expected) {
            check(expected.getCause() instanceof NullPointerException, "composition stops on intentionally absent SV");
        }
        check(VsnLayout.draw(composed, sn, "default", false, animated, 84, mask, 16, 54), "real jl hook associated exact anh with exact amU before graphics");
        for (int i = 0; i < 8; i++) {
            for (int r = 0; r <= 84; r++) {
                draws.clear();
                check(VsnLayout.draw(state, sn, "default", false, animations[i], r,
                    amw.MODULE$.a(animations[i].a(), r), 16, 54), "actual adapter all reveal indices");
                StringBuilder visible = new StringBuilder();
                for (String drawn : draws) visible.append(drawn.substring(0, drawn.lastIndexOf('@')));
                int expected = Math.min(r, TEXTS[i].length());
                if (i == 7 && expected == TEXTS[i].length() - 1) expected--;
                eq(visible.toString(), TEXTS[i].substring(0, expected), "actual bridge full/reveal conservation");
            }
        }
        for (int i = 0; i < 8; i++) {
            amn parent = animations[i];
            draws.clear();
            check(VsnLayout.draw(state, sn, "default", false, parent, 84, amw.MODULE$.a(parent.a(), 84), 16, 54), "parent full-frame fixture");
            List<String> parentFrame = new ArrayList<String>(draws);
            azK<Object> skip = new aAw<Object>(Double.valueOf(100.5));
            amn copy = parent.a(parent.a(), parent.e(), skip, parent.g());
            check(copy != parent && copy.a() == parent.a(), "real copier returns fresh original child with original text argument");
            check(copy.f() == skip && copy.e() == parent.e() && copy.g() == parent.g(), "copier parameters/timing untouched");
            eq(VsnLayout.status(copy), "CAPTURED_UNBOUND_SOURCE", "real amn hook inherited exact parent provenance");
            for (int r = 0; r <= 84; r++) {
                draws.clear();
                check(VsnLayout.draw(state, sn, "default", false, copy, r, amw.MODULE$.a(copy.a(), r), 16, 54), "copied animation all reveal indices");
                StringBuilder visible = new StringBuilder();
                for (String drawn : draws) visible.append(drawn.substring(0, drawn.lastIndexOf('@')));
                int expected = Math.min(r, TEXTS[i].length());
                if (i == 7 && expected == TEXTS[i].length() - 1) expected--;
                eq(visible.toString(), TEXTS[i].substring(0, expected), "copy full/reveal conservation");
            }
            eq(draws, parentFrame, "copied full frame retains exact parent line origins");
            int completion = copy.a(100.5, true);
            eq(copy.i(), 100.5, "copied original completion deadline unchanged");
            eq(completion, TEXTS[i].length(), "real copied skip deadline completes original reveal");
            check(VsnLayout.draw(state, sn, "default", false, copy, completion, amw.MODULE$.a(copy.a(), completion), 16, 54), "normal skip copy can draw completion");
            amn grandchild = copy.a(copy.a(), copy.e(), skip, copy.g());
            check(VsnLayout.draw(state, sn, "default", false, grandchild, completion, amw.MODULE$.a(grandchild.a(), completion), 16, 54), "multi-generation exact copy provenance");
            check(VsnLayout.inherit(parent, copy) == copy, "bridge never replaces original return child");
        }
        amn changedText = animated.a(animated.a() + "X", animated.e(), animated.f(), animated.g());
        eq(VsnLayout.status(changedText), "UNBOUND_ANIMATION", "changed text copier does not inherit");
        amn unbound = new amn(animated.a(), animated.e(), animated.f(), animated.g());
        amn unboundCopy = unbound.a(unbound.a(), 17.0, unbound.f(), .125f);
        eq(VsnLayout.status(unboundCopy), "UNBOUND_ANIMATION", "equal-text unbound receiver never inherits");
        check(unboundCopy.a().equals(unbound.a()) && unboundCopy.e() == 17.0 && unboundCopy.f() == unbound.f() && unboundCopy.g() == .125f, "non-target copy result/parameters unchanged");
        amn eventSwap = animations[1].a(animated.a(), animations[1].e(), animations[1].f(), animations[1].g());
        eq(VsnLayout.status(eventSwap), "UNBOUND_ANIMATION", "another event cannot inherit by requesting target text");
        check(VsnLayout.inherit(null, unboundCopy) == unboundCopy && VsnLayout.inherit(unbound, null) == null, "missing provenance stays a no-op");
        int count = draws.size();
        check(!VsnLayout.draw(state, sn, "Fox", false, animated, 84, mask, 16, 54), "Fox dingbats unchanged");
        check(!VsnLayout.draw(state, sn, "HardFox", true, animated, 84, mask, 16, 54), "HardFox unchanged");
        check(draws.size() == count, "no swallowed dingbats draw");
        anh otherState = new anh(null, 100.0, null, null, null, null, true, null, null, null, null);
        check(!VsnLayout.draw(otherState, sn, "", false, animated, 84, mask, 16, 54), "equal state is not identity");
        amn equalAnimated = new amn(animated.a(), 0, (azK)(Object)azI.MODULE$, .06f);
        expectFailure(() -> VsnLayout.draw(state, sn, "", false, equalAnimated, 84, mask, 16, 54), "equal text not identity: unbound/copy instance fails closed under activated target");
        VsnLayout.capture(commands[1], TEXTS[0], equalAnimated);
        expectFailure(() -> VsnLayout.draw(state, sn, "", false, equalAnimated, 84, mask, 16, 54), "wrong event identity");
        amn wrongEventCopy = equalAnimated.a(equalAnimated.a(), equalAnimated.e(), equalAnimated.f(), equalAnimated.g());
        expectFailure(() -> VsnLayout.draw(state, sn, "", false, wrongEventCopy, 84, mask, 16, 54), "copy preserves wrong event rejection rather than rebind by same text");
        check(VsnLayout.inherit(active, equalAnimated) == equalAnimated, "existing child binding is never overwritten");
        expectFailure(() -> VsnLayout.draw(state, sn, "", false, equalAnimated, 84, mask, 16, 54), "different-event child provenance remains unchanged");
        expectFailure(() -> VsnLayout.draw(state, sn, "", false, active, 1, mask, 16, 54), "wrong mask");
        VsnLayout.enablePrototype(source, new PixelLayout.Profile(new PixelLayout.Rect(0, 0, 10, 10), 16, PixelLayout.Insets.NONE), "overflow fixture");
        expectFailure(() -> VsnLayout.draw(state, sn, "", false, active, 84, mask, 16, 54), "auto subtitle overflow fails closed");
        VsnLayout.disablePrototype(source);
        // The actual patched callback executes draw -> original event -> original hint.
        List<String> events = new ArrayList<String>();
        ZJ eventBus = (ZJ)Proxy.newProxyInstance(VsnLayoutTest.class.getClassLoader(), new Class<?>[]{ZJ.class}, (proxy, method, arguments) -> { events.add("event"); order.add("event"); return null; });
        anh late = new anh(null, 200.025, null, null, null, null, true, null, null, null, null);
        VsnLayout.observe(late, source);
        jo renderer = new jo(late, 28, false, sn, 16, 54, Ol.MODULE$, eventBus);
        Method callback = jo.class.getDeclaredMethod("a", jo.class, String.class, azK.class, amn.class, int.class, String.class, boolean.class);
        callback.invoke(null, renderer, "", azI.MODULE$, animated, 84, mask, false);
        eq(events.size(), 1, "original event executes once in diagnostic fallback");
        VsnLayout.enablePrototype(source, p, "tail order fixture");
        order.clear();
        callback.invoke(null, renderer, "", azI.MODULE$, animated, 84, mask, false);
        eq(events.size(), 2, "original event executes once when handled");
        check(order.contains("hint") && order.indexOf("text") < order.indexOf("event") && order.indexOf("event") < order.indexOf("hint"), "text -> original event -> original hint order");
        callback.invoke(null, renderer, "", azI.MODULE$, animated, 84, mask, true);
        eq(events.size(), 2, "done suppresses original event exactly as baseline");
        VsnLayout.disablePrototype(source);
    }
    static arp font() throws Exception {
        arp.a data = new arp.a();
        data.o = data.p = 1; data.q = false;
        for (String text : TEXTS) for (int i = 0; i < text.length(); i++) {
            char cp = text.charAt(i);
            arp.b glyph = new arp.b(); glyph.a = cp; glyph.d = cp == 32 ? 0 : cp < 128 ? 8 : 10;
            glyph.e = cp == 32 ? 0 : 10; glyph.l = cp < 128 ? 8 : 10;
            data.a(cp, glyph);
        }
        if (fontPath != null) {
            Constructor<aqX> file = aqX.class.getDeclaredConstructor(String.class, apO.a.class);
            file.setAccessible(true);
            data = new arp.a(file.newInstance(fontPath, null), false);
            System.out.println("VSN actual arp font data parsed: " + fontPath + ", lineHeight=" + data.i);
        }
        // Allocate without invoking texture constructors/native initialization.
        Field f = sun.misc.Unsafe.class.getDeclaredField("theUnsafe"); f.setAccessible(true);
        sun.misc.Unsafe unsafe = (sun.misc.Unsafe)f.get(null);
        arp font = (arp)unsafe.allocateInstance(arp.class);
        Field a = arp.class.getDeclaredField("a");
        unsafe.putObject(font, unsafe.objectFieldOffset(a), data);
        return font;
    }
    static Map<String, ClassNode> nodes(String jar) throws IOException {
        Map<String, ClassNode> nodes = new LinkedHashMap<>();
        try (ZipFile z = new ZipFile(jar)) {
            for (String name : VsnPatch.INPUT_SHA256.keySet()) {
                ClassNode n = new ClassNode(); new ClassReader(z.getInputStream(z.getEntry(name + ".class"))).accept(n, 0); nodes.put(name, n);
            }
        }
        return nodes;
    }
    static void transform(String jar, Path output) throws Exception {
        Map<String, ClassNode> nodes = nodes(jar);
        MethodNode callback = VsnPatch.method(nodes.get("PRG/jo"), "a", VsnPatch.CALLBACK);
        List<AbstractInsnNode> tail = new ArrayList<>(); boolean after = false;
        for (AbstractInsnNode n : callback.instructions) {
            if (after && n.getOpcode() >= 0) tail.add(n);
            if (n instanceof MethodInsnNode && ((MethodInsnNode)n).owner.equals("PRG/aEO") && ((MethodInsnNode)n).name.equals("f")) after = true;
        }
        Map<String, ClassNode> bad = nodes(jar);
        VsnPatch.method(bad.get("PRG/jl"), "a", VsnPatch.COMPOSE).instructions.insert(new InsnNode(Opcodes.NOP));
        String before = VsnPatch.fingerprint(VsnPatch.method(bad.get("PRG/jo"), "a", VsnPatch.CALLBACK));
        expectFailure(() -> VsnPatch.apply(bad), "mutation rejected atomically");
        eq(before, VsnPatch.fingerprint(VsnPatch.method(bad.get("PRG/jo"), "a", VsnPatch.CALLBACK)), "no partial mutation");
        Map<String, ClassNode> badCopy = nodes(jar);
        VsnPatch.method(badCopy.get("PRG/amn"), "a", VsnPatch.COPY).instructions.insert(new InsnNode(Opcodes.NOP));
        expectFailure(() -> VsnPatch.apply(badCopy), "copier mismatch rejected before mutating any target");
        eq(before, VsnPatch.fingerprint(VsnPatch.method(badCopy.get("PRG/jo"), "a", VsnPatch.CALLBACK)), "copier failure leaves jo unchanged");
        MethodNode copier = VsnPatch.method(nodes.get("PRG/amn"), "a", VsnPatch.COPY);
        List<AbstractInsnNode> originalCopy = new ArrayList<>();
        for (AbstractInsnNode n : copier.instructions) if (n.getOpcode() >= 0) originalCopy.add(n);
        VsnPatch.apply(nodes);
        int previous = -1;
        for (AbstractInsnNode original : originalCopy) {
            int index = copier.instructions.indexOf(original);
            check(index > previous, "all original copy construction/return nodes retain their order"); previous = index;
        }
        List<AbstractInsnNode> patchedCopy = new ArrayList<>();
        for (AbstractInsnNode n : copier.instructions) if (n.getOpcode() >= 0) patchedCopy.add(n);
        check(patchedCopy.size() == originalCopy.size() + 3 && patchedCopy.get(7).getOpcode() == Opcodes.ALOAD
            && ((VarInsnNode)patchedCopy.get(7)).var == 0 && patchedCopy.get(8).getOpcode() == Opcodes.SWAP,
            "copy hook uses exact receiver and existing stack child with no parameter/local rewrite");
        MethodInsnNode inheritance = (MethodInsnNode)patchedCopy.get(9);
        eq(inheritance.owner + "." + inheritance.name + inheritance.desc,
            "PRG/VsnLayout.inherit(LPRG/amn;LPRG/amn;)LPRG/amn;", "exact inheritance bridge before original ARETURN");
        for (AbstractInsnNode original : tail) check(callback.instructions.indexOf(original) >= 0, "same tail nodes retained");
        int at = -1;
        for (AbstractInsnNode original : tail) {
            int index = callback.instructions.indexOf(original); check(index > at, "tail order"); at = index;
        }
        for (AbstractInsnNode n : callback.instructions) if (n instanceof MethodInsnNode)
            check(!((MethodInsnNode)n).owner.equals("PRG/amr$e"), "no old secondary chunking in callback");
        expectFailure(() -> VsnPatch.apply(nodes), "second application rejected");
        for (Map.Entry<String, ClassNode> entry : nodes.entrySet()) {
            ClassWriter writer = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS) {
                protected String getCommonSuperClass(String a, String b) {
                    if (assignable(a, b, jar)) return a;
                    if (assignable(b, a, jar)) return b;
                    ClassNode x = hierarchy(a, jar), y = hierarchy(b, jar);
                    if ((x.access & Opcodes.ACC_INTERFACE) != 0 || (y.access & Opcodes.ACC_INTERFACE) != 0) return "java/lang/Object";
                    do { a = hierarchy(a, jar).superName; } while (a != null && !assignable(a, b, jar));
                    return a == null ? "java/lang/Object" : a;
                }
            };
            entry.getValue().accept(writer);
            Path target = output.resolve(entry.getKey() + ".class"); Files.createDirectories(target.getParent()); Files.write(target, writer.toByteArray());
        }
        // Windows directory lookup is case-insensitive (amn versus amN).
        // Execute from exact ZIP entries, never loose transformed game classes.
        try (ZipOutputStream archive = new ZipOutputStream(Files.newOutputStream(output.resolve("vsn-patched.jar")))) {
            for (String name : nodes.keySet()) {
                archive.putNextEntry(new ZipEntry(name + ".class"));
                archive.write(Files.readAllBytes(output.resolve(name + ".class")));
                archive.closeEntry();
            }
        }
        System.out.println("VSN ASM PASS: exact boundaries; same tail nodes/order; atomic rejection; 4 transformed classes written; receiver-based copier hook verified; exact-entry test JAR created");
    }
    static amH[] parserTrace(String path) throws Exception {
        Field field = sun.misc.Unsafe.class.getDeclaredField("theUnsafe"); field.setAccessible(true);
        sun.misc.Unsafe unsafe = (sun.misc.Unsafe)field.get(null);
        amS.a parser = (amS.a)unsafe.allocateInstance(amS.a.class);
        Field source = amS.a.class.getDeclaredField("a");
        unsafe.putObject(parser, unsafe.objectFieldOffset(source), "ClassicPreTitle");
        String script = new String(Files.readAllBytes(Paths.get(path)), java.nio.charset.StandardCharsets.UTF_8);
        auK input = auL.MODULE$.a(script, (azz<String, auI>)(s -> new auC(s)));
        auG result = ava.MODULE$.a(input, (azz<auN<Object>,auN<aEO<amZ>>>)(s -> parser.E(s)), ava.MODULE$.a(), ava.MODULE$.b(), ava.MODULE$.c());
        aEO<amZ> parsed = (aEO<amZ>)result.a().e();
        List<amH> commands = new ArrayList<>();
        for (int i = 0; i < parsed.length(); i++) {
            if (!(parsed.m(i) instanceof amH)) continue;
            amH command = (amH)parsed.m(i);
            commands.add(command);
            String value = ams.MODULE$.a(command.a(), amr.i.MODULE$.a());
            System.out.println("PARSED len=" + value.length() + " text=[" + value.replace(" ", "_") + "] key=" + command.a().e());
            System.out.println("ANIM=[" + ((amr.d)amw.MODULE$.a(value, Ol.MODULE$, Om.MODULE$).s()).a().replace(" ", "_") + "]");
        }
        eq(commands.size(), 8, "frozen script auto count");
        return commands.toArray(new amH[0]);
    }
    static void englishNonTarget(amH[] commands) {
        aEO<amW> list = (aEO<amW>)(aEO<?>)aFC.MODULE$;
        for (int i = 7; i >= 0; i--) list = list.b((amW)commands[i]);
        amU source = new amU("ClassicPreTitle", null, null, null, list);
        anh state = new anh(null, 100.0, null, null, null, null, true, null, null, null, null);
        VsnLayout.observe(state, source);
        VsnLayout.enablePrototype(source, new PixelLayout.Profile(new PixelLayout.Rect(0, 0, 224, 48), 16, PixelLayout.Insets.NONE), "English non-target fixture");
        for (amH command : commands) {
            amn animation = ((amG)command.a(state, new amX(null, Ol.MODULE$, Om.MODULE$, null)).f().f()).a();
            check(!VsnLayout.draw(state, null, command.f(), false, animation, 0, amw.MODULE$.a(animation.a(), 0), 16, 54), "r21 SFW English preserves original path under prototype");
            eq(VsnLayout.status(animation), "KNOWN_R21_SFW_ENGLISH_NON_TARGET", "explicit English variant status");
            amn copy = animation.a(animation.a(), animation.e(), animation.f(), animation.g());
            check(!VsnLayout.draw(state, null, command.f(), false, copy, 0, amw.MODULE$.a(copy.a(), 0), 16, 54), "English copied instance remains non-target");
            eq(VsnLayout.status(copy), "KNOWN_R21_SFW_ENGLISH_NON_TARGET", "English provenance copy does not activate layout");
        }
        VsnLayout.disablePrototype(source);
    }
    static final Map<String, ClassNode> HIERARCHY = new HashMap<>();
    static ClassNode hierarchy(String name, String jar) {
        ClassNode found = HIERARCHY.get(name);
        if (found != null) return found;
        try (ZipFile z = new ZipFile(jar)) {
            ClassNode n = new ClassNode();
            ZipEntry entry = z.getEntry(name + ".class");
            InputStream input = entry == null ? ClassLoader.getSystemResourceAsStream(name + ".class") : z.getInputStream(entry);
            if (input == null) throw new IllegalStateException("missing hierarchy " + name);
            try (InputStream close = input) { new ClassReader(close).accept(n, ClassReader.SKIP_CODE | ClassReader.SKIP_DEBUG | ClassReader.SKIP_FRAMES); }
            HIERARCHY.put(name, n); return n;
        } catch (IOException failure) { throw new IllegalStateException(failure); }
    }
    static boolean assignable(String target, String type, String jar) {
        if (target.equals(type) || target.equals("java/lang/Object")) return true;
        ClassNode n = hierarchy(type, jar);
        if (n.superName != null && assignable(target, n.superName, jar)) return true;
        for (String itf : n.interfaces) if (assignable(target, itf, jar)) return true;
        return false;
    }
    static void expectFailure(Runnable run, String message) {
        try { run.run(); } catch (IllegalStateException expected) { return; }
        throw new AssertionError(message);
    }
    static void check(boolean value, String message) { if (!value) throw new AssertionError(message); }
    static void eq(Object a, Object b, String message) { if (!Objects.equals(a, b)) throw new AssertionError(message + ": " + a + " != " + b); }

}
