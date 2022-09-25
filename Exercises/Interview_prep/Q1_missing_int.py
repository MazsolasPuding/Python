import random

arr = list(range(1,100))
rand = random.randint(1,100)
arr.remove(rand)
print(rand)

def find_missing(arr):
	for i in range(len(arr)-1):
		if arr[i+1] != arr[i]+1:
			return arr[i]+1

print(find_missing(arr))
