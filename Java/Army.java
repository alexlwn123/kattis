import java.util.*;
public class Army {

    public static void main(String[] args)  {
        Scanner input = new Scanner(System.in);
        int cases = Integer.parseInt(input.nextLine());
        for(;cases > 0;cases--) {
            int ng = input.nextInt();
            int nm = input.nextInt();
            
            List<Integer> godzil = new ArrayList<Integer>();
            List<Integer> mecha = new ArrayList<Integer>();

            for(int i = 0; i < ng; i++) {
                godzil.add(input.nextInt());
            }
            for(int i = 0; i < nm; i++) {
                mecha.add(input.nextInt());
            }

            Collections.sort(godzil);
            Collections.sort(mecha);

            while(godzil.size() > 0 && mecha.size() > 0) {
                if(godzil.get(0) < mecha.get(0))
                    godzil.remove(0);
                else
                    mecha.remove(0);
            }

            System.out.println((godzil.size() == 0 ? "MechaGodzilla" : "Godzilla"));
        }
    }
}
