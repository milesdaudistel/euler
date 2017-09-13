#for this problem, 0 is not a natural number
def sumsquaredifference():
	sum = 0
	squaresum = 0
	for i in range(101):
		sum += i
		squaresum += i*i
	print(sum*sum-squaresum)

sumsquaredifference()
	
