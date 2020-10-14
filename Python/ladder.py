import math
def main():
  h, v = map(int, input().split(' '))
  print(math.ceil(h / math.sin(v/180*math.pi)))

if __name__ == '__main__':
  main()
