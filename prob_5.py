def gcd(x, y):
	if x>y:
		divisor, dividend=y,x
	else:
		divisor, dividend=x,y
	rem=dividend%divisor
	if rem==0:
		return divisor
	else:
		return gcd(rem, divisor)


def lcm(x, y):
	return (x*y)/gcd(x,y)

div=1
for i in range (1, 31):
	div=lcm(div, i)

print(div)