import java.util.*;
public class I {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String in = input.nextLine();
		if(in.length() <= 2 ||
			in.replace(in.substring(0,1), "").length() == 0||
			in.replace(in.substring(1,2), "").length() == 0) {
			//in.replace(in.substring(0,1), "").replace(in.substring(0,1), "").length() == 0)
			
			System.out.println(0);
			return;
		}
		String temp = in.substring(0);
		

		int max1 = 0;
		String maxc1 = "";
		String maxc2 = "";
		int max2 = 0;

		while(temp.length() > 0) {

			String x = temp.substring(0,1);
			int num = temp.length() - temp.replace(x, "").length();
			
			if(num > max1) {
				max2 = max1;
				maxc2 = maxc1;
				max1 = num;
				maxc1 = x;
			}

			else if(num > max2) {
				max2 = num;
				maxc2 = x;
			}

			temp = temp.replace(x, "");
		}

		
		int count = in.replace(maxc1, "").replace(maxc2, "").length();

		
		System.out.println(count);

	

	}
}