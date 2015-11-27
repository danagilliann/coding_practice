def fib(n):
	x = 0
	y = 1
	h = 0

	for r in range(0, n):
		print x 
		h = x + y
		y = x
		x = h

fib(10)
