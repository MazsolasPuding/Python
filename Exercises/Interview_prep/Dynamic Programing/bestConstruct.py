from itertools import combinations


def best_construct(target, words, memo={}):
    if target in memo: return memo[target]
    if target == "": return []

    best_combination = None

    for word in words:
        if target.find(word) == 0:
            remaining = target[len(word):]
            current_comb = best_construct(remaining, words, memo)
            result = current_comb[:]
            result.append(word)
            if best_combination == None or len(best_combination) > len(result):
                best_combination = result

    memo[target] = best_combination
    return best_combination





def main():
    string = "eeeeeeeeeeeeeeeeeeeeeee"
    arr = ["e", "ee", "eee", "eeee", "eeeee"]
    res = best_construct(string, arr)
    print(res)
    # res = can_construct(string, arr)
    # print(res)
    return 0


if __name__ == "__main__":
    main()
