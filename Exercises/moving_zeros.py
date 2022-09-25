"""Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements."""

arr = [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]

def move_zeros(array):
	cnt = 0
	i = 0
	while (i < len(arr)):
		if array[i] == 0:
			del array[i]
			cnt += 1
			i -= 1
		i += 1
	while(cnt):
		array.append(0)
		cnt -= 1
	return array

print(arr)
print(move_zeros(arr))
