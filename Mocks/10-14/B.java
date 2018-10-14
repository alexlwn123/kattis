import java.util.*;
public class B {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		double slices = input.nextInt();
		double rings = input.nextInt();
		double radius = input.nextDouble();

		double ang1 = input.nextInt();
		double len1 = input.nextInt();
		double ang2 = input.nextInt();
		double len2 = input.nextInt();

	//	System.out.println("slices: " + slices + " rings: " + rings + " rad: " + radius);
	//	System.out.println("Point1: " + ang1 +" " + len1 + " " + "Point2: " + ang2 + " " + len2);

		double totalDist = 0;

		double moveRings = Math.abs(len1 - len2) / rings * radius;

		double around = Math.PI * (Math.abs(ang1 - ang2) / slices) * (Math.min(len1, len2) / rings * radius);

		
		totalDist = moveRings + around;
		
		System.out.println(Math.min(totalDist, (len1 + len2)/ rings * radius));


	} 
}