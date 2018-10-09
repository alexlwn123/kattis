import java.util.*;
import java.util.stream.Collectors;
public class A {

	public static void main(String args[]) {
		Scanner input = new Scanner(System.in);
		int width = input.nextInt();
		int n = input.nextInt();

		ArrayList<Integer> walls = new ArrayList<Integer>(); 
		walls.add(0);
		walls.add(width);



		for(int i = 0; i < n; i++) 
			walls.add(input.nextInt());

		//System.out.println(walls.toString());
		
		ArrayList<Integer> out = new ArrayList<Integer>();

		for(int i = 0; i < walls.size(); i++) {
			for(int j = 0; j < walls.size(); j++) {
				out.add(walls.get(i) - walls.get(j));
			}
		}
		//System.out.println(out.toString());

		int[] ints = out.stream()
				.mapToInt(x -> Math.abs(x))
				.distinct()
				.sorted()
				.filter(x -> x != 0)
				.toArray();


		for(int x: ints) {
			System.out.print(x + " ");
		}

	}

}
