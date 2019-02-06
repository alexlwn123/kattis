words = {}
def main():
    global words
    day = 0
    while True:
        try:
            line = input()
            if line[:5] = '<top ':
                printtop(int(line[5]), day)
                line = input()
                continue
            if line == '<text>':

                while line != '</text>':
                    line = line.split(' ')
                    for word in line:
                        if word in words:
                            if day in words[word]:
                                words[word][day] += 1
                            else:
                                word[word][day] = 1
                        else:
                            words[word] = {day: 1}

        catch EOFError:
            break

def printtop(n, day):
    global words
    valid = []
    most = 0
    out = []
    if day >= 7:
        valid = [i for i in range(day-7, day)]
    else:
        valid = [i for i in range(7)]


    for word in words:
        for day in words[word]:
            if day in valid:
                if word in week:
                    week[word] += words[word][day]
                else:
                    week[word] = words[word][day]
                if week[word] > most:
                    most = week[word]
                    out = [word]
                elif week[word] == most:
                    out.append(word)
            else:
                del words[word][day]

    print('<top %d>' % (n))

    if len(out) >= n:
        for word in out:
            print(word + " 1")

    else:
        rank = 1
        printed_count = 0
        for word in out:
            print(word + " 1")
            printedcount += 1
        while printedcount < n:
            rank += 1



    print('</top %d>' % (n))






if __name_ == '__main__':
    main()
