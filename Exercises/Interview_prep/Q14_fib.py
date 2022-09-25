def fib(n):
	"""..."""
	if n == 1:
		return 1
	if n == 0:
		return 0
	num = 0
	num = (fib(n-1) + fib(n-2))
	return num

def fib_list(n):
	"""..."""
	res = []
	for i in range(1, n+1):
		res.append(fib(i))
	return res

print(fib_list(40))
