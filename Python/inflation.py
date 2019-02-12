def main():
    n = int(input())
    cans = list(map(int, input().split()))
    cans.sort()
    smallest =1
    for i in range(1, n+1):
        j = cans[i-1]
        if j > i:
            print("impossible")
            return
        smallest = min(smallest, j/i)

    print(smallest)


if __name__ == '__main__':
    main()
