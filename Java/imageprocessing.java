import java.util.*;
public class imageprocessing {
   public static void main(String[] args) {

     Scanner input = new Scanner(System.in);
     int H = input.nextInt();
     int W = input.nextInt();
     int N = input.nextInt();
     int M = input.nextInt();

     int[][] before = new int[H][W];
     for (int i = 0; i < H; i++) { 
       for (int j = 0; j < W; j++) {
         before[i][j] = input.nextInt();
       }
     }
     int[][] ker = new int[N][M];
     for (int i = N-1; i >= 0; i--) { 
       for (int j = M-1; j >= 0; j--) {
         ker[i][j] = input.nextInt();
       }
     }
     int[][] after = new int[H-N+1][W-M+1];
     for (int j = 0; j < after.length; j++) { 
       for (int i = 0; i < after[0].length; i++) {
         for (int k = 0; k < N; k++) {
           for (int l = 0; l < M; l++) {
             after[i][j] += ker[k][l] * before[i+k][j+l];
           }
         }
       }
     }

     for (int[] arr: after) {
        for (int i = 0; i < arr.length; i++) {
          System.out.print(arr[i]);
          System.out.print(" ");
        }
        System.out.println();
     }
     

    




    }


}
