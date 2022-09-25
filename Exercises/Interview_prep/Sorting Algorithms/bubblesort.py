def bubble_sort(arr):
    for j in range(len(arr)):
        switch = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                switch = True
        if not switch:
            break
    return arr




def main():
    arr = [1, 5, 3, 7, 4, 8, 9, 4, 2, 10, 3]
    print(arr)
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)

if __name__ == "__main__":
    main()