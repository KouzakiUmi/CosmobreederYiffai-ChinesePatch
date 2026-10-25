import cosmoloc.layout.PixelLayout;
import java.io.InputStream;
import java.lang.reflect.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.zip.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Isolated fixture tests: no game main, installation, save or archive writes.
 * args: original.jar helper-output-directory. All generated files are optional;
 * this test itself performs no writes. PRG runtime fixtures do NOT prove G3.
 */
public final class ItemMenuLayoutTest implements Opcodes {
    private static int assertions;
    private static double glyphAdvance = 10;
    public static PixelLayout.Metrics metrics() {
        return new PixelLayout.Metrics() {
            public PixelLayout.Glyph glyph(int cp) {
                return new PixelLayout.Glyph(glyphAdvance, 0, -10, 10, 10);
            }
            public double kerning(int a, int b) { return 0; }
        };
    }
    private static void check(boolean value, String message) {
        assertions++; if (!value) throw new AssertionError(message);
    }
    private static PixelLayout.Profile profile(String id, int width, int height) {
        return new PixelLayout.Profile(id, "test-1", new PixelLayout.Rect(0, 0, width, height),
                14, PixelLayout.Insets.NONE);
    }
    private static void pure() {
        String full = "完整名称中文测试装备+";
        PixelLayout.Plan p = PRG.ItemMenuLayout.plan(full, metrics(), profile("name", 40, 56));
        check(!p.overflow && p.lines.size() == 3, "complete equipped name wraps without loss");
        int end = 0;
        for (PixelLayout.Line l : p.lines) {
            check(l.display.start == end, "contiguous full text");
            end = l.display.end;
            check(l.layoutBounds.width() <= 40, "actual pixel width");
            check(l.visiblePrefix(full.length()).displayEnd == l.display.end, "full reveal");
        }
        check(end == full.length() && full.endsWith("+"), "full name and suffix retained");
        PixelLayout.Plan exact = PRG.ItemMenuLayout.plan("甲乙丙丁", metrics(), profile("exact", 40, 14));
        check(!exact.overflow && exact.lines.size() == 1, "exact width/height");
        check(PRG.ItemMenuLayout.plan("甲乙丙丁戊", metrics(), profile("over", 40, 14)).overflow,
                "height overflow explicitly retained");
        check(PRG.ItemMenuLayout.plan("甲", metrics(), profile("unit", 9, 14)).overflow, "oversized unit");
        PixelLayout.Plan two = PRG.ItemMenuLayout.plan("一二三四五六七八九十", metrics(), profile("tall", 20, 28));
        check(two.overflow && two.lines.size() == 5 && two.text.length() == 10, "no zip-to-two-line loss");
        PixelLayout.Plan mixed = PRG.ItemMenuLayout.plan("A（中文）……B\nC", metrics(), profile("mixed", 80, 70));
        check(mixed.text.equals("A（中文）……B\nC"), "mixed final text not rewritten");
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 2) throw new IllegalArgumentException("original.jar helper-output-directory");
        pure(); patch(args[0]); runtimeFixture(Paths.get(args[1]));
        System.out.println("ITEM_MENU_TEST_OK assertions=" + assertions + " (G1 + isolated G2 fixture; G3 unverified)");
    }

    private static Map<String,ClassNode> load(String jar) throws Exception {
        String[] names = {"Le", "Lg", "Lb"};
        String[] hashes = {
            "6e0a0f8d826cb42810354ac753fb609d766d3e487a423692f51c2809b103e86d",
            "426f0c4be7947b096e421fb62a387e5b43a9e5b8f084475dd7464cf9f50e1240",
            "c753a5df061b665c502f265fd3d340f33f52803c193daa787f294aa43cba4ae1"};
        Map<String,ClassNode> out = new TreeMap<>();
        try (ZipFile zip = new ZipFile(jar)) {
            for (int i = 0; i < names.length; i++) {
                String name = "PRG/" + names[i];
                byte[] bytes;
                try (InputStream input = zip.getInputStream(zip.getEntry(name + ".class"))) { bytes = input.readAllBytes(); }
                StringBuilder actual = new StringBuilder();
                for (byte b : MessageDigest.getInstance("SHA-256").digest(bytes)) actual.append(String.format("%02x", b & 255));
                check(hashes[i].equals(actual.toString()), "pinned actual class " + name);
                ClassNode node = new ClassNode(ASM8);
                new ClassReader(bytes).accept(node, ClassReader.EXPAND_FRAMES);
                out.put(name, node);
            }
        }
        return out;
    }
    private static MethodNode method(ClassNode c, String name, String desc) {
        for (MethodNode m : c.methods) if (m.name.equals(name) && m.desc.equals(desc)) return m;
        throw new AssertionError("method " + c.name + name + desc);
    }
    private static byte[] methodBytes(MethodNode m) {
        ClassWriter w = new ClassWriter(0);
        w.visit(V1_8, ACC_PUBLIC, "Probe", null, "java/lang/Object", null);
        m.accept(w); w.visitEnd(); return w.toByteArray();
    }
    private static int calls(MethodNode m, String owner, String name) {
        int count = 0;
        for (AbstractInsnNode n : m.instructions.toArray())
            if (n instanceof MethodInsnNode && ((MethodInsnNode)n).owner.equals(owner)
                    && ((MethodInsnNode)n).name.equals(name)) count++;
        return count;
    }
    private static void patch(String jar) throws Exception {
        Map<String,ClassNode> actual = load(jar);
        Map<String,byte[]> untouched = new TreeMap<>();
        for (ClassNode c : actual.values()) for (MethodNode m : c.methods) {
            boolean target = (m.name.equals("b") && m.desc.equals("(LPRG/SN;)V"))
                    || (c.name.equals("PRG/Le") && (m.name.equals("<init>")
                    || (m.name.equals("b") && m.desc.equals("(LPRG/Le;)Ljava/lang/String;"))));
            if (!target) untouched.put(c.name + m.name + m.desc, methodBytes(m));
        }
        ItemMenuPatch.apply(actual);
        for (ClassNode c : actual.values()) for (MethodNode m : c.methods) {
            byte[] original = untouched.get(c.name + m.name + m.desc);
            if (original != null) check(Arrays.equals(original, methodBytes(m)), "unrelated method unchanged " + c.name + m.name + m.desc);
        }
        ClassNode le = actual.get("PRG/Le"), lg = actual.get("PRG/Lg"), lb = actual.get("PRG/Lb");
        MethodNode ctor = method(le, "<init>", "(LPRG/apr;)V");
        check(calls(ctor, "PRG/ItemMenuLayout", "registerName") == 1, "one selected name identity");
        check(calls(ctor, "PRG/ItemMenuLayout", "registerDescription") == 1, "one description identity");
        MethodNode name = method(le, "b", "(LPRG/Le;)Ljava/lang/String;");
        check(calls(name, "PRG/ItemMenuLayout", "prototypeEnabled") == 1, "local-only prototype gate");
        check(calls(name, "PRG/ItemMenuLayout", "observeFullName") == 1, "observe complete local2");
        check(calls(method(lg, "b", "(LPRG/SN;)V"), "PRG/ItemMenuLayout", "drawName") == 1, "Lg final full-line bridge");
        MethodNode desc = method(lb, "b", "(LPRG/SN;)V");
        check(calls(desc, "PRG/azy", "apply") == 1 && calls(desc, "PRG/amr$d", "a") == 1, "final description evaluated once");
        for (AbstractInsnNode n : desc.instructions.toArray())
            if (n instanceof MethodInsnNode && ((MethodInsnNode)n).name.equals("drawDescription")) {
                AbstractInsnNode branch = n.getNext();
                check(branch instanceof JumpInsnNode && branch.getOpcode() == IFEQ, "explicit diagnostic fallback");
                check(branch.getNext().getOpcode() == RETURN, "prototype exits before BOTH old splitting stages");
            }
        // Emit real frames against the pinned original hierarchy. Parse and verify-load only,
        // without invoking game constructors or initializing the game.
        Map<String,byte[]> emitted = new HashMap<>();
        for (ClassNode c : actual.values()) {
            ClassWriter w = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS);
            c.accept(w); byte[] bytes = w.toByteArray(); new ClassReader(bytes);
            emitted.put(c.name.replace('/', '.'), bytes);
            check((bytes[6] & 255) == 0 && (bytes[7] & 255) == 52, "runtime targets remain Java8");
        }
        ClassLoader verify = byteLoader(emitted);
        for (String type : emitted.keySet()) check(verify.loadClass(type).getDeclaredMethods().length > 0, "verify emitted " + type);
        boolean rejected = false;
        try { ItemMenuPatch.apply(actual); } catch (IllegalStateException expected) { rejected = true; }
        check(rejected, "already patched input rejected");
        Map<String,ClassNode> mismatch = load(jar);
        MethodNode wrong = method(mismatch.get("PRG/Lb"), "b", "(LPRG/SN;)V");
        for (AbstractInsnNode n : wrong.instructions.toArray())
            if (n instanceof MethodInsnNode && ((MethodInsnNode)n).owner.equals("PRG/amw")) ((MethodInsnNode)n).name = "wrong";
        rejected = false;
        try { ItemMenuPatch.apply(mismatch); } catch (IllegalStateException expected) { rejected = true; }
        check(rejected, "structural mismatch rejected");
        check(calls(method(mismatch.get("PRG/Le"), "<init>", "(LPRG/apr;)V"), "PRG/ItemMenuLayout", "registerName") == 0,
                "failure before any partial class mutation");
    }

    private static ClassLoader byteLoader(final Map<String,byte[]> classes) {
        return new ClassLoader(ItemMenuLayoutTest.class.getClassLoader()) {
            @Override protected synchronized Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                if (!classes.containsKey(name)) return super.loadClass(name, resolve);
                Class<?> value = findLoadedClass(name);
                if (value == null) { byte[] b = classes.get(name); value = defineClass(name, b, 0, b.length); }
                if (resolve) resolveClass(value); return value;
            }
        };
    }
    private static ClassWriter basic(String name, int access) {
        ClassWriter w = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS);
        w.visit(V1_8, access, name, null, "java/lang/Object", null);
        if ((access & ACC_INTERFACE) == 0) {
            MethodVisitor m = w.visitMethod(ACC_PUBLIC, "<init>", "()V", null, null);
            m.visitCode(); m.visitVarInsn(ALOAD, 0); m.visitMethodInsn(INVOKESPECIAL, "java/lang/Object", "<init>", "()V", false);
            m.visitInsn(RETURN); m.visitMaxs(0, 0); m.visitEnd();
        }
        return w;
    }
    private static void fixture(Map<String,byte[]> all, String name) {
        ClassWriter w = basic(name, ACC_PUBLIC);
        if (name.equals("PRG/Lb")) for (String method : new String[] {"e_", "f_"}) {
            MethodVisitor m = w.visitMethod(ACC_PUBLIC, method, "()I", null, null); m.visitCode();
            m.visitIntInsn(SIPUSH, method.equals("e_") ? 136 : 22); m.visitInsn(IRETURN); m.visitMaxs(0, 0); m.visitEnd();
        }
        w.visitEnd(); all.put(name.replace('/', '.'), w.toByteArray());
    }
    private static void runtimeFixture(Path helperDir) throws Exception {
        Map<String,byte[]> all = new HashMap<>();
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(helperDir.resolve("PRG"), "ItemMenuLayout*.class")) {
            for (Path p : stream) all.put("PRG." + p.getFileName().toString().replace(".class", ""), Files.readAllBytes(p));
        }
        for (String n : new String[] {"PRG/Le", "PRG/Lg", "PRG/Lb", "PRG/arp"}) fixture(all, n);
        ClassWriter sn = basic("PRG/SN", ACC_PUBLIC | ACC_INTERFACE | ACC_ABSTRACT);
        sn.visitMethod(ACC_PUBLIC | ACC_ABSTRACT, "a", "(Ljava/lang/String;IILjava/lang/String;)V", null, null).visitEnd();
        sn.visitMethod(ACC_PUBLIC | ACC_ABSTRACT, "b", "()Ljava/lang/String;", null, null).visitEnd();
        sn.visitEnd(); all.put("PRG.SN", sn.toByteArray());
        ClassWriter bridge = basic("PRG/LayoutBridge", ACC_PUBLIC);
        bridge.visitField(ACC_PUBLIC | ACC_STATIC, "FONT", "LPRG/arp;", null, null).visitEnd();
        MethodVisitor m = bridge.visitMethod(ACC_STATIC, "<clinit>", "()V", null, null); m.visitCode();
        m.visitTypeInsn(NEW, "PRG/arp"); m.visitInsn(DUP); m.visitMethodInsn(INVOKESPECIAL, "PRG/arp", "<init>", "()V", false);
        m.visitFieldInsn(PUTSTATIC, "PRG/LayoutBridge", "FONT", "LPRG/arp;"); m.visitInsn(RETURN); m.visitMaxs(0, 0); m.visitEnd();
        m = bridge.visitMethod(ACC_PUBLIC | ACC_STATIC, "font", "(LPRG/SN;Ljava/lang/String;)LPRG/arp;", null, null); m.visitCode();
        m.visitFieldInsn(GETSTATIC, "PRG/LayoutBridge", "FONT", "LPRG/arp;"); m.visitInsn(ARETURN); m.visitMaxs(0, 0); m.visitEnd();
        m = bridge.visitMethod(ACC_PUBLIC | ACC_STATIC, "metrics", "(LPRG/arp;)Lcosmoloc/layout/PixelLayout$Metrics;", null, null); m.visitCode();
        m.visitMethodInsn(INVOKESTATIC, "ItemMenuLayoutTest", "metrics", "()Lcosmoloc/layout/PixelLayout$Metrics;", false);
        m.visitInsn(ARETURN); m.visitMaxs(0, 0); m.visitEnd();
        m = bridge.visitMethod(ACC_PUBLIC | ACC_STATIC, "draw", "(LPRG/SN;Ljava/lang/String;IILjava/lang/String;)V", null, null); m.visitCode();
        for (int i = 0; i < 5; i++) m.visitVarInsn(i == 2 || i == 3 ? ILOAD : ALOAD, i);
        m.visitMethodInsn(INVOKEINTERFACE, "PRG/SN", "a", "(Ljava/lang/String;IILjava/lang/String;)V", true);
        m.visitInsn(RETURN); m.visitMaxs(0, 0); m.visitEnd(); bridge.visitEnd();
        all.put("PRG.LayoutBridge", bridge.toByteArray());
        ClassLoader loader = byteLoader(all);
        Class<?> api = loader.loadClass("PRG.ItemMenuLayout"), le = loader.loadClass("PRG.Le"), lg = loader.loadClass("PRG.Lg"),
                lb = loader.loadClass("PRG.Lb"), renderer = loader.loadClass("PRG.SN");
        Object owner = le.getConstructor().newInstance(), name = lg.getConstructor().newInstance(),
                category = lg.getConstructor().newInstance(), description = lb.getConstructor().newInstance();
        List<Object[]> draws = new ArrayList<>();
        Object proxy = java.lang.reflect.Proxy.newProxyInstance(loader, new Class<?>[] {renderer}, (p, method, args) -> {
            if (method.getName().equals("b")) return "default";
            if (method.getName().equals("a")) draws.add(args);
            return null;
        });
        api.getMethod("disablePrototype").invoke(null);
        api.getMethod("registerName", le, lg).invoke(null, owner, name);
        api.getMethod("registerDescription", le, lb).invoke(null, owner, description);
        Method drawName = api.getMethod("drawName", renderer, String.class, int.class, int.class, String.class, lg);
        Method drawDescription = api.getMethod("drawDescription", lb, renderer, String.class);
        check(api.getMethod("mode").invoke(null).equals("diagnostic-not-adapted"), "safe unknown-rectangle default");
        drawName.invoke(null, proxy, "未改原绘制", 176, -16, "default", name);
        check(draws.size() == 1 && draws.get(0)[2].equals(-16), "default original negative anchor preserved");
        Object diagnostic = api.getMethod("lastName").invoke(null);
        check(diagnostic.getClass().getField("blockedReason").get(diagnostic).equals("unknown-contentRect-and-parent-clip"), "unknown clip explicit");
        check(!(Boolean) drawDescription.invoke(null, description, proxy, "这是一段十四码元以上的完整动态道具说明文本"), "diagnostic keeps original consume chain");
        api.getMethod("configurePrototype", PixelLayout.Profile.class, PixelLayout.Profile.class)
                .invoke(null, profile("name", 40, 56), profile("description", 40, 112));
        draws.clear(); drawName.invoke(null, proxy, "完整名称中文+", 176, -16, "default", name);
        check(draws.size() == 2 && draws.get(0)[2].equals(-26) && draws.get(1)[2].equals(-40), "topdown -> original SN y conversion");
        StringBuilder rendered = new StringBuilder(); for (Object[] d : draws) rendered.append(d[0]);
        check(rendered.toString().equals("完整名称中文+"), "full name including suffix drawn once");
        Object cached = api.getMethod("lastName").invoke(null).getClass().getField("plan").get(api.getMethod("lastName").invoke(null));
        drawName.invoke(null, proxy, "完整名称中文+", 176, -16, "default", name);
        Object cachedAgain = api.getMethod("lastName").invoke(null).getClass().getField("plan").get(api.getMethod("lastName").invoke(null));
        check(cached == cachedAgain, "stable text/metrics/profile reuses plan");
        glyphAdvance = 11;
        drawName.invoke(null, proxy, "完整名称中文+", 176, -16, "default", name);
        Object revised = api.getMethod("lastName").invoke(null).getClass().getField("plan").get(api.getMethod("lastName").invoke(null));
        check(revised != cached, "mutable metric revision invalidates plan"); glyphAdvance = 10;
        draws.clear(); drawName.invoke(null, proxy, "类别标签不换行", 136, 174, "default", category);
        check(draws.size() == 1 && draws.get(0)[0].equals("类别标签不换行"), "unregistered Lg exact passthrough");
        draws.clear(); drawName.invoke(null, proxy, "", 176, -16, "default", name);
        check(draws.isEmpty(), "original blink empty string remains invisible");
        String dynamic1 = "这是一段超过十四码元并且必须全部显示的说明文字";
        check((Boolean) drawDescription.invoke(null, description, proxy, dynamic1), "prototype consumes final full description");
        diagnostic = api.getMethod("lastDescription").invoke(null);
        check(diagnostic.getClass().getField("finalText").get(diagnostic).equals(dynamic1), "description before amw retained");
        String dynamic2 = "每三秒变化的另一种完整说明";
        draws.clear(); drawDescription.invoke(null, description, proxy, dynamic2);
        diagnostic = api.getMethod("lastDescription").invoke(null);
        check(diagnostic.getClass().getField("finalText").get(diagnostic).equals(dynamic2), "dynamic final supplier never frozen");
        api.getMethod("configurePrototype", PixelLayout.Profile.class, PixelLayout.Profile.class)
                .invoke(null, profile("small-name", 40, 14), profile("small-description", 40, 14));
        draws.clear(); boolean blocked = false;
        try { drawDescription.invoke(null, description, proxy, dynamic1); }
        catch (InvocationTargetException expected) { blocked = expected.getCause() instanceof IllegalStateException; }
        check(blocked && draws.isEmpty(), "overflow blocks before drawing any partial text");
        diagnostic = api.getMethod("lastDescription").invoke(null);
        check(diagnostic.getClass().getField("plan").get(diagnostic) != null, "overflow plan available for diagnosis");
        check(!(Boolean) diagnostic.getClass().getField("parentClipVerified").get(diagnostic), "never claim verified parent clip");
        api.getMethod("configurePrototype", PixelLayout.Profile.class, PixelLayout.Profile.class)
                .invoke(null, new PixelLayout.Profile("fractional", "1", new PixelLayout.Rect(0.5, 0, 40, 28),
                        14, PixelLayout.Insets.NONE), profile("description", 40, 112));
        draws.clear(); blocked = false;
        try { drawName.invoke(null, proxy, "完整名称", 176, -16, "default", name); }
        catch (InvocationTargetException expected) { blocked = expected.getCause() instanceof IllegalStateException; }
        check(blocked && draws.isEmpty(), "fractional SN backend mismatch blocks instead of rounding");
        api.getMethod("configurePrototype", PixelLayout.Profile.class, PixelLayout.Profile.class)
                .invoke(null, profile("capacity-name", 40, 56), profile("capacity-description", 40, 112));
        List<Object> liveWidgets = new ArrayList<>();
        int limit = api.getField("MAX_ENTRIES").getInt(null);
        for (int i = 2; i < limit; i++) {
            Object live = lg.getConstructor().newInstance(); liveWidgets.add(live);
            api.getMethod("registerName", le, lg).invoke(null, owner, live);
        }
        blocked = false;
        try { api.getMethod("registerName", le, lg).invoke(null, owner, lg.getConstructor().newInstance()); }
        catch (InvocationTargetException expected) { blocked = expected.getCause() instanceof IllegalStateException
                && expected.getCause().getMessage().contains("registration-capacity"); }
        check(blocked && liveWidgets.size() == limit - 2, "bounded registry blocks rather than evicting live identities");
        draws.clear(); drawName.invoke(null, proxy, "完整名称中文+", 176, -16, "default", name);
        check(draws.size() == 2, "oldest live selected name remains registered after capacity failure");
        String property = "cosmo.layout.item.prototype";
        Map<String,String> savedProperties = new HashMap<>();
        savedProperties.put(property, System.getProperty(property));
        for (String field : new String[] {"name", "description"})
            for (String part : new String[] {"x", "y", "width", "height", "step"}) {
                String key = "cosmo.layout.item." + field + "." + part;
                savedProperties.put(key, System.getProperty(key)); System.clearProperty(key);
            }
        try {
            System.setProperty(property, "true"); blocked = false;
            try { api.getMethod("configureFromProperties").invoke(null); }
            catch (InvocationTargetException expected) { blocked = expected.getCause() instanceof IllegalStateException; }
            check(blocked, "launch opt-in requires explicit rectangles");
            for (String field : new String[] {"name", "description"}) {
                String prefix = "cosmo.layout.item." + field + ".";
                System.setProperty(prefix + "x", "0"); System.setProperty(prefix + "y", "0");
                System.setProperty(prefix + "width", "40"); System.setProperty(prefix + "height", "112");
                System.setProperty(prefix + "step", "14");
            }
            // New helper class loader = first registration, not an explicit configure call.
            ClassLoader startup = byteLoader(all);
            Class<?> startupApi = startup.loadClass("PRG.ItemMenuLayout"), startupLe = startup.loadClass("PRG.Le"),
                    startupLg = startup.loadClass("PRG.Lg");
            startupApi.getMethod("registerName", startupLe, startupLg).invoke(null,
                    startupLe.getConstructor().newInstance(), startupLg.getConstructor().newInstance());
            check(startupApi.getMethod("mode").invoke(null).equals("prototype-unverified"), "real startup property activation");
            System.setProperty("cosmo.layout.item.name.step", "8"); blocked = false;
            try { api.getMethod("configureFromProperties").invoke(null); }
            catch (InvocationTargetException expected) { blocked = expected.getCause() instanceof IllegalArgumentException; }
            check(blocked, "8px prototype line step rejected");
        } finally {
            for (Map.Entry<String,String> saved : savedProperties.entrySet())
                if (saved.getValue() == null) System.clearProperty(saved.getKey());
                else System.setProperty(saved.getKey(), saved.getValue());
            api.getMethod("disablePrototype").invoke(null);
        }
    }
}
