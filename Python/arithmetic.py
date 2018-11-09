line = raw_input()

out = hex(int(line,8))[2:].upper()

if out[-1]=='L':
	out=out[:-1]
print(out)
