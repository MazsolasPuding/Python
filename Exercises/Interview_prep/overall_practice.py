# def subArraySum(arr, n, s): 
#    #Write your code here
#     print(n)
#     if n == 0: return True
#     if n < 0: return False
#     # print(arr)

#     for i in range(len(arr)):
#         remainder = n - arr[i]
#         if subArraySum(arr[i+1:], remainder, s): 
#             # print(n)
#             return True

#     return False


# def subArraySum(arr, target, s): 
#    #Write your code here
#     for i in range(len(arr)):
#         remainder = target - arr[i]

#         for j in range(i+1, len(arr)):
#             remainder -= arr[j]
#             if remainder < 0: break
#             elif remainder == 0: return [i, j]

#     return False


# def subArraySum(arr, n, s): 
#    #Write your code here
#     for i in range(n):
#         sum = arr[i]

#         for j in range(i+1, n):
#             sum += arr[j]
#             if sum > s: break
#             elif sum == s: return [i+1, j+1]

#     return [-1]


# arr = [3, 4, 1, 5, 2]
# res = subArraySum(arr, 10, 5)
# print(res)


"""Fibonachi sequence"""
# O(2^n) Time, O(n) Space
# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list_fib = list(map(fib, range(0, 10)))
# print(list_fib)

# # O(n) Time
# def fib(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 2:
#         return 1
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)
#     return memo[n]

# print(list(map(fib, range(1, 11))))



# """River task"""
# arr = [
#     [0, 1, 1, 0, 1],
#     [0, 0, 1, 0, 0],
#     [1, 0, 0, 1, 1],
#     [1, 0, 0, 1, 0]
# ]
# def river(arr):
#     ones = []
#     for row in range(len(arr)):
#         for column in range(len(arr[row])):
#             if arr[row][column] == 1:
#                 ones.append((row, column))
    
#     for coord in ones:
#         a, b = coord
        

#     return ones
    



# print(river(arr))

# tup1 = (1, 2)
# tup2 = (2, 1)
# a, b = tup1
# c, d = tup2
# tupminus = (a-c, b-d)
# print(tupminus)






