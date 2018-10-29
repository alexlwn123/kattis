import math
line = input().split(' ')
out = ''
if line[2] == '1':
    if int(line[1]) > 14:
        out = 'TLE'
    else:
        out = 'TLE' if math.factorial(int(line[1])) > int(line[0]) else 'AC'
if line[2] == '2':
    out = 'TLE' if math.pow(2, int(line[1])) > int(line[0]) else 'AC'
if line[2] == '3':
    out = 'TLE' if math.pow(int(line[1]),4) > int(line[0]) else 'AC'
if line[2] == '4':
    out = 'TLE' if math.pow(int(line[1]),3) > int(line[0])  else 'AC'
if line[2] == '5':
    out = 'TLE' if math.pow(int(line[1]),2) > int(line[0]) else 'AC'
if line[2] == '6':
    out = 'TLE' if math.log(int(line[1]),2) * int(line[1]) > int(line[0]) else 'AC'
if line[2] == '7':
    out = 'TLE' if int(line[1]) > int(line[0]) else 'AC'
print(out)
