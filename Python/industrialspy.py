from sys import stdin
from itertools import permutations, combinations
def getPrimes(n):
  n, correction = n-n%6+6, 2-(n%6>1)
  sieve = [True] * (n//3)
  for i in range(1,int(n**0.5)//3+1):
    if sieve[i]:
      k=3*i+1|1
      sieve[k*k//3::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
      sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
  return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

def main():
  primes = set(getPrimes(9999999))

  n = int(stdin.readline().strip())
  for _ in range(n):
    line = stdin.readline().strip()
    nums = set([int(x) for x in line])
    for i in range(2, len(line)+1):
      for num in set(combinations(line, i)):
        nums = nums.union(set([int("".join(x)) for x in permutations(num)]))

    count = sum([1 if p in primes else 0 for p in nums])
    print(count)

if __name__ == '__main__':
  main()
