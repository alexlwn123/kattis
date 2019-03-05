def main():
  arr = []
  counts = set()
  out = []
  try:
    while True:
      line = input().split()
      temp = []
      for word in line:
        tempa = word.lower()
        if tempa not in counts:
          temp.append(word)
          counts.add(tempa)
        else:
          temp.append('.')
      out.append(" ".join(temp))


  except EOFError as Exception:
    pass


  print("\n".join(out))


if __name__ == '__main__':
  main()
