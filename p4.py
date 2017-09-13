def ispalindrome(n):
	backwards = 0
	temp = n
	while temp > 0:
		backwards = backwards * 10 + temp % 10
		temp = temp // 10

	return backwards == n

def largestproductpalindrome():
	largest = 0
	for i in range(100, 999):
		for j in range(100, 999):
			p = i*j
			if ispalindrome(p) and p > largest:
				largest = p
	print(largest)

largestproductpalindrome()
		
