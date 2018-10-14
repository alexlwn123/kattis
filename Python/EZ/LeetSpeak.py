import sys

line = sys.stdin.readline()
line = line[:-1]
line = line.lower()
dictionary = {
	"a" : "@",
	"b" : "8",
	"c" : "(",
	"d" : "|)",
	"e" : "3",
	"f" : "#",
	"g" : "6",
	"h" : "[-]",
	"i" : "|",
	"j" : "_|",
	"k" : "|<",
	"l" : "1",
	"m" : "[]\\/[]",
	"n" : "[]\\[]",
	"o" : "0",
	"p" : "|D",
	"q" : "(,)",
	"r" : "|Z",
	"s" : "$",
	"t" : "']['",
	"u" : "|_|",
	"v" : "\\/",
	"w" : "\\/\\/",
	"x" : "}{",
	"y" : "`/",
	"z" : "2"
}
for c in line:
	if c in dictionary:
		print(dictionary[c], end = "")
	else:
		print(c, end = "")
	

