def main():
    cases = int(input())
    for _ in range(cases):
        numCities, numPilots = map(int, input().split())
        print(numCities-1)

        for _ in range(numPilots):
            input()

if __name__ == '__main__':
    main()
