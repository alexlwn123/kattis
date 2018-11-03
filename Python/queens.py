import sys
def main():
    width = int(input())
    x = []
    y = []
    diag = []
    diag2 = []
    for i in range(width): #Checks rows and cols and both diag
        line = sys.stdin.readline().strip()
        point = tuple(map(int, line.split()))
        if point[0] in x or point[1] in y or point[1]-point[0] in diag or point[1] + point[0] in diag2:
            # col           row             diag1                           diag2
            print('INCORRECT')
            return
        x.append(point[0])
        y.append(point[1])
        diag.append(point[1]-point[0])
        diag2.append(point[1]+point[0])
    print('CORRECT')

if __name__ == '__main__':
    main()

