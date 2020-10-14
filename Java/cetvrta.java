import java.util.*;
public class cetvrta {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int[] x = new int[3];
    int[] y = new int[3];

    for (int i = 0; i < 3; i++) {
      x[i] = input.nextInt();
      y[i] = input.nextInt();
    }

    Arrays.sort(x);
    Arrays.sort(y);

    System.out.print(x[0] == x[1] ? x[2] : x[0]);
    System.out.print(' ');
    System.out.print(y[0] == y[1] ? y[2] : y[0]);

  }
}
