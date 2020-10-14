def main():
  n, m = map(int, input().split())
  first, second = input(),input()
  bfirst, bsecond = first[::-1], second[::-1]
  bfirst = [ord(x)-97 for x in bfirst]
  bsecond = [ord(x)-97 for x in bsecond]
  key = bfirst

  for i in range(m-n):
    key.append((bsecond[i]-key[i]+26)%26)
  

  print(''.join([chr(x+97) for x in key[::-1]]))
   
  



  


if __name__ == '__main__':
  main()
