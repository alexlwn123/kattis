import java.util.*;
public class Ants {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int cases = (int) input.nextInt();

		for(; cases > 0; cases--) {
			int len = input.nextInt();
			int antcount = input.nextInt();

			int[] ants = new int[antcount];
			for(int i = 0; i < antcount; i++) {
				ants[i] = input.nextInt();
			}

			int min = Arrays.stream(ants)
						.min()
						.orElse(0);
			int max = Arrays.stream(ants)
						.max()
						.orElse(0);
			int mid = Arrays.stream(ants)
						.map(x -> Math.min(x, len-x))
						.max()
						.orElse(0);
			System.out.println(mid + " " + Math.max(len - min, max));
		}
	}
}