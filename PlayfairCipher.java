import java.awt.Point;

public class PlayfairCipher {
    private static char[][] charTable;
    private static Point[] positions;

    private static String prepareText(String s, boolean chgJtoI) {
        s = s.toUpperCase().replaceAll("[^A-Z]", "");
        return chgJtoI ? s.replace("J", "I") : s.replace("Q", "");
    }

    private static void createTbl(String key, boolean chgJtoI) {
        charTable = new char[5][5];
        positions = new Point[26];

        String s = prepareText(key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ", chgJtoI);
        int k = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (positions[c - 'A'] == null) {
                charTable[k / 5][k % 5] = c;
                positions[c - 'A'] = new Point(k % 5, k / 5);
                k++;
            }
        }
    }

    private static String codec(StringBuilder txt, int dir) {
        for (int i = 0; i < txt.length(); i += 2) {
            char a = txt.charAt(i);
            char b = txt.charAt(i + 1);
            int row1 = positions[a - 'A'].y, col1 = positions[a - 'A'].x;
            int row2 = positions[b - 'A'].y, col2 = positions[b - 'A'].x;

            if (row1 == row2) { // Same row
                col1 = Math.floorMod(col1 + dir, 5);
                col2 = Math.floorMod(col2 + dir, 5);
            } else if (col1 == col2) { // Same column
                row1 = Math.floorMod(row1 + dir, 5);
                row2 = Math.floorMod(row2 + dir, 5);
            } else { // Rectangle swap
                int temp = col1;
                col1 = col2;
                col2 = temp;
            }

            txt.setCharAt(i, charTable[row1][col1]);
            txt.setCharAt(i + 1, charTable[row2][col2]);
        }
        return txt.toString();
    }

    private static String encode(String s) {
        StringBuilder sb = new StringBuilder(s);
        for (int i = 0; i < sb.length(); i += 2) {
            if (i == sb.length() - 1) {
                sb.append('X'); // Append X if odd length
            } else if (sb.charAt(i) == sb.charAt(i + 1)) {
                sb.insert(i + 1, 'X');
            }
        }
        return codec(sb, 1);
    }

    private static String decode(String s) {
        return codec(new StringBuilder(s), -1); // Decrypt using -1 direction
    }

    public static void main(String[] args) {
        String key = "CSE";
        String txt = "Security Lab"; // Original message
        boolean chgJtoI = true; // Replace 'J' with 'I'

        createTbl(key, chgJtoI);
        String preparedText = prepareText(txt, chgJtoI);
        String enc = encode(preparedText);

        System.out.println("Playfair Cipher Simulation");
        System.out.println("--------------------------------------");
        System.out.println("Original Message : " + txt);
        System.out.println("Encrypted Message: " + enc);
        System.out.println("Decrypted Message: " + decode(enc));
    }
}
