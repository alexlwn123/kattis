import java.util.*;
public class twostones {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int x = input.nextInt();
    System.out.println( x % 2 == 0 ?"Bob" : "Alice");
  }
}
