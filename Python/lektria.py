construct = lambda s, i, j: s[:i][::-1]+s[i:j][::-1]+s[j:][::-1]

s = input()
best = ""
for i in range(1,len(s)-1):
	for j in range(i+1,len(s)):
		output = construct(s, i, j)
		if best == "":
                    best = output
		if output < best:
			best = output

print(best)
