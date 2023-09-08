# Marco De Groskovskaja 06/02/23
'''
def MergeSort(arr):

    def _MergeSort(arr, p, r):
        if p < r:
            q = p+(r-p)//2

            _MergeSort(arr, p, q)
            _MergeSort(arr, q+1, r)
            _Merge(arr, p, q, r)


    def _Merge(arr, p, q, r):
        n_1 = q - p + 1
        n_2 = r - q

        L = [0] * (n_1)
        R = [0] * (n_2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n_1):
            L[i] = arr[p + i]

        for j in range(0, n_2):
            R[j] = arr[q + 1 + j]

        # Merge the temp arrays back into arr[p..r]
        i = 0	 # Initial index of first subarray
        j = 0	 # Initial index of second subarray
        k = p	 # Initial index of merged subarray

        while i < n_1 and j < n_2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n_1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n_2:
            arr[k] = R[j]
            j += 1
            k += 1


    return _MergeSort(arr, 0, len(arr) -1)
'''
def MergeSort(input_data):
    """
    Sorts the given list data using merge sort and returns a new copy of sorted data.
     If verbose is set to true, prints how much time the algorithm needed.
    """

    data = input_data.copy()
    data2 = data.copy()

    i = 0
    while 2**i < len(input_data):
        s1 = 0
        e1 = s1 + 2**i - 1
        s2 = e1 + 1
        e2 = s2 + 2**i - 1
        j = 0
        while s2 < len(input_data):
            if e2 >= len(input_data):
                e2 = len(input_data)-1
            while s1 <= e1 or s2 <= e2:
                if s2 > e2:
                    data2[j] = data[s1]
                    s1 += 1
                elif s1 <= e1 and data[s1] < data[s2]:
                    data2[j] = data[s1]
                    s1 += 1
                else:
                    data2[j] = data[s2]
                    s2 += 1
                j += 1
            s1 = e2 + 1
            e1 = s1 + 2**i - 1
            s2 = e1 + 1
            e2 = s2 + 2**i - 1
        data = data2
        data2 = data.copy()
        i += 1


    return data
