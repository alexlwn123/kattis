n = int(input())
print(sum(sorted(list(map(int, input().split())))[-3::-3]))
