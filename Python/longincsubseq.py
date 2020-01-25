import sys

def main():
  out = []
  for line in sys.stdin:
    n = int(line)
    arr = list(map(int, sys.stdin.readline().strip().split()))
    ind = [0] * n
    dp = [0] * (n+1)
    length = 0

    for i in range(n):
      lo, hi = 1, length 
      while lo <= hi:
        mid = (lo+hi)//2
        if (arr[dp[mid]] < arr[i]):
          lo = mid+1
        else:
          hi = mid-1

      newlen = lo
      ind[i] = dp[newlen-1]
      dp[newlen] = i

      if (newlen > length):
        length = newlen
    
    case, j = [], dp[length]

    
    for i in range(length-1, -1, -1):
      case.append(j)
      j = ind[j]
    

    out.append(str(length))
    out.append(' '.join(list(map(str, case[::-1]))))


  sys.stdout.write('\n'.join(out))
        

if __name__ == '__main__':
  main()
