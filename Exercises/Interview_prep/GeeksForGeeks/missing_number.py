def MissingNumber(array,n):
    array.sort()
    
    for i in range(0, n-1):
        if array[i]+1 not in array and array[i]+1 <= n:
            return array[i]+1
        elif array[i]-1 not in array and array[i]-1 > 0:
            return array[i]-1
    return -1


arr = [1]
res = MissingNumber(arr, 2)
print(res)