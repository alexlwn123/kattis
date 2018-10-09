import java.util.*;
public class EE{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int low = 0;
		int high = 1001;
		int half = (low + high) / 2;
		while(true) {
			System.out.println(half);
			System.out.flush();
			String ans = input.nextLine();

			if (ans.equals("correct")) break;

			if (ans.equals("higher")) {
				low = half;
				half = (low + high) / 2;
			}
			else {
				high = half;
				half = (high + low) / 2;
			}
		}
	}
}