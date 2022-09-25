def insertion_sort(arr):
    for i in range(len(arr)):
        curr = i
        for j in range(i-1, -1, -1):
            # print(f"i: {i}, j: {j}")
            if arr[curr] < arr[j]:
                arr[curr], arr[j] = arr[j], arr[curr]
                curr -= 1
            else: break
    return arr


def main():
    arr = [2, 5, 3, 7, 1, 8, 9, 4, 2, 10, 3]
    print("original array : " , arr)
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)

if __name__ == "__main__":
    main()