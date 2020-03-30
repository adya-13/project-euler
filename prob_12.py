def factors(n):
	c=0
	for i in range(1, n+1):
		if n%i==0:
			c+=1
	return c

n=1
c=1
while True:
	if n%2==0:
		c=factors(int(n/2))*factors(n+1)
	else:
		c=factors(n)*factors(int((n+1)/2))
	if c>500:
	 	print(n*(n+1)//2)
	 	break	
	n+=1

