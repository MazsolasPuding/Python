"""
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
"""

def subarray_with_given_sum(array, target_sum):
    for i in range(len(array)):
        start_index = i
        remainder = target_sum - array[i]
        rest_array = array[i+1:]
        for j in range(len(rest_array)):
            end_index = i + j
            if remainder == 0: return (start_index+1, end_index+1)
            if remainder < 0: break
            print(remainder)
            remainder -= rest_array[j]
    return -1


def main():
    

    array = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
    target_sum = 468
    return subarray_with_given_sum(array, target_sum)


if __name__ == "__main__":
    res = main()
    print(res)