arr = [2,2,3,1,5,1,6,7,4,3,8]

def find_duplicates(arr):
	"""..."""
	temp = []
	duplicates = []
	for i in range(len(arr)):
		if not arr[i] in temp:
			temp.append(arr[i])
		else:
			duplicates.append(arr[i])
	return duplicates

print(find_duplicates(arr))
