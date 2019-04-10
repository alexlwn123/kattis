def main():
  n = int(input())
  for _ in range(n):
    line = input()
    if line[:10] == "Simon says":
      print(line[11:])
if __name__ == '__main__':
  main()
