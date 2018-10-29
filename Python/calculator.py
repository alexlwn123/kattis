while True:
    try:
        line = input()
        print('%.2f' % eval(line))
    except EOFError:
        break
