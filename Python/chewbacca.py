import sys

def find_layer(x, K):
  layer = 0
  while x >= 0:
    x -= K ** layer
    layer += 1

  return [layer-1, x + K**(layer-1)]

def main():
  N, K, Q = map(int, sys.stdin.readline().split())
  out = []
  for line in sys.stdin.readlines():    
    u, v = map(int, line.split())
    u_layer, u_off,= find_layer(u-1, K)
    v_layer, v_off = find_layer(v-1, K)

    dist = 0

    while (u_off != v_off or v_layer != u_layer):
      dist += 1
      if u_layer >= v_layer:
        u_layer -= 1 
        u_off //= K
      else:
        v_layer -= 1
        v_off //= K
      
    out.append(str(dist))

  print('\n'.join(out))

if __name__ == '__main__':
  main()
