def pallindrome(n):
	n=str(n)
	s=""
	for x in n:
		s=x+s
	if s==n:
		return 1
	else:
		return 0

c=0
max=1
for x in range(999, 99, -1):
	for y in range(x, 99, -1):
		if pallindrome(x*y)==1:
			if x*y>max:
				max=x*y
print(max)
			
			
	
