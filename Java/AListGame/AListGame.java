import java.util.*;
public class AListGame {
	public static void main(String[] args) {
		fillSieve();
		Scanner input = new Scanner(System.in);
		int x = input.nextInt();
		int n = x;
		int score = 0;

		for(int i = 2; i <= (x+1); i++) {
			if(i > (n/i) + 3){
				score++;
				break;
			}	
			if(isPrime(i))
				while(x % i == 0) {
					score++;
					x /= i;
				}
		}
		System.out.println(score);

	}
	
	public static boolean[] primes = new boolean[10000000]; 
	
	public static void fillSieve() {
	    Arrays.fill(primes, true);       
	    primes[0] = primes[1] = false;      
	    for (int i = 2; i < primes.length; i++) {
	    
	        if(primes[i]) {
	            for (int j = 2; i * j < primes.length; j++) {
	                primes[i * j] = false;
	            }
	        }
	    }
	}

	public static boolean isPrime(int n) {
		if(n < primes.length)
	    	return primes[n]; 
		
		return true;
	}	
}