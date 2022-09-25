array = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

def quick_sort(arr):
	pivot = len(arr)-1
	if len(arr) <= 1: return arr
	for i in range(pivot+1):
		mem = i
		if(arr[pivot] < arr[i] and 0 < pivot):
			while(i <= pivot and i < len(arr)-1):
				arr[i], arr[i+1] = arr[i+1], arr[i]
				i += 1
			pivot -= 1
			i = mem
		print(arr)
		print(pivot)
	arr = quick_sort(arr[:pivot]) + quick_sort(arr[pivot:])
	return arr


print(quick_sort(array))