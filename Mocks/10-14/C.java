import java.util.*;
public class C {
	public static void main (String[] args) {
		Scanner input = new Scanner(System.in);
	       	int cases = Integer.parseInt(input.nextLine());
	
		for(int i = 0; i < cases; i++) {
			ArrayList<Point> points = new ArrayList<>();
			String[] line = input.nextLine().split(" ");
			for(int j = 1; j < line.length-1; j+=2) {
				points.add(new Point(Integer.parseInt(line[j]),Integer.parseInt(line[j+1])));
			}
			for(Point p: points) {
				//System.out.println("P: " + p);
			}
			System.out.println(Math.abs(area(points)));
		}
	}

	public static double area(ArrayList<Point> points) {
		points.add(points.get(0));
		int sum1 = 0;
		int sum2 = 0;
		for(int i = 0; i < points.size()-1; i++) {
			sum1 += points.get(i).x * points.get(i+1).y;
			sum2 += points.get(i).y * points.get(i+1).x;
			//System.out.println(sum1 + " " + sum2);
		}
		//System.out.println(sum1 + " " + sum2);
		return 0.5 * (sum1 - sum2);
	}
	public static class Point{

		public int x;
		public int y;

		Point(int x, int y) {

			this.x = x;
			this.y = y;
			
		}
		public String toString() {
			return x + " " + y;
		}
		

	}
}
