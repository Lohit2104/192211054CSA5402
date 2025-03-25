import java.util.Scanner;

class RailFenceCipher {

    public static String encrypt(String text, int depth) {
        if (depth <= 1)
            return text; // No transformation needed for depth 1

        int len = text.length();
        char[][] rail = new char[depth][len];
        boolean down = false;
        int row = 0;

        // Fill the rail fence matrix
        for (int i = 0; i < len; i++) {
            // Change direction if we reach the top or bottom row
            if (row == 0 || row == depth - 1) {
                down = !down;
            }
            rail[row][i] = text.charAt(i);
            row += down ? 1 : -1;
        }

        // Read from rail in row-wise order to get ciphertext
        StringBuilder cipherText = new StringBuilder();
        for (char[] chars : rail) {
            for (char ch : chars) {
                if (ch != 0)
                    cipherText.append(ch);
            }
        }

        return cipherText.toString();
    }

    public static String decrypt(String cipher, int depth) {
        if (depth <= 1)
            return cipher;

        int len = cipher.length();
        char[][] rail = new char[depth][len];
        boolean down = false;
        int row = 0;

        // Mark positions in rail matrix
        for (int i = 0; i < len; i++) {
            if (row == 0 || row == depth - 1) {
                down = !down;
            }
            rail[row][i] = '*';
            row += down ? 1 : -1;
        }

        // Fill rail matrix with ciphertext characters
        int index = 0;
        for (int i = 0; i < depth; i++) {
            for (int j = 0; j < len; j++) {
                if (rail[i][j] == '*' && index < cipher.length()) {
                    rail[i][j] = cipher.charAt(index++);
                }
            }
        }

        // Read the rail matrix in a zig-zag pattern to get plaintext
        StringBuilder plainText = new StringBuilder();
        row = 0;
        down = false;
        for (int i = 0; i < len; i++) {
            if (row == 0 || row == depth - 1) {
                down = !down;
            }
            plainText.append(rail[row][i]);
            row += down ? 1 : -1;
        }

        return plainText.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter message to encrypt:");
        String message = sc.nextLine();

        System.out.println("Enter rail depth:");
        int depth = sc.nextInt();
        sc.close();

        String encrypted = encrypt(message.replaceAll("\\s", ""), depth);
        String decrypted = decrypt(encrypted, depth);

        System.out.println("\nRail Fence Cipher Simulation");
        System.out.println("-----------------------------");
        System.out.println("Original Message: " + message);
        System.out.println("Encrypted Message: " + encrypted);
        System.out.println("Decrypted Message: " + decrypted);
    }
}
