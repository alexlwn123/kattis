import math
def main():
  n = int(input())
  for _ in range(n):
    v, t, x, h1, h2 = map(float, input().split())
    t = t /180 * math.pi
    vx = math.cos(t) * v
    T = x / vx 

    y = v*T*math.sin(t) - 0.5*9.81*T*T
    print('Safe' if y >= h1+1 and y <= h2 - 1 else 'Not Safe')



if __name__ == '__main__':
  main()
