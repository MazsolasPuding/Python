# Basic approach:
# def can_sum(target_sum, arr):
#     if target_sum == 0: return True
#     if target_sum < 0: return False

#     for num in arr:
#         remainder = target_sum - num
#         if (can_sum(remainder, arr)):
#             return True
#     return False







def can_sum(target, arr):
    if target == 0: return True
    if target < 0: return False

    for num in arr:
        remainder = target - num
        if(can_sum(remainder, arr)):
            return True
    return False


def can_sum_breadth(target, arr):
    queue = [target]

    while queue:
        # print(queue)
        current = queue.pop(0)
        if current == 0: return True
        if current < 0: continue
        
        for num in arr:
            current -= num
            queue.append(current)
    return False


# Dynamic approach:
# def can_sum_memo(target_sum, arr, memo={}):
#     if target_sum in memo: return memo[target_sum]
#     if target_sum == 0: return True
#     if target_sum < 0: return False

#     for num in arr:
#         remainder = target_sum - num
#         if (can_sum_memo(remainder, arr, memo)):
#             memo[target_sum] = True
#             return True
#     memo[target_sum] = False
#     return False



def can_sum_memo(target, arr, memo={}):
    if target == 0: return True
    if target < 0: return False

    for num in arr:
        remainder = target - num
        if(can_sum_memo(remainder, arr, memo)):
            memo[target] = True
            return True
    memo[target] = False
    return False



def main():
    target = 90
    array = [2, 3]
    res = can_sum(target, array)
    print(res)
    res = can_sum_memo(target, array)
    print(res)
    res = can_sum_breadth(target, array)
    print(res)


if __name__ == "__main__":
    main()
