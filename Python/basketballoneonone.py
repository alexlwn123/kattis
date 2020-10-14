def main():
  x = {"A": 0, "B": 0}
  line = input()
  for i in range(0, len(line),2):
    x[line[i]] += int(line[i+1])
    if x["A"] >= 11 and x["A"] - x["B"] >= 2:
      print("A")
      return
    if x["B"] >= 11 and x["B"] - x["A"] >= 2:
      print("B")
      return


if __name__ == '__main__':
  main()
