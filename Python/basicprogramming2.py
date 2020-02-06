def main():
  n, t = map(int, input().split())
  arr = list(map(int, input().split()))
  if t == 1:
    S = set()
    for x in arr:
      S.add(7777 - x)
    for x in arr:
      if x in S:
        print('Yes')
        return

    print('No')
    return

  elif t == 2:
    S = set(arr)
    print('Unique' if len(set(arr)) == n else 'Contains duplicate')
    return


  elif t == 3:
    D = {}
    for x in arr:
      if x not in D:
        D[x] = 0
      D[x] += 1
    m,a = -1, -1
    for x,y in D.items():
      if y > n/2:
        print(x)
        return
    print(-1)
    return
      

  elif t == 4:
    arr.sort()
    if n%2==1:
      print(arr[n//2])
    else:
      print(arr[n//2-1],arr[n//2])
    return

  else:
    arr.sort()
    s,e = 0, 1
    while s < n and arr[s] < 100:
      s += 1
    while e < n+1 and arr[-e] > 999:
      e += 1
    if e == 1:
      print(' '.join(list(map(str, arr[s:]))))
    else:
      print(' '.join(list(map(str, arr[s:-e+1]))))

    
if __name__ == '__main__':
  main()
