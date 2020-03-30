def isPrime(n):
	if n<=1:
		return False

	if n==2 or n==3:
		return True

	if n%2==0:
		return False
	elif n%3==0:
		return False
	else:
		for i in range(6, int(n**0.5) + 2, 6):
			if n%(i+1)==0 or n%(i-1)==0 :
				return False
	return True

def nthprime(n):
	i=3
	count=1
	while count<n:
		if isPrime(i):
			count = count+1
		i=i+2
	return i-2