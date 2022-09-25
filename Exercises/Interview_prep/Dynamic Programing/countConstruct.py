# # Base recursion:
# def can_construct(string, arr):
#     if string == "": return 1
#     total = 0

#     for word in arr:
#         if string.find(word) == 0:
#             remaining = string[len(word):]
#             solutions = can_construct(remaining, arr)
#             total += solutions
            
#     return total

# # Dynamic:
# def can_construct_din(string, arr, memo={}):
#     if string in memo: return memo[string]
#     if string == "": return 1
#     total = 0

#     for word in arr:
#         if string.find(word) == 0:
#             remaining = string[len(word):]
#             solutions = can_construct_din(remaining, arr, memo)
#             total += solutions
    
#     memo[string] = total
#     return total




def count_construct(target, words, memo={}):
    if target in memo: return memo[target]
    if target == "": return 1
    
    solutions = 0
    for word in words:
        if target.find(word) == 0:
            remaining = target[len(word):]
            count = count_construct(remaining, words, memo)
            solutions += count
    memo[target] = solutions
    return solutions



def main():
    string = "eeeeeeeeeeeeeeeeeeeeeeeeee"
    arr = ["e", "ee", "eee", "eeee", "eeeee"]
    res = count_construct(string, arr)
    print(res)
    # res = can_construct(string, arr)
    # print(res)
    return 0


if __name__ == "__main__":
    main()

    