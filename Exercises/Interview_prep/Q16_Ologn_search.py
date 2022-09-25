arr = list(range(30))

def search(x, arr):
	"""..."""
	low = 0
	high = 0
	while(true):
		half = int(len(arr)/2)
		mid = arr[half]
		if x < mid:
			
			