sieve=[True]*(1<<20)

sieve[0] = False
sieve[1] = False

index = 2
while index**2<len(sieve):
	if sieve[index]:
		j = index**2
		while j<len(sieve):
			sieve[j] = False
			j+=index
	index+=1

def isprime(n):
	if n<len(sieve):
		return sieve[n]
	index=2
	while index**2<=n:
		if index<len(sieve) and not sieve[index]:
			index+=1
			continue
		if not n%index:
			return False
		index+=1
	return True




def gcd(a,b):
	while b:
		r= a%b
		a,b = b,r
	return a

def prob(n):
	count,pcount=0,0
	for base in [2,8,10,16]:
		try:
			nb = int(n,base)
		except:
			pass
		else:
			count+=1
			if isprime(nb):
				pcount+=1
	d= gcd(count,pcount)
	count//=d
	pcount//=d
	return '%d/%d'%(pcount,count)



t = int(raw_input())

for _ in xrange(t):
	n= raw_input()
	print prob(n)
