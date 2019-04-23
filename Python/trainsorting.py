def main():
  n = int(input())
  trains = [int(input()) for _ in range(n)]
  inc, dec = [1] * n, [1] * n


  for i in range(n-1,-1,-1):
    for j in range(i+1,n):
      if trains[i] > trains[j]:
        dec[i] = max(dec[j]+1, dec[i])
      elif trains[i] < trains[j]:
        inc[i] = max(inc[j]+1, inc[i])

  ans = 0
  for i in range(n):
    binc, bdec = 0, 0
    for j in range(i+1, n):
      if trains[i] < trains[j]:
        binc = max(binc, inc[j])
      elif trains[i] > trains[j]:
        bdec = max(bdec, dec[j])

    ans = max(ans, 1+binc+bdec)

  print(ans)

if __name__ == '__main__':
  main()
