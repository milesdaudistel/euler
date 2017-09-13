def evenfib():
	t1 = 1
	t2 = 2
	sum = 0	

	while t2 < 4000000:
		if t2 % 2 == 0:
			sum += t2

		temp = t1+t2
		t1 = t2
		t2 = temp
	print(sum)

evenfib()
