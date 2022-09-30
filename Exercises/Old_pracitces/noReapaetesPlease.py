letters = "abc"
arr = [1,2,3]

# def permutate_all(word):
# 	"""Given a number of characters, find all permutations"""
# 	if len(word) == 1:
# 		return [word]

# 	perms = permutate_all(word[1:])
# 	char = word[0]
# 	result = []

# 	for perm in perms:
# 		for i in range(len(perm)+1):
# 			result.append(perm[:i] + char + perm[i:])
# 	return result

# def different_adjacent_letters(word):
# 	for i in range(1, len(word)-1):
# 		if word[i] != word[i-1] and word[i] != word[i+1]:
# 			return True


# permutations = permutate_all(letters)
# print(permutations)
# result = filter(different_adjacent_letters, permutations)
# print(list(result))


# def permutate(word):
# 	"""..."""
# 	if len(word) <= 1:
# 		return [word]
# 	perms = permutate(word[1:])
# 	char = word[0]
# 	result = []

# 	for perm in perms:
# 		for i in range(len(perm)+1):
# 			result.append(perm[i:] + char + perm[:i])
# 	return result

# print(permutate(letters))


def permutate_numbers(arr):
	"""..."""
	if len(arr) <= 1:
		return [arr]

	perms = permutate_numbers(arr[1:])
	num = arr[0]
	result = []

	for perm in perms:
		for i in range(len(perm)+1):
			temp = perm[1:] + [num] + perm[:1]
			result.append(temp)
	return result

print(permutate_numbers(arr))
