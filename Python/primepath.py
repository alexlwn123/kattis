def isPrime(n):
  for i in range(2, 1 + int(n ** 1/2)):
    if n % i == 0:
      return False
  return True

def main():
  n = int(input())
  digits = [1,2,3,4,5,6,7,8,9,0]
  for _ in range(n):
    start, finish = map(int, input().split())
    tree = {start:start}
    q = [start]
    done = False
    while q:
      curr = q.pop(0)
      if curr == finish:
        count = 0
        while tree[curr] != curr:
          curr = tree[curr]
          count += 1
        print(count)
        done = True
        break
      for i in range(4):
        for j in range(10):
          dx = 10 ** i
          digit = curr // dx
          digit = digit % 10
          dx *= j-digit

          temp = dx + curr
          if temp != curr and isPrime(temp) and temp not in tree:
            tree[temp] = curr
            q.append(temp)
    if done:
      print("Impossible")


if __name__ == '__main__':
  main()
