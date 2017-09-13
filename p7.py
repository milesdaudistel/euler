import math


def bigprime():
	counter = 0
	n = 1
	while counter < 10001:
		n += 1
		if isprime(n):
			counter += 1
	print(n)


def isprime(n):
	for i in range(2, math.floor(math.sqrt(n))+1):
		if n % i == 0:
			return False
	if n == 1:
		return False
	return True

if __name__ == '__main__':
	bigprime()
