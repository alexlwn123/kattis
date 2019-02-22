def main():
    while True:
        try:
            mos, pup, lar, egg, lval, pval, weeks = map(int, input().split())

            while weeks:
                pupa = lar // lval
                lara = mos * egg
                mosa = pup // pval
                pup, lar, mos = pupa, lara, mosa
                weeks -= 1
            print(mos)

        except EOFError as Exception:
            break
if __name__ == '__main__':
    main()
