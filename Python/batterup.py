n = input()
y = [x for x in list(map(int, input().split())) if x > -1]
print(sum(y) /len(y)) 
