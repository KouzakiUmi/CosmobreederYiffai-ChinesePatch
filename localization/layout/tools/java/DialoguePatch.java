import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.zip.*;
import jdk.internal.org.objectweb.asm.*;
import jdk.internal.org.objectweb.asm.tree.*;

/** Build-time only. apply validates BOTH targets before any mutation. The driver
 * must SHA-pin original bytes and use archive-aware COMPUTE_FRAMES/MAXS. */
public final class DialoguePatch implements Opcodes {
    private DialoguePatch() { }
    public static final String RADIO = "(LPRG/afD$g;LPRG/amq;LPRG/amv;LPRG/apr;)LPRG/aAJ;";
    public static final String STORY = "(LPRG/afD$g;LPRG/MG;DLPRG/azA;LPRG/apr;)LPRG/Na$a;";
    public static final Map<String, String> INPUT_SHA256;
    static {
        Map<String, String> pins = new LinkedHashMap<String, String>();
        pins.put("PRG/JR", "89bc9f39fc7227f0407afa626b8f816099f7b0f0e9c0a3e43abc719378c680c9");
        pins.put("PRG/Nb", "147d037fe7553457eb1ce10310b74ca6ffa42cfeac1e78d068d0ffbc594bbb92");
        INPUT_SHA256 = Collections.unmodifiableMap(pins);
    }
    private static final String RADIO_CODE = "9dc4fa88f1281a1f427e03a056c789387abcbdb0ee04c6eb9b0d8460dc885ae1";
    private static final String STORY_CODE = "bcd7fa84389434db009e65a92aa105894bfca28a0ebb6dbac9db885730617774";

