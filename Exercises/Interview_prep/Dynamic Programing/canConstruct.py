# # Base recursion:
# def can_construct(string, arr):
#     if string == "": return True

#     for word in arr:
#         if string.find(word) == 0:
#             remaining = string[len(word):]
#             if (can_construct(remaining, arr)):
#                 return True
    
#     return False

# # Dynamic:
# def can_construct_din(string, arr, memo={}):
#     if string in memo: return memo[string]
#     if string == "": return True

#     for word in arr:
#         if string.find(word) == 0:
#             remaining = string[len(word):]
#             if (can_construct_din(remaining, arr, memo)):
#                 memo[string] = True
#                 return True
    
#     memo[string] = False
#     return False


def can_construct(target, words, memo={}):
    if target in memo: return memo[target]
    if target == "": return True

    for word in words:
        if target.find(word) == 0:
            remaining = target[len(word):]
            if (can_construct(remaining, words, memo)):
                memo[target] = True
                return True
    memo[target] = False
    return False




def main():
    string = "eeeeeeeeeeeeeeeeeeeeeeeeef"
    arr = ["e", "ee", "eee", "eeee", "eeeee"]
    res = can_construct(string, arr)
    # res = can_construct_din(string, arr)
    print(res)
    return 0


if __name__ == "__main__":
    main()

    