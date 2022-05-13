import java.awt.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;


public class ImageRepo {
    static int key = 1241085523;
    static int IV = -1826778;
    static String database = "database";
    static String display = "display";

    public static void main(String[] args) {
        String command = args[0];
        /*
        if(command.equals("-encrypt") || command.equals("-en")){
            encryptFile(args[1]);
        }
        else if(command.equals("-decrypt") || command.equals("-de")){
            decryptFile(args[1]);
        }
        */
        if(command.equals("-add")){
            addFile(args[1]);
        }
        else if(command.equals("-list")){
            listFile();
        }
        else if(command.equals("-display")){
            displayFile(args[1]);
        }

    }

    private static void addFile(String filename) {
        File path = new File(database);
        if(!Files.exists(Paths.get(database))){
            path.mkdir();
        }
        encryptFile(filename);
    }

    private static void displayFile(String imageName) {
        File path = new File(display);
        if(!Files.exists(Paths.get(display))){
            path.mkdir();
        }
        decryptFile(imageName);
    }

    private static void listFile() {
        File path = new File(database);
        if(!Files.exists(Paths.get(database))){
            path.mkdir();
        }
        String[] files;
        files = path.list();
        for (String file : files){
            //System.out.println(file.split(".")[0]);
            System.out.println(file.substring(0, file.length()-2));
        }
    }

    // the file are encrypted and decrypted in CBC mode
    private static void encryptFile(String filename){
        try {
            FileInputStream fis = new FileInputStream(filename);
            byte encrypt[] = new byte[fis.available()];
            fis.read(encrypt);
            encrypt[0] = (byte) (encrypt[0] ^ IV);
            encrypt[0] = encrypt(encrypt[0]);
            for (int i = 1; i < encrypt.length; i++){
                encrypt[i] = (byte) (encrypt[i] ^ encrypt[i-1]);
                encrypt[i] = encrypt(encrypt[i]);
            }
            Path path = Paths.get(filename);
            String newFileName = path.getFileName() + "en";
            File dir = new File(database);

            File newFile = new File(dir, newFileName);
            newFile.createNewFile();
            FileOutputStream fos = new FileOutputStream(newFile, false);
            fos.write(encrypt);
            fos.close();
            fis.close();
            System.out.println("encryption finished");
        } catch (FileNotFoundException e) {
            System.out.println("The file was not found.");
            return;
        }
        catch (IOException io){
            io.printStackTrace();
            return;
        }
    }
    private static void decryptFile(String filename){
        try {
            Path path = Paths.get(filename);
            String newFileName = path.getFileName() + "en";
            File dir = new File(database);
            File newFile = new File(dir, newFileName);

            FileInputStream fis = new FileInputStream(newFile);
            byte decrypt[] = new byte[fis.available()];
            fis.read(decrypt);

            for (int i = decrypt.length - 1; i >= 0; i--){
                decrypt[i] = decrypt(decrypt[i]);
                if(i == 0){
                    decrypt[i] = (byte) (decrypt[i] ^ IV);
                }
                else{
                    decrypt[i] = (byte) (decrypt[i] ^ decrypt[i - 1]);
                }
            }

            String fileName = path.getFileName() + "";
            File displayDir = new File(display);
            File displayFile = new File(displayDir, fileName);

            displayFile.createNewFile();
            FileOutputStream fos = new FileOutputStream(displayFile, false);
            fos.write(decrypt);
            fos.close();
            fis.close();
            System.out.println("decryption finished");
        } catch (FileNotFoundException e) {
            System.out.println("The file was not found.");
            return;
        }
        catch (IOException io){
            io.printStackTrace();
            return;
        }
    }

    // just using XOR not very secure but by updating these function we can use more secured functions
    // like AES or other block ciphers
    private static byte encrypt (byte block){
        return (byte)(block ^ key);
    }
    private static byte decrypt (byte block){
        return (byte)(block ^ key);
    }
}
