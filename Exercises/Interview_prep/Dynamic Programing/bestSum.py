def best_sum(target, arr, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortest = None

    for num in arr:
        remainder = target - num
        remainder_comb = best_sum(remainder, arr, memo)
        if remainder_comb != None:
            result = remainder_comb[:]
            result.append(num)
        try:
            if shortest == None or len(result) < len(shortest):
                shortest = result
        except:
            continue
    memo[target] = shortest
    return shortest










def main():
    array = [2, 3, 25]
    target_sum = 1000
    res = best_sum(target_sum, array)
    print(res)

if __name__ == "__main__":
    main()