import java.util.*;
public class addWords { 

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Map<String, Integer> codes = new HashMap<String, Integer>();
		Map<Integer, String> ans = new HashMap<Integer, String>();
		while(scanner.hasNextLine()) {
			boolean cleared = false;
			boolean unknown = false;
			String full = scanner.nextLine();

			String[] line = full.replace("  ", " ").split(" ");
			//System.out.println(Arrays.deepToString(line));
			if(line[0].equals("clear")) {
				codes.clear();
				ans.clear();
			}

			else if(line[0].equals("def")) {
				if(!codes.containsKey(line[1])) {
					codes.put(line[1], Integer.parseInt(line[2]));
					ans.put(Integer.parseInt(line[2]), line[1]);	
				}		
				else{
					ans.remove(codes.get(line[1]));
					ans.put(Integer.parseInt(line[2]), line[1]);
					codes.replace(line[1], Integer.parseInt(line[2]));
				}
			}
			
			
			else if(line[0].equals("calc")) {
				int val = 0;
				if(codes.containsKey(line[1]))
					val = codes.get(line[1]);
				else
					unknown = true;

				for(int i = 2; i < line.length; i += 2) {
				
					if(line[i].equals("=")) {
						break;
					}

					if(!codes.containsKey(line[i+1])) {
						unknown = true;
						//System.out.println("unknown: " + line[i+1]);
						break;
					}

					if(line[i].equals("+")) { 
						val += codes.get(line[i+1]);
						//System.out.println("+");
					}

					else if(line[i].equals("-")) {
						val -= codes.get(line[i+1]);
						//System.out.println("-");
					}

					
					//System.out.println("sum: " + val);

				}

				System.out.println(full.substring(4) + " " + 
					(unknown || !ans.containsKey(val) ? "unknown" : ans.get(val)));
			}

		}

	}
}