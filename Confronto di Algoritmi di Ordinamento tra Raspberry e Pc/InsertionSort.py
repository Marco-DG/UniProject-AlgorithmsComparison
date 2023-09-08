# Marco De Groskovskaja 06/02/23

# Slide 50
def InsertionSort(arr):

    for j in range(2, len(arr)):
        key = arr[j]

        # Inserisci A[j] nella sequenza ordinata A[1 . . j − 1]
        i = j -1
        while i > 0 and arr[i] > key:
            arr[i +1] = arr[i]
            i = i -1
        
        arr[i +1] = key
