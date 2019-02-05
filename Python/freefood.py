def main():
    n = int(input())
    calender = [False for _ in range(0, 366)]

    for _ in range(n):
        x,y = map(int, input().split())
        for z in range(x,y+1):
            calender[z] = True
    total = 0
    for day in calender:
        total += (1 if day else 0)

    print(total)



if __name__ == '__main__':
    main()
