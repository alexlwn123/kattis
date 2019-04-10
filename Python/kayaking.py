def dec(mat, bne):
  for s in mat:
    if 'b' == s:
      bne[0] -= 1
    if 'n' == s:
      bne[1] -= 1
    if 'e' == s:
      bne[2] -= 1

def ok(s, bne):
  tbne = bne[:]
  dec(s, tbne);
  return tbne[0] >=0 and tbne[1] >= 0 and tbne[2] >= 0

def works(b, n, e, speeds, boats, speed):
  bne = [b, n, e]
  yes = True
  for factor in boats:
    tyes = False
    for match in speeds:
      if factor * match[0] >= speed and ok(match[1], bne):
        dec(match[1], bne)
        tyes = True
        break

    if not tyes:
      yes = False
      break

  return yes

def main():
  b, n, e = map(int, raw_input().split())
  sb, sn, se = map(int, raw_input().split())
  boats = sorted(list(map(int, raw_input().split())))[::-1]

  speeds = sorted([
      (sb+sb, 'bb'),
      (sb+sn, 'bn'),
      (sb+se, 'be'),
      (sn+sn, 'nn'),
      (sn+se, 'ne'),
      (se+se, 'ee')
      ])

  low, high = 0, boats[0] * se * 2 + 10

  while high - low > 1:
    mid = (high+low) // 2
    if works(b, n, e, speeds, boats, mid):
      low = mid
    else:
      high = mid

  print low

if __name__ == '__main__':
  main()
