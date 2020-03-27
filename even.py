a=1 
b=2 
sum=2 
c=0
while True:
	c=a+b
	a=b
	b=c
	if(c<=4000000):
		if(c%2==0):
			sum=sum+c
	else:
		break

print(sum)