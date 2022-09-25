from itertools import combinations


import pprint

def all_construct(target, words):
    if target == "": return [[]]
    
    combinations = []

    for word in words:
        if target.find(word) == 0:
            remaining = target[len(word):]
            current_comb = all_construct(remaining, words)
            result = [*current_comb]
            for i in range(len(result)):
                result[i].append(word)
            for j in range(len(result)):
                combinations.append(result[j])
    print(len(combinations))
    return combinations



def main():
    string = "eeeee"
    arr = ["e", "ee", "eee", "eeee", "eeeee"]
    res = all_construct(string, arr)
    pprint.pprint(res)
    # res = can_construct(string, arr)
    # print(res)


if __name__ == "__main__":
    main()
