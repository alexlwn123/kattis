def main():
  M = int(input())

  counts = {}
  sets = []
  lines = []
  for _ in range(M):
    lines.append(input().split())
    for x in lines[-1]:
      if x not in counts:
        counts[x] = 0
      counts[x] += 1
    sets.append(set(lines[-1]))


  done = set(sets[0])
  print(sets)

  for s in sets:
    done = done.intersection(s)
    print(done)



  print('\n'.join(done))
    




if __name__ == '__main__':
  main()
