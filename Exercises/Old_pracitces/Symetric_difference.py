sets1 = [[1, 2, 3, 4], [4, 5, 6, 9]]
sets2 = [[1, 2, 3, 4], [4, 5, 6, 9], [8, 7, 2, 5]]

def symetric_difference(sets):
	result = []
	for i in range(len(sets)):
		for value in sets[i]:
			if value in result:
				result.remove(value)
			else:
				result.append(value)
	return result

print(symetric_difference(sets1))
print(symetric_difference(sets2))