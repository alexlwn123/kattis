import sys
def primesx(n):
  sieve = [True] * n
  for i in range(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
  return [2] + [i for i in range(3,n,2) if sieve[i]]

def main():
  N = int(sys.stdin.readline().strip())
  primes = set(primesx(10000))
  out = []
  i = 0
  lines = sys.stdin.read().splitlines()
  for i in range(1, N+1):
    q, p = map(int, lines[i-1].split())
    if p not in primes:
      out.append(f'{i} {p} NO')
      continue

    x = p
    seen = set()
    while True:
      if x in seen:
        out.append(f'{i} {p} NO')
        break
      if x == 1:
        out.append(f'{i} {p} YES')
        break
      seen.add(x)

      x = sum([a**2 for a in list(map(int, list(str(x))))])

  print('\n'.join(out))



if __name__ == '__main__':
  main()
