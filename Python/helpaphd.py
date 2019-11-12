n = int(input())
for _ in range(n):
  line = input()
  if line[0]=='P':
    print('skipped')
  else:
    print(eval(line))
