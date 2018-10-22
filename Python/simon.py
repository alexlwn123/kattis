import sys
def main():
    lines = sys.stdin.read().splitlines()

    for line in lines[1:]:
        out = ''
        if line[:11] == 'simon says ':
            out = line[11:]
        print(out)


if __name__ == '__main__':
    main()
