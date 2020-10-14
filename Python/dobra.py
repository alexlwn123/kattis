good = 0
def check(SET, line, i):
  if i < len(line)-2 and sum([1 for x in line[i+1:i+3] if x in SET]) >= 2:
    #print(sum([1 for x in line[i+1:i+3] if x in SET]), "SUM1", SET)
    return False

  if i < len(line) - 1 and i > 0 and sum([1 for x in line[i-1:i+2] if x in SET]) >= 2:
    #print(sum([1 for x in line[i-1:i+2] if x in SET]), line, i, 'SUM2', SET)
    return False

  if i > 1 and sum([1 for x in line[i-2:i] if x in SET]) >= 2:
    #print(sum([1 for x in line[i-2:i] if x in SET]), 'SUM3', SET)
    return False
  
  return True

def generate(V, C, line, score):
  global good

  if '_' not in line: 
    if 'L' in line:
      good += score 
    return

  i = line.index('_')
    
  if check(C, line, i):
    line[i] = 'X'
    generate(V, C, line, score*(len(C)-1))
    line[i] = 'L'
    generate(V, C, line, score*1)
    line[i] = '_'
  
  if check(V, line, i):
    line[i] = 'A'
    generate(V, C, line, score*len(V))
    line[i] = '_'



def main():

  V = {"A", "E","I","O","U"}
  C = {chr(x) for x in range(65,91)} - V
  line = list(input())
  generate(V, C, line, 1)
  global good 
  print(good)

  
if __name__ == '__main__':
  main()
