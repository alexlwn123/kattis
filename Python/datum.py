def main():
    d, m = map(int, input().split())
    day = 2+d
    m -= 1
    while m > 0:
        if m in [1,3,5,7,8,10,12]:
            day += 31
        elif m in [4,6,9,11]:
            day += 30
        else:
            day += 28
        m -=1
    out = ""
    day %= 7
    if day == 0:
        print("Monday")
    if day == 1:
        print("Tuesday")
    if day == 2:
        print("Wednesday")
    if day == 3:
        print("Thursday")
    if day == 4:
        print("Friday")
    if day == 5:
        print("Saturday")
    if day == 6:
        print("Sunday")
if __name__ == '__main__':
    main()
