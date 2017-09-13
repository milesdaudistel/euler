#a^2 + b^2 = c^2
#a + b + c = 1000
#a + b + root(a^2 + b^2) = 1000

import math

for a in range(1, 1000):
	for b in range(1, 1000):
		c = math.sqrt(a*a+b*b)
		if a+b+c == 1000:
			print("a=" + str(a))
			print("b=" + str(b))
			print("c=" + str(c))
			print("product=" + str(a*b*c))
