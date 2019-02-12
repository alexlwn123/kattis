from collections import OrderedDict
def main():
    n = int(input())
    teams = OrderedDict()
    for _ in range(n):
        if len(teams) == 12:
            break

        line = input().split()
        if line[0] not in teams:
            teams[line[0]] = line[1]
    for team in teams:
        print(team, teams[team])

if __name__ == '__main__':
    main()
