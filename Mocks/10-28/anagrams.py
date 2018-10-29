import sys
import math

def main():

    lines = sys.stdin.read().splitlines() 

    for line in lines:
        charlist = {}
        for character in line:

            if character not in charlist:
                charlist[character] = 1

            else:
                charlist[character] += 1

        count = math.factorial(len(line))

        for key in charlist:
            count //= math.factorial(charlist[key])
                
        print("%d" % count)

if __name__ == '__main__':
    main()
