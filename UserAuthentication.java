import java.util.HashMap;

public class UserAuthentication {
    private static HashMap<String, String[]> userDatabase = new HashMap<>();

    public static void registerUser(String username, String password)
            throws Exception {
        String salt = PasswordHasher.generateSalt();
        String hashedPassword = PasswordHasher.hashPassword(password,
                salt);
        userDatabase.put(username, new String[] { hashedPassword, salt });
        System.out.println("User registered successfully!");
    }

    public static boolean authenticateUser(String username, String password) throws Exception {
        if (userDatabase.containsKey(username)) {
            String[] storedData = userDatabase.get(username);
            String hashedPassword = PasswordHasher.hashPassword(password,
                    storedData[1]);
            return storedData[0].equals(hashedPassword);
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        registerUser("user1", "securePassword");
        boolean isAuthenticated = authenticateUser("user1",
                "securePassword");
        System.out.println("Authentication success: " + isAuthenticated);
    }
}