import java.io.*;
import java.security.AccessControlException;
import java.util.Scanner;

public class SecureLogin {
    public static void main(String[] args) {
        System.setSecurityManager(new SecurityManager());
        String correctUsername = "admin";
        String correctPassword = "password123";

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter username: ");
        String username = scanner.nextLine();
        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        if (username.equals(correctUsername) &&
                password.equals(correctPassword)) {
            System.out.println("Login Successful!");
            try {
                FileWriter writer = new FileWriter("login.txt", true);
                writer.write("User " + username + " logged in successfully.\n");
                writer.close();
            } catch (AccessControlException e) {
                System.out.println("Security Exception: File write access denied!");
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            System.out.println("Invalid Credentials!");
        }
        scanner.close();
    }
}
