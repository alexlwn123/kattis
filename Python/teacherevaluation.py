def main():
  n, p = map(int, input().split(' '))
  grades = list(map(int, input().split(' ')))
  count = 0
  while p > sum(grades) // len(grades):
    if count >= 200:
      print('impossible')
      break
    count += 1
    grades.append(100)
  else:
    print(count)



if __name__ == '__main__':
  main()
