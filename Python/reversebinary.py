line = input()
line = bin(int(line))
line = str(line)[::-1][:-2]
line = int(line, 2)
print(line)
