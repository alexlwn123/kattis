length = int(input())
check = ('aa', 'ee', 'ii', 'oo', 'uu', 'yy')
while length != 0:
    words = []
    counts = []
    for i in range(length):
        words.append(input())
        counts.append(0)
        for j in range(len(words[i])-1):
            if words[i][j:j+2] in check:
                counts[i] += 1
    length = int(input())
    print(words[counts.index(max(counts))])
