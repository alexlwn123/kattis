import java.util.*;
public class F {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int low = 1;
		int high = 10;
		while (input.hasNextLine()) {
			int guess = Integer.parseInt(input.nextLine());
			if (guess== 0)
				return;
			
			String info = input.nextLine();
			
			if (info.equals("too high") && high >= guess)
				high = guess-1;
			if (info.equals("too low") && low <= guess)
				low = guess+1;



			if (info.equals("right on")) {
				if (low > high || guess < low || guess > high) {
					System.out.println("Stan is dishonest");
					low = 1;
					high = 10;
				}
				
				else {
					System.out.println("Stan may be honest");
					low = 1;
					high = 10;
				}	

			}	
		}

	}
}