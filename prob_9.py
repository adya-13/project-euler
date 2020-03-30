def pythagorean_triplet(n):
	for i in range(1, int(n/2)):
		for j in range(i+1, 1001):
			k=n-i-j
			if(i*i+j*j==k*k):
				return i*j*k
print(pythagorean_triplet(1000))