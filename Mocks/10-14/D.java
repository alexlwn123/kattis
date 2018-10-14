import java.util.*;
public class D {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		int linelen = input.nextInt();

		int[] line = Arrays.stream(input.nextLine().split(" ")).mapToInt(x -> Integer.parseInt(x)).toArray();
		int[] dp = new int[linelen];

		ArrayList<Integer> longestchain = new ArrayList();

		


		int totalmax = 0;

		for(int i = 1; i < linelen; i++) {
			int maxLen = 0;
			ArrayList<Integer>[] chains = new ArrayList[i];

			for(int j = 0; j < i; j++) {
				if(line[j] < line[i]) {
					maxLen = Math.max(maxLen, dp[j]);
					chains[i].add(line[j]);
				}
			}

			dp[i] += maxLen;

			
			if(dp[i] > totalmax) {
				totalmax = dp[i];
				longestchain = chains[i];
			}
			totalmax = Math.max(totalmax, dp[i]);


		}
		System.out.println(totalmax);



	}

}