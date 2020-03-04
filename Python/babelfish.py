import sys
def main():
  lines = sys.stdin.read().splitlines()
  i = 0
  m = {}
  while True:
    line = lines[i].split()
    i+=1
    if len(line) < 2:
      break
    m[line[1]] = line[0]

  out = []
  for j in range(i, len(lines)):
    if lines[j] in m:
      out.append(m[lines[j]])
    else:
      out.append('eh')
  print('\n'.join(out))
    


    
    



if __name__ == '__main__':
  main()
