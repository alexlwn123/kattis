def main():
  n = int(input())
  x, y, z = 0, 1, 0
  for _ in range(n-1):
    temp = y 
    y += x
    x = temp

  print(x, y)

    
    
     
    


if __name__ == '__main__':
  main()
