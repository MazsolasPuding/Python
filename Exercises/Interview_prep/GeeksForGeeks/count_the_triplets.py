# def triplet_counter(array):
#     counter = 0
#     for number in array:
#         rest = array[:]
#         rest.remove(number)
#         counter += find_triplet(number, rest)
#     return counter//2


# def find_triplet(target, array):
#     queue = [(target, 0, [])]
#     triplet_count = 0

#     while queue:
#         current = queue.pop(0)
#         print(current)

#         current_target, current_depth, used_nums = current
#         if current_depth > 2 or current_target < 0 or (len(used_nums) == 2 and used_nums[0] == used_nums[1]): continue
#         if current_target == 0 and current_depth == 2:
#             triplet_count += 1        
        
#         for num in array:
#             num_list = current[2][:]
#             num_list.append(num)
#             queue.append((current[0]-num, current[1]+1, num_list))
#     return triplet_count



# def countTriplet(arr, n):
#  # code here
#     arr.sort()
#     count = 0
#     for k in range(n, 2, -1):
#         i = k - 1
#         r = i - 1
#         l = 0
#         while l < r:
#             sum = arr[l] + arr[r]
#             if sum == arr[i]:
#                 count += 1
#                 l += 1
#                 r -= 1
#             elif sum < arr[i]:
#                 l += 1
#             else:
#                 r-=1
#     return count

def triplet_counter(arr, length):
    count = 0

    for i in range(length):
        for j in range(length):
            if j == i: continue
            for k in range(length):
                if j == k: continue
                if arr[i] == arr[j] + arr[k]:
                    count += 1

    return count



def main():
    arr = [14, 3, 6, 8, 11, 16]
    res1 = triplet_counter(arr, len(arr))
    # res2 = countTriplet(arr, len(arr))
    return (res1)


if __name__ == "__main__":
    res = main()
    print(res)