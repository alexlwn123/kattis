import java.util.*;
public class BB {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while(input.hasNextLine()) {
			int first = input.nextInt();
			int second = input.nextInt();

			if(first == 0 && second == 0)
				return;

			System.out.println(first / second + " " + first % second + " / " + second);

		}
	}
}