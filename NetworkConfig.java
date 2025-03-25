import java.io.*;

public class NetworkConfig {
    public static void main(String[] args) {
        try {
            Process process = Runtime.getRuntime().exec("ipconfig"); // Change to "ifconfig" for Linux
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.contains("Subnet Mask") || line.contains("Gateway")) {
                    System.out.println(line.trim());
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}