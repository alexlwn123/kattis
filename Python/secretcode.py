line = input()
while line != '0':
    key = [int(x) for x in line.split(' ')]
    keylen = key[0]
    key = key[1:]
    line = input()
    sections = [line[i*keylen:(i+1)*keylen] for i in range(len(line) // keylen)]
    sections.append(line[(len(line) // keylen) * keylen:])

    if len(sections[-1]) == 0:
        del sections[-1]
    else:
        sections[-1] = sections[-1].ljust(keylen)

    sections = [list(section) for section in sections]
    out = [[] for i in range(len(sections))]
    for i in range(len(out)):
        for j in key:
            out[i].append(str(sections[i][j-1]))

    out = [''.join(x) for x in out]
    out = ''.join(out)

    print("'" + out + "'")

    line = input()

