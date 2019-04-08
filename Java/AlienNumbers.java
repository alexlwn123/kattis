import java.util.*;
public class AlienNumbers {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int cases = Integer.parseInt(input.nextLine());
		int currentcase = 1;
		while(input.hasNextLine()) {
			String[] ints = input.nextLine().split(" ");
			//System.out.println(Arrays.deepToString(ints));
			int base1 = ints[1].length();
			int base2 = ints[2].length();
			Character[] system1 = new Character[base1];
			Character[] system2 = new Character[base2];
			
			for(int i = 0; i < base1; i++) {
				system1[i] = ints[1].charAt(i);
			}
			for(int i = 0; i < base2; i++) {
				system2[i] = ints[2].charAt(i);
			}
			//System.out.println("System1: " + (Arrays.deepToString(system1)));
			//System.out.println("System2: " + (Arrays.deepToString(system2)));
			int value = 0;

			for(int i = ints[0].length()-1, j = 0; i >= 0; i--, j++) {

				value += find(system1, ints[0].charAt(i)) * (Math.pow(base1, j));
				//System.out.println("place: " + find(system1, ints[0].charAt(i)));
			}
			//System.out.println("Value: " + value);
			String out = "";
			int places = (int) (Math.log(value) / Math.log(base2));
			for(int j = 0; value > 0; j++) {
				int currentplaceval = (int) ((value % Math.pow(base2, j+1)) / Math.pow(base2, j));
				//System.out.println("J: " + j + " val: " + value + " base: " + base2 + 
					//" currentplaceval: " + currentplaceval);
				out = Character.toString(system2[currentplaceval]) + out;
				value -= currentplaceval * Math.pow(base2, j);
				//TODO: convert first10 to new system with divide 
			}
			System.out.println("Case #" + currentcase + ": " + out);
			currentcase++;
		}
	}

	public static int find(Character[] arr, Character key) {
		for(int i = 0; i < arr.length; i++) {
			if(arr[i].equals(key))
				return i;
		}
		return -1;
	}

}