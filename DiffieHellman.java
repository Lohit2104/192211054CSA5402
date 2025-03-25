import java.math.BigInteger;

class DiffieHellman {
    public static void main(String args[]) {
        int p = 23; // Public prime number
        int g = 5; // Public primitive root

        int x = 4; // Alice's private key
        int y = 3; // Bob's private key

        System.out.println(
                "Simulation of Diffie-Hellman Key Exchange Algorithm\n-------------------------------------------------");

        // Alice computes g^x mod p
        BigInteger aliceSends = BigInteger.valueOf(g).modPow(BigInteger.valueOf(x), BigInteger.valueOf(p));
        System.out.println("Alice Sends : " + aliceSends);

        // Bob computes g^y mod p
        BigInteger bobSends = BigInteger.valueOf(g).modPow(BigInteger.valueOf(y), BigInteger.valueOf(p));
        System.out.println("Bob Sends : " + bobSends);

        // Bob computes (Alice's value)^y mod p
        BigInteger bobComputes = aliceSends.modPow(BigInteger.valueOf(y), BigInteger.valueOf(p));
        System.out.println("Bob Computes : " + bobComputes);

        // Alice computes (Bob's value)^x mod p
        BigInteger aliceComputes = bobSends.modPow(BigInteger.valueOf(x), BigInteger.valueOf(p));
        System.out.println("Alice Computes : " + aliceComputes);

        // Shared secret should be the same for both Alice and Bob
        if (aliceComputes.equals(bobComputes)) {
            System.out.println("Success: Shared Secret Matches! " + aliceComputes);
        } else {
            System.out.println("Error: Shared Secrets do not Match!");
        }
    }
}
