def straight_sort(arr):
    count = 0
    for i in range(len(arr)-1):
        max_value = arr[0]
        index_max = 0
        for j in range(len(arr)-count):
            if arr[j] > max_value:
                max_value = arr[j]
                index_max = j
        arr[len(arr)-1-count], arr[index_max] = arr[index_max], arr[len(arr)-1-count]
        count += 1
    print(arr)
arr = [8, 3, 9, 4, 5]
# straight_sort(arr)

def straight_sortV2(arr , count=0):
    if count == len(arr)-1:
        return arr
    max_value = max(arr[:len(arr)-count])
    find_index = arr.index(max_value)
    arr[len(arr)-1-count], arr[find_index] = arr[find_index], arr[len(arr)-1-count]
    count += 1
    return straight_sortV2(arr , count)

print(straight_sortV2(arr))
