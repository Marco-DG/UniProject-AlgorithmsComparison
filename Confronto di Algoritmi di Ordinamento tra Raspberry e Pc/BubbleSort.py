def BubbleSort(arr):
    
    q = 0
    i = len(arr)-1
    while i > 0:
        j = 0
        while j < i:
            if arr[j] > arr[j+1]:
                q = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = q
            j += 1
        i -= 1

    return arr