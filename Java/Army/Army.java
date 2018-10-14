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
			int godzilmax = 0;
			int mechmax = 0;
			for(int i = 0; i < ng; i++) {
				int x = input.nextInt();
				if(x > godzilmax)
					godzilmax = x;
			}
			for(int i = 0; i < nm; i++) {
				int x = input.nextInt();
				if(x > mechmax)
					mechmax = x;
			}

			//Collections.sort(godzil);
			//Collections.sort(mecha);


			System.out.println(mechmax > godzilmax ? "MechaGodzilla" : "Godzilla");
		}
	}
}