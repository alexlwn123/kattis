import java.util.*;
public class Queens {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		boolean[][] board = new boolean[8][8];
		int count = 0;
		for(int i = 0; i < 8; i++) {
			String line = input.nextLine(); 
			boolean yes = false;
			for(int j = 0; j < 8; j++) 
				if(line.charAt(j) == '*'){
					count++;
					if(yes) {
						System.out.println("invalid");
						return;
					}
					board[i][j] = true;
					yes = true;
				}
		}
		//System.out.println(count);
		if(count != 8) {
			System.out.println("invalid");
			return;
		}
		//collumns
		for(int i = 0; i < 8; i++) {
			boolean yes = false;
			for(int j = 0; j < 8; j++) {
				if(board[j][i]) {
					if(yes) {
						System.out.println("invalid");
						return;
					}
					yes = true;
				}
			}
		}

		//diags downright

		for(int i = 0; i < 8; i++) {  //top
			boolean yes1 = false;
			boolean yes2 = false;
			for(int j = 0; i + j < 8; j++) {
				if(board[i+j][j]) {
					if(yes1) {
						System.out.println("invalid");
						return;
					}
					yes1 = true;
				}
				if(board[j][i+j]) {
					if(yes2) {
						System.out.println("invalid");
						return;
					}
					yes2 = true;
				}
			}
		}
		//diags upright
		for(int i = 0; i < 8; i++) {  
			boolean yes1 = false;
			
			for(int j = 0; i-j >= 0; j++) {
				if(board[i-j][j]) {
					if(yes1) {
						System.out.println("invalid");
						return;
					}
					yes1 = true;
				}
				
			}
		}
		//diags upright
		for(int i = 0; i < 8; i++) {  
			boolean yes1 = false;
		
			for(int j = 0; j+i < 8; j++) {
				if(board[7-j][i+j]) {
					if(yes1) {
						System.out.println("invalid");
						return;
					}
					yes1 = true;
				}
				
			}
		}

		
		System.out.println("valid");
	}
}