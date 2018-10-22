import java.util.*;
public class B {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int numt = input.nextInt();
		int numl = input.nextInt();
		input.nextLine();
		String[] arr1 = input.nextLine().split(" ");
		String[] arr2 = input.nextLine().split(" ");

		int[] tarr = new int[numt];
		int[] larr = new int[numl];



		for(int i = 0; i < numt; i++) {
			tarr[i] = Integer.parseInt(arr1[i]);
		}
		for(int i = 0; i < numl; i++) {
			larr[i] = Integer.parseInt(arr2[i]);
		}
		Arrays.sort(tarr);
		Arrays.sort(larr);

		//System.out.println("t: " + Arrays.toString(tarr) + "\nl: " + Arrays.toString(larr));
		int min = 0;
		int i = numt-1;
		int j = numl-1;
		int count = 0;
		while(i >= 0 && j >= 0) {
			if(tarr[i] <= larr[j]) {
				count++;
				i--;
				j--;
			}
			else
				i--;
		}

		System.out.println(count);
	}
}