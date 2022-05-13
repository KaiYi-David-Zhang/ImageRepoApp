import java.awt.*;
import java.io.*;

public class ImageRepo {
    static int key = 11111111;
    int IV = 1;
    public static void main(String[] args) {
        String command = args[0];
        if(command.equals("-encrypt") || command.equals("-en")){
            encrypt(args[1]);
        }
        else if(command.equals("-decrypt") || command.equals("-de")){
            decrypt(args[1]);
        }



    }

    private static void encrypt(String filename){
        try {
            FileInputStream fis = new FileInputStream(filename);
            byte encrypt[] = new byte[fis.available()];
            fis.read(encrypt);
            int i = 0;
            for (byte b : encrypt){
                encrypt[i] = (byte) (b ^ key);
                i++;
            }
            File newFile = new File(filename + "en");
            newFile.createNewFile();
            FileOutputStream fos = new FileOutputStream(newFile, false);
            fos.write(encrypt);
            fos.close();
            fis.close();
            System.out.println("finished");
        } catch (FileNotFoundException e) {
            System.out.println("The file was not found.");
            return;
        }
        catch (IOException io){
            io.printStackTrace();
            return;
        }
    }
    private static void decrypt(String filename){
        try {
            FileInputStream fis = new FileInputStream(filename);
            byte decrypt[] = new byte[fis.available()];
            fis.read(decrypt);
            int i = 0;
            for (byte b : decrypt){
                decrypt[i] = (byte) (b ^ key);
                i++;
            }
            File newFile = new File(filename.substring(0, filename.length()-2));
            newFile.createNewFile();
            FileOutputStream fos = new FileOutputStream(newFile, false);
            fos.write(decrypt);
            fos.close();
            fis.close();
            System.out.println("finished");
        } catch (FileNotFoundException e) {
            System.out.println("The file was not found.");
            return;
        }
        catch (IOException io){
            io.printStackTrace();
            return;
        }
    }
}
