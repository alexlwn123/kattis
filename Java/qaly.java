import java.util.*;

public class qaly{
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int x = (int) input.nextInt();
    double sum = 0;
    for (int i = 0; i < x; i++) {
      sum += input.nextDouble()*input.nextDouble();
    }

    System.out.println(sum);
  }
}
