from p7 import isprime

print(isprime(1))
sum = 0
for i in range(2000000):
	if isprime(i):
		sum += i


print(sum)
