import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpsConfigurator;
import com.sun.net.httpserver.HttpsServer;
import javax.net.ssl.*;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.security.KeyStore;
import java.io.FileInputStream;

public class HttpsServerExample {
    public static void main(String[] args) throws Exception {
        // Load the keystore
        char[] password = "password".toCharArray();
        KeyStore ks = KeyStore.getInstance("JKS");
        FileInputStream fis = new FileInputStream("keystore.jks");
        ks.load(fis, password);

        // Set up the KeyManager
        char[] keyPassword = "abinaya".toCharArray(); // use the password you've set up in the command prompt for the
                                                      // keystore
        KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
        kmf.init(ks, keyPassword);

        // Set up the SSL context
        SSLContext sslContext = SSLContext.getInstance("TLS");

        sslContext.init(kmf.getKeyManagers(), null, null);

        // Create HTTPS server
        HttpsServer server = HttpsServer.create(new InetSocketAddress(8443), 0);
        server.setHttpsConfigurator(new HttpsConfigurator(sslContext));
        server.createContext("/test", exchange -> {
            String response = "Hello, Secure World!";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        });

        server.setExecutor(null);
        server.start();
        System.out.println("HTTPS server started on port 8443");
    }
}