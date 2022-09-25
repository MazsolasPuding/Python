array = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

def insertion_sort(arr):
	for i in range(1, len(arr)):
		while arr[i] < arr[i-1] and 0 < i:
			arr[i], arr[i-1] = arr[i-1], arr[i]
			i -= 1
	return arr

print(insertion_sort(array))
