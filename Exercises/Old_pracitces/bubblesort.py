array = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

def bubbleSort(arr):
	while(True):
		swapped = False
		for i in range(len(arr)-1):
			if arr[i+1] < arr[i]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				swapped = True
		if swapped == False:
			break
	return arr

print(bubbleSort(array))
