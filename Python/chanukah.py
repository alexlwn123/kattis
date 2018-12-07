def main():
    ans = [0]
    for i in range(1, 20000):
        ans.append(ans[-1] + i)

    n = int(input())
    for i in range(1, n+1):
        x = int(input().split(' ')[1])
        print(str(i) + " " + str(ans[x+1]-1))
if __name__ == '__main__':
    main()
