import java.net.*;
import java.util.Scanner;

public class DNSLookup {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        System.out.println("===== DNS Lookup Tool =====");

        do {
            System.out.println("\nMenu:");
            System.out.println("1. Find IP address from URL");
            System.out.println("2. Find URL (hostname) from IP address");
            System.out.println("3. Exit");
            System.out.print("Enter your choice (1-3): ");

            while (!scanner.hasNextInt()) {
                System.out.print("Invalid input! Enter number (1-3): ");
                scanner.next();
            }
            choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            try {
                switch (choice) {
                    case 1:
                        System.out.print("Enter URL (e.g., www.google.com): ");
                        String url = scanner.nextLine().trim();
                        if (url.isEmpty()) {
                            System.out.println("URL cannot be empty.");
                            break;
                        }
                        InetAddress inet = InetAddress.getByName(url);
                        System.out.println("Host Name: " + inet.getHostName());
                        System.out.println("IP Address: " + inet.getHostAddress());
                        break;

                    case 2:
                        System.out.print("Enter IP address (e.g., 142.250.183.132): ");
                        String ip = scanner.nextLine().trim();
                        if (ip.isEmpty()) {
                            System.out.println("IP cannot be empty.");
                            break;
                        }
                        InetAddress inetByIP = InetAddress.getByName(ip);
                        String hostName = inetByIP.getHostName();

                        if (hostName.equals(ip))
                            System.out.println("No hostname found. Reverse DNS lookup failed.");
                        else
                            System.out.println("Hostname for IP " + ip + ": " + hostName);
                        break;

                    case 3:
                        System.out.println("Exiting... Goodbye!");
                        break;

                    default:
                        System.out.println("Invalid choice! Please select 1–3.");
                }
            } catch (UnknownHostException e) {
                System.out.println("Lookup failed: " + e.getMessage());
            }

        } while (choice != 3);

        scanner.close();
    }
}
