import math

def largestprime():
	num = 600851475143
	
	#pointless to consider 1, and 2 is obviously not a factor
	i = 3
	
	while num > i:
		if num % i == 0:
			num = num / i
		else:
			i += 2

	print(num)
	print(i)
	

largestprime()
