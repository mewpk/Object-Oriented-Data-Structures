def bubble_sort(arr):
    swap = True
    while swap :
        swap = False
        for i in range(len(arr)-1):
            print(arr)
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1], arr[i]
                swap = True




    print(arr)
arr = [8,3,9,4,5]
bubble_sort(arr)