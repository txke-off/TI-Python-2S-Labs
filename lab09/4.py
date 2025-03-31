def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list)-1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Пример использования
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
index = binary_search(sorted_list, target)
print(f'Элемент {target} найден на индексе {index}')
