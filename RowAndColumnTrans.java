import java.util.Scanner;

class RowAndColumnTrans {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        // Input
        System.out.println("Enter the plain text:");
        String pl = sc.nextLine();
        sc.close();

        // Remove spaces
        String s = pl.replaceAll("\\s", "");
        System.out.println("Processed text (spaces removed): " + s);

        // Define column size
        int col = 4;

        // Compute required rows
        int row = (int) Math.ceil(s.length() / (double) col);

        // Create and fill matrix with padding ('#' if needed)
        char[][] ch = new char[row][col];
        int index = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (index < s.length()) {
                    ch[i][j] = s.charAt(index++);
                } else {
                    ch[i][j] = '#'; // Padding
                }
            }
        }

        // Transpose the matrix
        char[][] trans = new char[col][row];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                trans[j][i] = ch[i][j];
            }
        }

        // Display Transposed Cipher Text
        System.out.print("Cipher Text: ");
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                System.out.print(trans[i][j]);
            }
        }
        System.out.println(); // New line for output clarity
    }
}
