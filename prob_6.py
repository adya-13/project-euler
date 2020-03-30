def sum_square(n):
	return ((n*(n+1))/2)**2

def square_sum(n):
	return (n*(n+1)*(2*n+1))/6

print(sum_square(100)-square_sum(100))