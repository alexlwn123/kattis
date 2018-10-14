import sys
import itertools

def main():
	line = sys.stdin.readline()

	print(''.join(k for k, g in itertools.groupby(line)))
	
if __name__ == '__main__':
	main()