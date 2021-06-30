import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class csvToNodes {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("/home/bhavesh/Downloads/Padloc_Defense.csv"));
        HashMap<String,SalmonellaStrain> strains = new HashMap<String, SalmonellaStrain>();
        while (sc.hasNext()){
            String line = sc.nextLine();
            String[] words = line.split(",");
            System.out.println(Arrays.toString(words));
        }
        sc.close();
    }
}
