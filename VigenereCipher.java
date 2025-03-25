public class VigenereCipher {

    // Encrypt function
    static String encrypt(String text, final String key) {
        StringBuilder res = new StringBuilder();
        String upperText = text.toUpperCase(); // Convert text to uppercase
        String upperKey = key.toUpperCase(); // Convert key to uppercase

        int j = 0; // key index
        for (int i = 0; i < upperText.length(); i++) {
            char c = upperText.charAt(i);

            if (Character.isLetter(c)) {
                char encryptedChar = (char) ((c + upperKey.charAt(j) - 2 * 'A') % 26 + 'A');
                res.append(encryptedChar);
                j = (j + 1) % upperKey.length();
            } else {
                res.append(c); // Keep spaces and special characters
            }
        }
        return res.toString();
    }

    // Decrypt function
    static String decrypt(String text, final String key) {
        StringBuilder res = new StringBuilder();
        String upperText = text.toUpperCase(); // Convert text to uppercase
        String upperKey = key.toUpperCase(); // Convert key to uppercase

        int j = 0; // key index
        for (int i = 0; i < upperText.length(); i++) {
            char c = upperText.charAt(i);

            if (Character.isLetter(c)) {
                char decryptedChar = (char) ((c - upperKey.charAt(j) + 26) % 26 + 'A');
                res.append(decryptedChar);
                j = (j + 1) % upperKey.length();
            } else {
                res.append(c); // Keep spaces and special characters
            }
        }
        return res.toString();
    }

    public static void main(String[] args) {
        String key = "VIGENERECIPHER";
        String msg = "Security Laboratory 123!";

        System.out.println("Vigenère Cipher Simulation\n--------------------------------------");
        System.out.println("Original Message  : " + msg);

        String encrypted = encrypt(msg, key);
        System.out.println("Encrypted Message : " + encrypted);

        String decrypted = decrypt(encrypted, key);
        System.out.println("Decrypted Message : " + decrypted);
    }
}