def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted or gap > 1:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        sorted = True

        for i in range(0, n-gap):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                sorted = False
    
    return arr

# Пример
arr = [12, 20, 31, 24, 3, 17, 40]
sorted_arr = comb_sort(arr)
print(sorted_arr)