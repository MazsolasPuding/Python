def selection_sort(arr):
    for i in range(len(arr)-1):
        min_ind = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
        print(arr)
    return arr



def main():
    arr = [2, 5, 3, 7, 1, 8, 9, 4, 2, 10, 3]
    print("original array : " , arr)
    sorted_arr = selection_sort(arr)
    print(sorted_arr)

if __name__ == "__main__":
    main()