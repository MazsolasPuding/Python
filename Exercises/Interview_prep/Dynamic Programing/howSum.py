# # Basic approach:
# def how_sum_basic(target, arr):
#     if target == 0: return []
#     if target < 0: return None

#     for elem in arr:
#         remainder = target - elem
#         remainder_res = how_sum_basic(remainder, arr)
#         if remainder_res != None:
#             remainder_res.append(elem)
#             return remainder_res


# # Dynamic appropach:
# def how_sum_dynamic(target, arr, memo={}):
#     if target in memo: return memo[target]
#     if target == 0: return []
#     if target < 0: return None

#     for elem in arr:
#         remainder = target - elem
#         remainder_res = how_sum_dynamic(remainder, arr, memo)
#         if remainder_res != None:
#             result =  remainder_res[:]
#             result.append(elem)
#             memo[target] = result
#             return memo[target]

#     memo[target]= None
#     return None




def how_sum(target, arr, memo={}):
    if target in memo: return memo[target]
    elif target == 0: return [[]]
    elif target < 0: return []

    for num in arr:
        remainder = target - num
        result = how_sum(remainder, arr, memo)
        if result != []:
            result[0].append(num)
            memo[target] = result
            return memo[target]
    memo[target] = []
    return []



def main():
    array = [7, 15]
    target_sum = 300
    #res = how_sum_basic(target_sum, array)
    res = how_sum(target_sum, array)
    print(res)


if __name__ == "__main__":
    main()