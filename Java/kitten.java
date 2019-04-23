import java.util.*;
import java.util.Arrays.*;
import java.util.stream.*;
public class kitten {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int k = Integer.parseInt(input.nextLine());
    String line = input.nextLine();
    Map<Integer, Integer> map = new HashMap<>();
    while (!line.equals("-1")) {
      int[] ints = 
        Stream.of(line.split(" "))
        .map(Integer::parseInt)
        .mapToInt(i->i)
        .toArray();
      int head = ints[0];
      for(int i = 1; i < ints.length;i++) {
        map.put(ints[i], head);
      }
      line = input.nextLine();
    }
    System.out.print(k+" ");
    do {k = map.get(k); System.out.print(k+" ");} while(map.containsKey(k));

  }
}
