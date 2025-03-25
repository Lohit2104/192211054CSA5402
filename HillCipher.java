public class HillCipher {
    /* 3x3 Key Matrix */
    private static final int[][] KEY_MATRIX = {
            { 1, 2, 1 },
            { 2, 3, 2 },
            { 2, 2, 1 }
    };

    /* 3x3 Inverse Key Matrix */
    private static final int[][] INV_KEY_MATRIX = {
            { -1, 0, 1 },
            { 2, -1, 0 },
            { -2, 2, -1 }
    };

    private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    private static String encode(char a, char b, char c) {
        int posa = a - 'A';
        int posb = b - 'A';
        int posc = c - 'A';

        int x = (posa * KEY_MATRIX[0][0] + posb * KEY_MATRIX[1][0] + posc * KEY_MATRIX[2][0]) % 26;
        int y = (posa * KEY_MATRIX[0][1] + posb * KEY_MATRIX[1][1] + posc * KEY_MATRIX[2][1]) % 26;
        int z = (posa * KEY_MATRIX[0][2] + posb * KEY_MATRIX[1][2] + posc * KEY_MATRIX[2][2]) % 26;

        return "" + ALPHABET.charAt(x) + ALPHABET.charAt(y) + ALPHABET.charAt(z);
    }

    private static String decode(char a, char b, char c) {
        int posa = a - 'A';
        int posb = b - 'A';
        int posc = c - 'A';

        int x = (posa * INV_KEY_MATRIX[0][0] + posb * INV_KEY_MATRIX[1][0] + posc * INV_KEY_MATRIX[2][0]) % 26;
        int y = (posa * INV_KEY_MATRIX[0][1] + posb * INV_KEY_MATRIX[1][1] + posc * INV_KEY_MATRIX[2][1]) % 26;
        int z = (posa * INV_KEY_MATRIX[0][2] + posb * INV_KEY_MATRIX[1][2] + posc * INV_KEY_MATRIX[2][2]) % 26;

        // Ensure non-negative modulo values
        x = (x + 26) % 26;
        y = (y + 26) % 26;
        z = (z + 26) % 26;

        return "" + ALPHABET.charAt(x) + ALPHABET.charAt(y) + ALPHABET.charAt(z);
    }

    public static void main(String[] args) {
        String msg = "Security Laboratory";
        System.out.println("Hill Cipher Simulation\n--------------------------------------");
        System.out.println("Original Message : " + msg);

        msg = msg.toUpperCase().replaceAll("\\s", ""); // Convert to uppercase & remove spaces

        // Padding to make length a multiple of 3
        while (msg.length() % 3 != 0) {
            msg += 'X';
        }
        System.out.println("Padded Message   : " + msg);

        StringBuilder encryptedText = new StringBuilder();
        for (int i = 0; i < msg.length(); i += 3) {
            encryptedText.append(encode(msg.charAt(i), msg.charAt(i + 1), msg.charAt(i + 2)));
        }
        System.out.println("Encrypted Message: " + encryptedText);

        StringBuilder decryptedText = new StringBuilder();
        for (int i = 0; i < encryptedText.length(); i += 3) {
            decryptedText
                    .append(decode(encryptedText.charAt(i), encryptedText.charAt(i + 1), encryptedText.charAt(i + 2)));
        }
        System.out.println("Decrypted Message: " + decryptedText);
    }
}
