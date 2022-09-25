import random

rand = random.randint(1,100)
lst = list(range(1,101))
lst.remove(rand-1)


def find_missing(arr):
	"""..."""
	for i in range(len(arr)-1):
		if arr[i+1] != arr[i]+1:
			missing = arr[i+1]
			return missing


def find_duplicates(arr):
	uniqe = []
	duplicates = []
	for i in range(len(arr)):
		if not arr[i] in uniqe:
			uniqe.append(arr[i])
		else:
			duplicates.append(arr[i])
	return duplicates

lst = [1, 2, 3, 2, 4, 5, 3, 7, 8, 1, 9]
print(find_duplicates(lst))
