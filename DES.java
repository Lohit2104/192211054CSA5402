import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.Arrays;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.KeyGenerator;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;

public class DES {
    public static void main(String[] argv) {
        try {
            System.out.println("Message Encryption Using DES Algorithm\n----------------------");

            // Generate a DES key
            KeyGenerator keygenerator = KeyGenerator.getInstance("DES");
            SecretKey myDesKey = keygenerator.generateKey();

            // Initialize cipher
            Cipher desCipher = Cipher.getInstance("DES/ECB/PKCS5Padding");

            // Encrypt
            desCipher.init(Cipher.ENCRYPT_MODE, myDesKey);
            byte[] text = "Secret Information".getBytes();
            System.out.println("Original Message: " + new String(text));
            System.out.println("Message [Byte Format]: " + Arrays.toString(text));

            byte[] textEncrypted = desCipher.doFinal(text);
            String encryptedBase64 = Base64.getEncoder().encodeToString(textEncrypted);
            System.out.println("Encrypted Message: " + encryptedBase64);

            // Decrypt
            desCipher.init(Cipher.DECRYPT_MODE, myDesKey);
            byte[] textDecrypted = desCipher.doFinal(textEncrypted);
            System.out.println("Decrypted Message: " + new String(textDecrypted));

        } catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException
                | IllegalBlockSizeException | BadPaddingException e) {
            e.printStackTrace();
        }
    }
}
