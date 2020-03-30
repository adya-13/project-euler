def primes(n):
	sum=0
	sieve=[True for i in range(n+1)]
	i=2
	while (i*i<=n):
		if(sieve[i]==True):
			for j in range(i+i, n+1, i):
				sieve[j]=False
		i=i+1

	for i in range(2,n+1):
		if sieve[i]:
			sum=sum+i
	return sum
	

print(primes(2000000-1))