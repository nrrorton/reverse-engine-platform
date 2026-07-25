import java.io.FileInputStream;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
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

    private static int getPEHeaderOffset(byte[] header) {

        ByteBuffer buffer = ByteBuffer.wrap(header);
        buffer.order(ByteOrder.LITTLE_ENDIAN);
        return buffer.getInt(0x3C);
    }

    private static ByteBuffer createLittleEndianBuffer(byte[] bytes) {

        ByteBuffer buffer = ByteBuffer.wrap(bytes);
        buffer.order(ByteOrder.LITTLE_ENDIAN);
        return buffer;
    }

    private static int getMachineType(byte[] coffHeader) {

        ByteBuffer buffer = createLittleEndianBuffer(coffHeader);
        return buffer.getShort(0) & 0xFFFF;
    }

    private static String getMachineName(int machineType) {

        return switch (machineType) {

            case 0x14C -> "x86";

            case 0x8664 -> "x64";

            case 0xAA64 -> "ARM64";

            default -> String.format("Unknown (0x%04X)", machineType);
        };
    }

    private static int getNumberOfSections(byte[] coffHeader) {

        ByteBuffer buffer = createLittleEndianBuffer(coffHeader);
        return buffer.getShort(2) & 0xFFFF;
    }

    private static int getOptionalHeaderSize(byte[] coffHeader) {

        ByteBuffer buffer = createLittleEndianBuffer(coffHeader);
        return buffer.getShort(16) & 0xFFFF;
    }

    private static String getSectionName(byte[] sectionHeader) {

        StringBuilder name = new StringBuilder();

        for (int i = 0; i < 8; i++) {
            if (sectionHeader[i] == 0) {
                break;
            }
            name.append((char) sectionHeader[i]);
        }
        return name.toString();
    }

    private static int getSectionTableOffset(int peOffset, int optionalHeaderSize) {
        return peOffset + 4 + 20 + optionalHeaderSize;
    }

    private static int getSectionVirtualSize(byte[] sectionHeader) {

        ByteBuffer buffer = createLittleEndianBuffer(sectionHeader);
        return buffer.getInt(8);
    }

    private static int getSectionVirtualAddress(byte[] sectionHeader) {

        ByteBuffer buffer = createLittleEndianBuffer(sectionHeader);
        return buffer.getInt(12);
    }

    private static int getSectionRawSize(byte[] sectionHeader) {

        ByteBuffer buffer = createLittleEndianBuffer(sectionHeader);
        return buffer.getInt(16);
    }

    private static int getSectionRawPointer(byte[] sectionHeader) {

        ByteBuffer buffer = createLittleEndianBuffer(sectionHeader);
        return buffer.getInt(20);
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

            System.out.println("============================================");
            System.out.println("           Executable Inspector");
            System.out.println("============================================");
            System.out.println();
            System.out.println("File: " + filePath.getFileName());
            System.out.println();

            System.out.println("DOS Header");
            System.out.println("-----------------------------------");
            System.out.printf("Magic Number : %s %s%n", magicFirst, magicSecond);
            System.out.printf("Valid        : %s%n", 
                    isValidDOSHeader(header) ? "Yes" : "No");
            System.out.println();

            int peOffset = getPEHeaderOffset(header);
            input.getChannel().position(peOffset);

            byte[] peSignature = new byte[4];
            input.read(peSignature);

            System.out.println("PE Header");
            System.out.println("-----------------------------------");
            System.out.printf("Offset       : 0x%X%n", peOffset);
            System.out.print("Signature    : ");

            for (byte b : peSignature) {
                System.out.print(byteToHex(b) + " ");
            }
            System.out.println("\n");

            byte[] coffHeader = new byte[20];
            input.read(coffHeader);

            int machine = getMachineType(coffHeader);
            int optionalHeaderSize = getOptionalHeaderSize(coffHeader);

            System.out.println("COFF Header");
            System.out.println("-----------------------------------");
            System.out.printf("Machine      : %s%n", getMachineName(machine));
            System.out.printf("Sections     : %d%n", getNumberOfSections(coffHeader));

            System.out.printf("Optional Hdr : %d bytes%n", optionalHeaderSize);

            int sectionTableOffset = getSectionTableOffset(peOffset, optionalHeaderSize);
            input.getChannel().position(sectionTableOffset);

            System.out.println();
            System.out.println("Sections");
            System.out.println("-----------------------------------");

            int numberOfSections = getNumberOfSections(coffHeader);

            if (numberOfSections <= 0) {
                System.out.println("No sections found.");
                return;
            }

            for (int i = 0; i < numberOfSections; i++) {

                byte[] sectionHeader = new byte[40];
                input.read(sectionHeader);

                String name = getSectionName(sectionHeader);
                int virtualSize = getSectionVirtualSize(sectionHeader);
                int virtualAddress = getSectionVirtualAddress(sectionHeader);
                int rawSize = getSectionRawSize(sectionHeader);
                int rawPointer = getSectionRawPointer(sectionHeader);

                System.out.printf("%2d. Section Name : %s%n", i + 1, name);

                System.out.printf("    Virtual Size : 0x%X%n", virtualSize);
                System.out.printf("    Virtual Addr : 0x%X%n", virtualAddress);
                System.out.printf("    Raw Size     : 0x%X%n", rawSize);
                System.out.printf("    Raw Offset   : 0x%X%n", rawPointer);

                System.out.println();
            }
    

        } catch (Exception e) {
            System.out.println("could not open file.");
        }

    }
    
}
