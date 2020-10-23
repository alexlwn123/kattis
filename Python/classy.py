def main():
  keys = {"upper": 2, "middle": 1, "lower": 0}
  T = int(input())
  for _ in range(T):
    n = int(input())
    people = []
    for _ in range(n):
      line = input().split()
      arr = list(map(lambda x: keys[x], line[1].split('-')))
      total = 0
      arr = [1] * (10 - len(arr)) + arr
      for i in range(10):
        total += 3 ** i * arr[i]
      people.append((line[0][:-1], total))

    people.sort(key = lambda x: (-x[1], x[0]))

    print('\n'.join([x[0] for x in people]))

    print('=' * 30)

  

    





if __name__ == '__main__':
  main()
