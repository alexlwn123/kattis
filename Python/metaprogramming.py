import sys
def main():
  lines = sys.stdin.read().splitlines()
  words = {}
  out = []
  for line in lines:
    line = line.split()
    if line[0] == 'define':
      words[line[2]] = int(line[1])
    elif line[0] == 'eval':
      if line[1] not in words or line[3] not in words:
        out.append('undefined')
      elif line[2] == '=':
        out.append('false' if words[line[1]] != words[line[3]] else 'true')
      elif line[2] == '>':
        out.append('false' if words[line[1]] <= words[line[3]] else 'true')
      elif line[2] == '<':
        out.append('false' if words[line[1]] >= words[line[3]] else 'true')

  print('\n'.join(out))

        



if __name__ == '__main__':
  main()
