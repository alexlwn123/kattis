def main():
  line = input().split(';')
  total = 0 
  for word in line:
    x = word.split('-')
    if len(x) > 1:
      total += int(x[1]) - int(x[0]) + 1
    else:
      total += 1

  print(total)



if __name__ == '__main__':
  main()
