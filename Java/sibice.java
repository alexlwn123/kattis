import java.util.*;
public class sibice {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    double diag = Math.hypot(input.nextDouble(),input.nextDouble());
    for (int i = 0; i < n; i++) {
      int x = input.nextInt();
      System.out.println((x > diag ? "NE" : "DA"));
    }
  }
}
