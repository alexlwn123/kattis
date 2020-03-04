def main():
  n = int(input())
  arr = sorted(list(map(int, input().split())), reverse=True)

  print(sum(arr[2::3]))

if __name__ == '__main__':
  main()
