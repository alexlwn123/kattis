import java.util.*;
public class Books {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		List<Integer> books = new ArrayList<Integer>();
		while(input.hasNextInt()) {
			books.add(input.nextInt());
		}
		Collections.sort(books);
		int cost = 0;
		for(int i = books.size()-1 , j = 1; i >= 0; i--, j++) {
			if(j % 3 != 0) 
				cost += books.get(i);
		}

		System.out.println(cost);
	}
}