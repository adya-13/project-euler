def digit_sum(n):
	n=str(n)
	sum=0
	for i in n:
		sum=sum+int(i)
	return sum

print(digit_sum(2**1000))