    public static void apply(Map<String, ClassNode> classes) {
        MethodNode radio = target(classes, "PRG/JR", RADIO, RADIO_CODE);
        MethodNode story = target(classes, "PRG/Nb", STORY, STORY_CODE);
        List<AbstractInsnNode> r = code(radio), s = code(story);
        int radioAt = boundary(r, true), storyAt = boundary(s, false);
        // Preflight is complete. Preserve all other locals, tuples, events and return code.
        InsnList replacement = new InsnList();
        replacement.add(new VarInsnNode(ALOAD, 18));
        replacement.add(new VarInsnNode(ALOAD, 2));
        replacement.add(new VarInsnNode(ALOAD, 3));
        replacement.add(new VarInsnNode(ALOAD, 8));
        replacement.add(new MethodInsnNode(INVOKESTATIC, "PRG/DialogueWrap", "radio",
            "(LPRG/aEO;LPRG/amq;LPRG/amv;LPRG/SA;)LPRG/aEO;", false));
        replacement.add(new VarInsnNode(ASTORE, 21));
        replace(radio, r, radioAt, 11, replacement);
        replacement = new InsnList();
        replacement.add(new VarInsnNode(ALOAD, 18));
        replacement.add(new MethodInsnNode(INVOKESTATIC, "PRG/DialogueWrap", "story", "(LPRG/aEO;)LPRG/aEO;", false));
        replace(story, s, storyAt, 3, replacement); // original ASTORE 20 is retained
    }
    private static MethodNode target(Map<String, ClassNode> map, String name, String desc, String fingerprint) {
        ClassNode c = map.get(name);
        if (c == null || !name.equals(c.name) || c.version != V1_8) fail("missing/version " + name);
        MethodNode m = VsnPatch.method(c, "a", desc);
        if (!m.tryCatchBlocks.isEmpty() || !VsnPatch.fingerprint(m).equals(fingerprint))
            fail("original instruction fingerprint " + name);
        return m;
    }
    private static int boundary(List<AbstractInsnNode> c, boolean radio) {
        int found = -1;
        for (int i = 0; i < c.size(); i++) {
            if (!var(c.get(i), ALOAD, 18)) continue;
            if (radio) {
                if (i + 10 >= c.size() || !var(c.get(i+1), ALOAD, 2) || !var(c.get(i+2), ALOAD, 3)
                    || !dynamic(c.get(i+3), "(LPRG/amq;LPRG/amv;)LPRG/azz;")
                    || !call(c.get(i+4), "w") || !var(c.get(i+5), ASTORE, 20)
                    || !var(c.get(i+6), ALOAD, 20) || !var(c.get(i+7), ALOAD, 8)
                    || !dynamic(c.get(i+8), "(LPRG/SA;)LPRG/azz;") || !call(c.get(i+9), "v")
                    || !var(c.get(i+10), ASTORE, 21)) continue;
            } else if (i + 3 >= c.size() || !dynamic(c.get(i+1), "()LPRG/azz;")
                       || !call(c.get(i+2), "w") || !var(c.get(i+3), ASTORE, 20)) continue;
            if (found != -1) fail("duplicate boundary");
            found = i;
        }
        if (found == -1) fail("missing exact boundary");
        if (radio) {
            // The original return passes local19 directly: preserve that EXACT event-list
            // reference, not a copy/rebuilt collection. The helper never receives events.
            if (c.size() != found + 17 || !var(c.get(found + 13), ALOAD, 21)
                || !var(c.get(found + 14), ALOAD, 19) || c.get(found + 16).getOpcode() != ARETURN)
                fail("original radio event-list identity tail");
        }
        return found;
    }
    private static boolean var(AbstractInsnNode n, int op, int local) {
        return n instanceof VarInsnNode && n.getOpcode() == op && ((VarInsnNode)n).var == local;
    }
    private static boolean dynamic(AbstractInsnNode n, String desc) {
        return n instanceof InvokeDynamicInsnNode && ((InvokeDynamicInsnNode)n).name.equals("apply")
            && ((InvokeDynamicInsnNode)n).desc.equals(desc);
    }
    private static boolean call(AbstractInsnNode n, String name) {
        if (!(n instanceof MethodInsnNode)) return false;
        MethodInsnNode m = (MethodInsnNode)n;
        return m.getOpcode() == INVOKEVIRTUAL && m.owner.equals("PRG/aEO") && m.name.equals(name)
            && m.desc.equals("(LPRG/azz;)LPRG/aEO;") && !m.itf;
    }
    private static List<AbstractInsnNode> code(MethodNode m) {
        List<AbstractInsnNode> out = new ArrayList<AbstractInsnNode>();
        for (AbstractInsnNode n : m.instructions) if (n.getOpcode() >= 0) out.add(n);
        return out;
    }
    private static void replace(MethodNode m, List<AbstractInsnNode> code, int start, int count, InsnList insert) {
        m.instructions.insertBefore(code.get(start), insert);
        for (int i = start; i < start + count; i++) m.instructions.remove(code.get(i));
        for (AbstractInsnNode n : m.instructions.toArray()) if (n instanceof FrameNode) m.instructions.remove(n);
    }
    private static void fail(String why) { throw new IllegalStateException("Dialogue patch refused: " + why); }
    private static String sha(byte[] value) throws Exception {
        StringBuilder out = new StringBuilder();
        for (byte b : MessageDigest.getInstance("SHA-256").digest(value)) out.append(String.format("%02x", b & 255));
        return out.toString();
    }

