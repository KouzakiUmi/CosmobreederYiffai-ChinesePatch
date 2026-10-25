import PRG.SaveMenuLayout;
import java.nio.file.Paths;

/** No game startup or menu/state access: only the test helper's static toggle. */
public final class TestInstallProfileProbe {
    public static void main(String[] args) throws Exception {
        String actual = Paths.get(SaveMenuLayout.class.getProtectionDomain().getCodeSource().getLocation().toURI()).toRealPath().toString();
        String expectedJar = Paths.get(args[0]).toRealPath().toString();
        boolean expected = Boolean.parseBoolean(args[1]);
        if (!actual.equals(expectedJar)) throw new AssertionError("Helper did not load from test JAR");
        if (SaveMenuLayout.prototypeEnabled() != expected) throw new AssertionError("Wrong test activation default/override");
        SaveMenuLayout.validateGeometry();
        SaveMenuLayout.disablePrototype();
        if (SaveMenuLayout.prototypeEnabled()) throw new AssertionError("Disable API failed");
        SaveMenuLayout.configurePrototype();
        if (!SaveMenuLayout.prototypeEnabled()) throw new AssertionError("Enable API failed");
        SaveMenuLayout.disablePrototype();
        System.out.println("TEST_INSTALL_PROFILE_PASS expected=" + expected + "; no scene/save/native/game main");
    }
}
