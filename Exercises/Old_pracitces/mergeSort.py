import math
array = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]
simple = [4,3,2,1]

def mergeSort(arr):
	if len(arr)<=1:
		return arr
	half = math.floor(len(arr)/2)
	arr1 = arr[:half]
	arr2 = arr[half:]
	result = []
	arr1 = mergeSort(arr1)
	arr2 = mergeSort(arr2)
	i, j = 0, 0

	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1
	result = result + arr1[i:] + arr2[j:]

	return result
	

print(mergeSort(array))