    /** Standalone isolated driver: input.jar NEW-output.jar helper.jar. Never writes a loose game class. */
    public static void main(String[] args) throws Exception {
        if (args.length != 3) throw new IllegalArgumentException("input.jar NEW-output.jar helper.jar (or --fingerprints input.jar unused)");
        boolean print = args[0].equals("--fingerprints");
        Path input = Paths.get(args[print ? 1 : 0]).toAbsolutePath().normalize();
        Map<String, byte[]> entries = new TreeMap<String, byte[]>();
        try (ZipFile jar = new ZipFile(input.toFile())) {
            Enumeration<? extends ZipEntry> it = jar.entries();
            while (it.hasMoreElements()) {
                ZipEntry e = it.nextElement();
                if (!e.isDirectory()) try (InputStream in = jar.getInputStream(e)) { entries.put(e.getName(), in.readAllBytes()); }
            }
        }
        Map<String, ClassNode> nodes = new LinkedHashMap<String, ClassNode>();
        for (Map.Entry<String, String> pin : INPUT_SHA256.entrySet()) {
            byte[] bytes = entries.get(pin.getKey() + ".class");
            if (bytes == null || !pin.getValue().equals(sha(bytes))) fail("SHA256 " + pin.getKey());
            ClassNode node = new ClassNode(ASM8);
            new ClassReader(bytes).accept(node, ClassReader.EXPAND_FRAMES);
            nodes.put(pin.getKey(), node);
        }
        if (print) {
            System.out.println("RADIO=" + VsnPatch.fingerprint(VsnPatch.method(nodes.get("PRG/JR"), "a", RADIO)));
            System.out.println("STORY=" + VsnPatch.fingerprint(VsnPatch.method(nodes.get("PRG/Nb"), "a", STORY)));
            return;
        }
        Path output = Paths.get(args[1]).toAbsolutePath().normalize();
        Path allowed = Paths.get("localization/work/dialogue-wrap-test").toAbsolutePath().normalize();
        if (!output.startsWith(allowed) || output.equals(input) || Files.exists(output)) fail("new isolated output path required");
        // Also prove that a bad second target cannot partially mutate the first one.
        ClassNode bad = new ClassNode(ASM8);
        byte[] nb = entries.get("PRG/Nb.class");
        new ClassReader(nb).accept(bad, ClassReader.EXPAND_FRAMES);
        MethodNode badMethod = VsnPatch.method(bad, "a", STORY);
        badMethod.instructions.insert(new InsnNode(NOP));
        Map<String, ClassNode> negative = new LinkedHashMap<String, ClassNode>(nodes);
        negative.put("PRG/Nb", bad);
        String before = VsnPatch.fingerprint(VsnPatch.method(nodes.get("PRG/JR"), "a", RADIO));
        try { apply(negative); throw new AssertionError("accepted bad Nb"); }
        catch (IllegalStateException expected) { }
        if (!before.equals(VsnPatch.fingerprint(VsnPatch.method(nodes.get("PRG/JR"), "a", RADIO))))
            throw new AssertionError("partial mutation");
        apply(nodes);
        try (URLClassLoader hierarchy = new URLClassLoader(new URL[]{input.toUri().toURL(), Paths.get(args[2]).toUri().toURL()}, DialoguePatch.class.getClassLoader())) {
            for (Map.Entry<String, ClassNode> target : nodes.entrySet()) {
                ClassWriter writer = new ClassWriter(ClassWriter.COMPUTE_FRAMES | ClassWriter.COMPUTE_MAXS) {
                    protected ClassLoader getClassLoader() { return hierarchy; }
                };
                target.getValue().accept(writer);
                entries.put(target.getKey() + ".class", writer.toByteArray());
            }
        }
        try (ZipFile helpers = new ZipFile(args[2])) {
            Enumeration<? extends ZipEntry> it = helpers.entries();
            while (it.hasMoreElements()) {
                ZipEntry e = it.nextElement();
                if (!e.getName().endsWith(".class") || !(e.getName().startsWith("PRG/DialogueWrap")
                    || e.getName().startsWith("cosmoloc/layout/"))) continue;
                if (entries.containsKey(e.getName())) fail("helper collision " + e.getName());
                try (InputStream in = helpers.getInputStream(e)) { entries.put(e.getName(), in.readAllBytes()); }
            }
        }
        if (!entries.containsKey("PRG/DialogueWrap.class")) fail("missing runtime helper");
        Files.createDirectories(output.getParent());
        try (ZipOutputStream jar = new ZipOutputStream(Files.newOutputStream(output, StandardOpenOption.CREATE_NEW))) {
            for (Map.Entry<String, byte[]> e : entries.entrySet()) {
                jar.putNextEntry(new ZipEntry(e.getKey())); jar.write(e.getValue()); jar.closeEntry();
            }
        }
        System.out.println("PASS SHA pins, both-target atomic preflight, frames/maxs; patched only JR/Nb: " + output);
    }
}
