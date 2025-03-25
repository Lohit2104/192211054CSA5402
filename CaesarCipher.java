class CaesarCipher {
    public static String encode(String enc, int offset) {
        offset = (offset % 26 + 26) % 26; // Ensure valid offset
        StringBuilder encoded = new StringBuilder();

        for (char i : enc.toCharArray()) {
            if (Character.isLetter(i)) {
                if (Character.isUpperCase(i)) {
                    encoded.append((char) ('A' + (i - 'A' + offset) % 26));
                } else {
                    encoded.append((char) ('a' + (i - 'a' + offset) % 26));
                }
            } else {
                encoded.append(i); // Keep non-alphabet characters unchanged
            }
        }
        return encoded.toString();
    }

    public static String decode(String enc, int offset) {
        return encode(enc, 26 - offset); // Reverse the shift
    }

    public static void main(String[] args) {
        String msg = "Anna University";
        int shift = 3;

        System.out.println("Simulating Caesar Cipher");
        System.out.println("--------------------------------------");
        System.out.println("Input Message       : " + msg);

        String encrypted = encode(msg, shift);
        System.out.println("Encrypted Message   : " + encrypted);

        String decrypted = decode(encrypted, shift);
        System.out.println("Decrypted Message   : " + decrypted);
    }
}
