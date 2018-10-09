import java.util.*;

public class D {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		ArrayList<Integer> nums = new ArrayList<>();
		while(input.hasNextInt())
			nums.add(input.nextInt());
		int n = nums.get(0);
		int t = nums.get(1);

		int count = 0;
			

		for(int i = 2; i < nums.size(); i++) {
			int x = nums.get(i);
			t -= x;
			if(t < 0) {
				System.out.println(count);
				return;
			}
			count++;
		}

		System.out.println(count);
		
	}
}