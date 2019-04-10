def main():
  arr = [" ","1","2","3","4","5","6","7","8","9","0","-","=","W","E","R","T","Y","U","I","O","P","[","]","\\","S","D","F","G","H","J","K","L",";","\'","X","C","V","B","N","M",",",".","/"]
  arr1 = [" ","`","1","2","3","4","5","6","7","8","9","0","-","Q","W","E","R","T","Y","U","I","O","P","[","]","A","S","D","F","G","H","J","K","L",";","Z","X","C","V","B","N","M",",","."]
  translate = {arr[i]: arr1[i] for i in range(len(arr))}
  try:
    while True:
      line = list(input())
      out = []
      for x in line:
        out.append(translate[x])
      print("".join(out))
  except EOFError as Exception:
    pass
if __name__ == '__main__':
  main()
