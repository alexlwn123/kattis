import java.util.*;
public class CC {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int stars = input.nextInt();

		System.out.println(stars + ":");

		for(int i = 2; i < stars/2 + 2; i++) {

			//System.out.print(3 % (i + i - 1));
			
			if((stars - i) % (i+i-1) == 0 || stars % (i + i - 1) == 0)
				System.out.println(i + "," + (i-1));

			if(stars % i == 0)
				System.out.println(i + "," + i);

		}
	}
}