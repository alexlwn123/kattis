import math
def main():
  n, k = map(int,input().split())
  a = math.log(n, 2)
  print("Your wish is granted!" if a <= k else "You will become a flying monkey!")
    

if __name__ == '__main__':
  main()
