import java.util.*;
public class towering {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    
    int[] line = Arrays.stream(input.nextLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
    int sum1 = line[6], sum2 = line[7];
    
    int h1 = 0, h2 = 0;
    for (int i = 0; i < 6; i++) {
      for (int j = 0; j < 6; j++) {
        if (i == j) continue;
        for (int k = 0; k < 6; k++) {
          if (i == k || j == k)
            continue;
          int[] first = {line[i], line[j], line[k]};
          int[] second = new int[3];
          int x = 0;
          for (int q = 0; q < 6; q++) {
            if (i == q || j == q || k == q){
              continue;
            }
            second[x] = line[q];
            x++;
          }
          int sumx = Arrays.stream(first).sum();
          int sumy = Arrays.stream(second).sum();
          first = Arrays.stream(first).map(a -> -a).toArray();
          Arrays.sort(first);
          first = Arrays.stream(first).map(a -> -a).toArray();
          second = Arrays.stream(second).map(a -> -a).toArray();
          Arrays.sort(second);
          second = Arrays.stream(second).map(a -> -a).toArray();
          if (sumx == sum1 || sumx == sum2)   { 
            if (first[0] > second[0]) {
              String out = Arrays.toString(first) + " " + Arrays.toString(second);
              out = out.replace("]", "");
              out = out.replace("[", "");
              out = out.replace(",", "");
              System.out.println(out);
              return; 
            } else {
              String out = Arrays.toString(second) + " " + Arrays.toString(first);
              out = out.replace("]", "");
              out = out.replace("[", "");
              out = out.replace(",", "");
              System.out.println(out);
              return;
            }
          }
        }  
      } 
    } 
  }
}
