def main():

    while True:
        p,a = map(int, input().split())
        if a == p == 0:
            break
        if pow(a,p,p) == a and not isPrime(p):
            print("yes")
        else:
            print("no")

def isPrime(n):
    for i in range(2, int(n**.5 + 1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
