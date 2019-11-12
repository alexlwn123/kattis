from itertools import combinations
def find(arr):
  sour, bitt = 1, 0
  for s, b in arr:
    sour *= s
    bitt += b
  return abs(sour-bitt)

def main():
  n = int(input())
  foods = []
  for _ in range(n):
    foods.append(list(map(int, input().split(' '))))

  minimum = 99999999999
  for i in range(1, n+1):
    combos = combinations(foods, i)
    for arr in combos:
      minimum = min(minimum, find(arr))

  print(minimum)


if __name__ == '__main__':
  main()
