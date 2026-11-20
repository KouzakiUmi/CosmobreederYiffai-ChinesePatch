import java.nio.file.*;
import java.util.*;

/** Resolves and verifies classes without initializing the game or opening a window. */
public final class VerifyLayout {
    public static void main(String[] args) throws Exception {
        int count = 0;
        for (String name : Files.readAllLines(Paths.get(args[0]))) {
            if (name.trim().isEmpty()) continue;
            Class<?> type = Class.forName(name.trim(), false, VerifyLayout.class.getClassLoader());
            type.getDeclaredMethods();
            type.getDeclaredConstructors();
            count++;
        }
        System.out.println("VERIFIED_NO_INITIALIZATION " + count);
    }
}
