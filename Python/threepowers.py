import sys
def main():
  lines = list(map(int, sys.stdin.read().splitlines()))[:-1]
  for n in lines:
    line = list(bin(n-1))[2:]
    s = [] 
    for i in range(len(line)):
      if line[-(i+1)] == '1':
        s.append(3**(i))

    if not s:
      print('{ }')
      continue
    out = ['{ ', ", ".join(list(map(str, s))), ' }']
    print(''.join(out))







if __name__ == '__main__':
  main()
