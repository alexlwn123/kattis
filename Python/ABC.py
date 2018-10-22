import sys
def main():
    line1 = sys.stdin.readline().split(" ")
    line1[-1] = line1[-1][:-1]
    line2 = sys.stdin.readline()[:-1]
    line1.sort(key=int)
    
    dictionary = {
            'A' : line1[0],
            'B' : line1[1],
            'C' : line1[2]
            }
	
    print(dictionary.get(line2[0]) + " " + dictionary.get(line2[1]) + " " + dictionary.get(line2[2]))

if __name__ == '__main__':
	main()
