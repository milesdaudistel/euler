def smallestmultiple():
	n = 2520
	while (not divisibleby1to20(n)):
		n += 1
	print(n)
	
def divisibleby1to20(n):
	for i in range(2, 20):
		if n % i != 0:
			return False
	return True

smallestmultiple()
