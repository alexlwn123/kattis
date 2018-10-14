import java.util.*;
public class Cold {

	public static void main(String args[]) {
		Scanner scanner = new Scanner(System.in);
		int len = Integer.parseInt(scanner.nextLine());
		String[] ints = scanner.nextLine().split(" ");
		//int[] nums = new int[len];

		int out = (int) Arrays.stream(ints)
						.filter(x -> Integer.parseInt(x) < 0)
						.count();
		System.out.println(out);
	}
}