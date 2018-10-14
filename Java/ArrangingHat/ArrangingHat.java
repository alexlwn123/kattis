import java.util.*;
public class ArrangingHat {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int nums = input.nextInt();
		int places = input.nextInt();
		int currentplace = 0;
		int val = 0;
		String x = "";
		String y = input.next();
		
		while(input.hasNext()) {
			x = y;
			y = input.next();


			if(x.equals(y) || y.compareTo(x) > 0){
				System.out.println(x);
			}

			else if(x.charAt(0) == y.charAt(0)) {
				int temp = 0;
				while(x.charAt(temp) == y.charAt(temp)) {
					temp++; 
				}
				y = change(x,y,temp);
			}

			else if(x.charAt(currentplace) > y.charAt(currentplace)) {
				if(x.charAt(currentplace)  > val) {
					x = x.substring(0, currentplace) + val + x.substring(currentplace +1);
				}
				else if(y.charAt(0) != 9) {
					val = y.charAt(0) + 1;
					x = val + x.substring(1);
				}
				y = change(x,y,0);
			}
			//System.out.println(x);
		}

	}
	public static String change(String x, String y, int i) {
		System.out.println("change");
		if(x.charAt(i) != 0) {
			int temp = Integer.parseInt(Character.toString(x.charAt(i))) - 1;
			x = x.substring(0,i) + String.valueOf(temp) + x.substring(i + 1);
			System.out.println(x);
			return y;
		}
		else {
			int temp = Integer.parseInt(Character.toString(y.charAt(i))) + 1;
			y = y.substring(0,i) + String.valueOf(temp) + y.substring(i + 1);
			System.out.println(x);
			return y;
		}
	}
}