import java.util.Scanner;

public class qualy{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        double total = 0;
        
        for (int i = 0; i < n; i++) {
            double a = input.nextDouble();
            double b = input.nextDouble();
            total += a*b;
        }
        System.out.println(total);
    }
}
