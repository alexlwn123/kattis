import java.util.*;
public class bookingaroom {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int r = input.nextInt(), n = input.nextInt();
    if (r == n) {
      System.out.println("too late");
      return;
    }
    boolean[] rooms = new boolean[r];
    
    for (int i = 0; i < n; i++) {
      rooms[input.nextInt() - 1] = true;
    }
    int x = 0;
    while(rooms[x] && x < rooms.length) x++; 

    System.out.println(x+1);
       

  }
}
