import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
public class secretchamber {
  public static boolean same(char a, char b, ArrayList<Character> seen, Map<Character, ArrayList<Character>> letters) {
    if (a == b) 
      return true;
    
    seen.add(a);
    if (!letters.containsKey(a)) {
      return false;
    } 

    for (char x: letters.get(a)) {
      if(!seen.contains(x) && same(x, b, seen, letters))
        return true; 
    } 
    return false;
    
  }
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int m, n;
    m = input.nextInt();
    n = input.nextInt();
    Map<Character, ArrayList<Character>> letters = new HashMap<>();

    for (int i = 0; i < m; i++) {
      char u = input.next().charAt(0);
      char v = input.next().charAt(0);
      if (letters.containsKey(u)) {
        letters.get(u).add(v);
      }
      else {
        letters.put(u, new ArrayList<Character>());
        letters.get(u).add(v);
      }    
    }

    for (int i = 0; i < n; i++) {
      String first = input.next();
      String second = input.next();
      
      if (first.length() != second.length()) {
        System.out.println("no");
        continue;
      }
      boolean good = true;
      for (int j = 0; j < first.length(); j++) {
        if (!same(first.charAt(j), second.charAt(j), new ArrayList<>(), letters)) {
          good = false;
          break;
        } 
      }
      System.out.println(good ? "yes" : "no");
    
    }
  }
}

