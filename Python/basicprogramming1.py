from itertools import islice
def main():
  N, T = map(int, input().split())
  arr = list(map(int, input().split()))
  if T == 1:
    print(7)
  elif T == 2:
    a, b = arr[0], arr[1]
    if a > b:
      print('Bigger')
    elif a == b:
      print('Equal')
    else:
      print('Smaller')
  elif T == 3:
    print(sorted(arr[:3])[1])
  elif T == 4:
    print(sum(arr))
  elif T == 5:
    print(sum(x for x in arr if x % 2 == 0))
  elif T == 6:
    print("".join(chr(x % 26 + 97) for x in arr))
  elif T == 7:
    visited, i = set(), 0
    while True:
      if i >= N:
        print("Out")
        return
      if i in visited:
        print('Cyclic')
        return
      if i == N-1:
        print("Done")
        return
      visited.add(i)
      i = arr[i]

if __name__ == '__main__':
  main()
