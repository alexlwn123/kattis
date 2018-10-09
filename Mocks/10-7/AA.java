import java.util.*;
public class AA{
   
   public static void main(String[] args){
      Scanner input = new Scanner(System.in);
      
      int stopsn = Integer.parseInt(input.nextLine());
      List<Integer> stops = new ArrayList<Integer>();
      while(input.hasNextInt()) {
         stops.add(input.nextInt());
      }
      Collections.sort(stops);
      //System.out.println(stops.toString());
      
      for(int i = 0; i < stops.size(); i++) {
         //System.out.println("y");
         if(i == stops.size() - 1) {
            System.out.print(" " + stops.get(i));
            return;
         }
         if(stops.get(i) != stops.get(i+1)-1) {
            if(i != 0)
               System.out.print(" ");
            System.out.print(stops.get(i));
         }
         else {
            int j = i+1;
            while(j < stops.size()-1 && stops.get(j+1) == stops.get(j)+1)
               j++;
            if(i != 0)
               System.out.print(" ");
            if(j - i > 1)
               System.out.print(stops.get(i) + "-" + stops.get(j));
            else
               System.out.print(stops.get(i) + " " + stops.get(j));

            i = j;
         }
      }
      
   }
}
