import sys
def main():
    size = int(input())
    runners = []

    for i in range(size):
        line = sys.stdin.readline().split()
        line[1], line[2] = float(line[1]), float(line[2])
        runners.append(line)

    runners.sort(key=lambda p: (p[2]))

    mintime = 9999999
    minteam = []

    for r in runners:
        team = []
        team.append(r)
        time = r[1]
        for r2 in runners:
            if r2 == r:
                continue
            team.append(r2)
            time += r2[2]
            if len(team) >= 4:
                break
        if time < mintime:
            mintime = time
            minteam = team

    print('{0:.9g}'.format(mintime))
    print(minteam[0][0])
    print(minteam[1][0])
    print(minteam[2][0])
    print(minteam[3][0])



if __name__ == '__main__':
    main()
