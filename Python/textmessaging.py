def main():
  N = int(input())
  for i in range(N):
    P, K, L = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)
    p, k, s = 1, 1, 0
    for x in arr:
      s += x * p
      if k == K:
        k=1
        p+=1
      else:
        k+=1
        
    print(f'Case #{i+1}: {s}')






if __name__ == '__main__':
  main()
