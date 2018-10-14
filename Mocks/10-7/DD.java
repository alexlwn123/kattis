import java.util.*;
public class DD {

	public static void main(String[] args) {
		int lr = 0;
		int ud = 0;
		int lbound = 0;
		int rbound = 0;
		int ubound = 0;
		int dbound = 0;

		ArrayList<Character> instructions = new ArrayList<>();


		Scanner input = new Scanner(System.in);

		while(input.hasNextLine()) {
			String line = input.nextLine();

			if(line.equals("left")){
				lr--;
				instructions.add('l');
				if(lr<lbound)
					lbound = lr;
			}
			if(line.equals("right")) {
				lr++;
				instructions.add('r');
				if(lr>rbound)
					rbound = lr;
			}
			if(line.equals("down")){
				ud--;
				instructions.add('d');
				if(ud < dbound)
					dbound = ud;
			}
			if(line.equals("up")) {
				ud++;
				instructions.add('u');
				if(ud > ubound)
					ubound = ud;
			}	

		}

		int totalx = rbound - lbound + 2;
		int totaly = ubound - dbound + 2;

		int startx = 0 - lbound + 1;
		int starty = 0 - dbound + 1;

		int endx = startx + ud;
		int endy = starty + lr;

		String[][] board = new String[totalx][totaly];

		for(int i = 0; i < totaly; i++){
			for(int j = 0; i < totalx; j++){
				if(i == 0 || i == totaly-1 || j == 0 || j == totalx-1) {
					board[i][j] = "#";
				}
				else
					board[i][j] = " ";
			}
		}

		int tempx = startx;
		int tempy = starty;

		board[startx][starty] = "S";
		board[endx][endy] = "E";

		for(Character inst: instructions) {
			if(inst == 'r')
				tempx++;
			if(inst == 'l')
				tempx--;
			if(inst == 'u')
				tempy++;
			if(inst == 'd')
				tempy--;

			if(board[tempx][tempy] != "S" && board[tempx][tempy] != "E")
				board[tempx][tempy] = "*";
		}

		for(int i = 0; i < totaly; i++){
			for(int j = 0; i < totalx; j++){
				System.out.print(board[i][j]);
			}
			System.out.print("\n");
		}






	}
}