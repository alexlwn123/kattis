    import sys
def main():
    lines = sys.stdin.read().splitlines()

    n = int(lines[0])
    
    for i in range(n):
        line = lines[i+1].split(' ')
        
        sum = int(line[0])
        diff = int(line[1])

        score1 = (sum + diff) // 2
        score2 = (sum - diff) // 2

        if score1 < 0 or score2 < 0 or score1 == 1 or score2 == 1 or sum - diff == 1 or sum % 2 != diff % 2:
            print('impossible')
        else:
            print(str(score1) + " " + str(score2))



if __name__ == '__main__':
    main()
