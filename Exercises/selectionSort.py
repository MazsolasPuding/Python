array = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

def selection_sort(arr):
	for i in range(len(arr)):
		smallest = i
		#print(smallest)
		for j in range(i, len(arr)):
			if arr[j] < arr[smallest]:
				smallest = j
				print(arr[smallest])
		arr[i], arr[smallest] = arr[smallest], arr[i]
	return arr

print(selection_sort(array))
