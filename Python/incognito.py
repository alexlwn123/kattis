cases = int(input())
for i in range(cases):
    attrib = int(input())
    attribs = dict()
    for j in range(attrib):
        x = input().split(' ')[1]
        if x in attribs: attribs[x] += 1
        else: attribs[x] = 2

    out = 1
    for key in attribs:
        out *= attribs[key]
    print(str(out-1))
