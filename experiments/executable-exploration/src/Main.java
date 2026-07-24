import java.io.FileInputStream;
import java.nio.file.Files;
import java.nio.file.Path;



public class Main {

    private static String byteToHex(int value) {
        return String.format("%02X", value & 0xFF);
    }

    private static boolean isValidDOSHeader(byte[] header) {

        if (header.length < 2) {
            return false;
        }

        return header[0] == 0x4D && header[1] == 0x5A;
    }

    public static void main(String[] args) {

        Path filePath = Path.of("C:/Users/nrror/reverse-engine-platform/hello.exe");

        if (!Files.exists(filePath)) {
            System.out.println("File does not exist.");
            return;
        }

        try (FileInputStream input = new FileInputStream(filePath.toFile())) {

            byte[] header = new byte[64];
            input.read(header);

            String magicFirst = byteToHex(header[0]);
            String magicSecond = byteToHex(header[1]);

            System.out.println("Magic:");
            System.out.println(magicFirst + " " + magicSecond + "\n");

            System.out.println("Valid DOS Header:");
            if (isValidDOSHeader(header)) {
                System.out.println("Valid");

            } else {
                System.out.println("Invalid");
            }
    

        } catch (Exception e) {
            System.out.println("could not open file.");
        }

    }
    
}
