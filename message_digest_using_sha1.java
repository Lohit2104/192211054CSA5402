import java.security.*;
import java.nio.charset.StandardCharsets;

public class message_digest_using_sha1 {
    public static void main(String[] a) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA1");
            System.out.println("Message digest object info:\n------------------------------ ");
            System.out.println("Algorithm=" + md.getAlgorithm());
            System.out.println("Provider=" + md.getProvider());
            System.out.println("ToString=" + md.toString());

            String input = "";
            md.update(input.getBytes(StandardCharsets.UTF_8));
            byte[] output = md.digest();
            System.out.println("\nSHA1(\"" + input + "\")=" + bytesToHex(output));

            input = "abc";
            md.update(input.getBytes(StandardCharsets.UTF_8));
            output = md.digest();
            System.out.println("\nSHA1(\"" + input + "\")=" + bytesToHex(output));

            input = "abcdefghijklmnopqrstuvwxyz";
            md.update(input.getBytes(StandardCharsets.UTF_8));
            output = md.digest();
            System.out.println("\nSHA1(\"" + input + "\")=" + bytesToHex(output));

        } catch (Exception e) {
            System.out.println("Exception: " + e);
        }
    }

    private static String bytesToHex(byte[] b) {
        StringBuilder buf = new StringBuilder();
        for (byte aB : b) {
            buf.append(String.format("%02X", aB));
        }
        return buf.toString();
    }
}
