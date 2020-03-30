def factorial(n):
	if n==0:
		return 1
	else:
		fact=1
		for i in range (1, n+1):
			fact=fact*i
		return fact

def sum_digit(n):
	n=str(n)
	sum=0
	for i in n:
		sum=sum+int(i)
	return sum

print((sum_digit(factorial(100))))
