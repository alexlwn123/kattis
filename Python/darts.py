import sys
import math
def main():
    lines = sys.stdin.read().splitlines()
    cases = int(lines[0])
    currentline = 1
    for i in range(cases):
        points = 0
        darts = int(lines[currentline])
        currentline += 1
        thisgame = lines[currentline:currentline + darts]
        for line in thisgame:
            currentline += 1
            dart = line.split()
            x = float(dart[0])
            y = float(dart[1])
            dist = math.hypot(x,y) 
            if dist < 220:
                points += 10 - int((dist-.00000001) / 20)
        print(str(points))

        


if __name__ == '__main__':
    main()
