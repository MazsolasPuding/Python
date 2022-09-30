array = [7, 9, 11, 13, 15]

def pairwise(arr, arg):
	"""Return the sum of indices where the sum of two elements == arg."""
	result = 0
	used = []
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i == j:
				pass
			elif (arr[i] + arr[j] == arg) and (i not in used) and (j not in used):
				print(f"{arr[i]} + {arr[j]} = {arg}")
				result += i + j
				used.append(i)
				used.append(j)
	return result

print(pairwise(array, 20)) #6
print(pairwise([0, 0, 0, 0, 1, 1], 1)) #10
print(pairwise([], 100)) #0
print(pairwise([1, 3, 2, 4], 4)) #1
