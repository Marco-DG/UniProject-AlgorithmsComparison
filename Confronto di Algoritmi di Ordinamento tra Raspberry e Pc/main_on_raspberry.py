from QuickSort import QuickSort
from MergeSort import MergeSort
from InsertionSort import InsertionSort
from BubbleSort import BubbleSort
from TestUnit import TestUnit

import random

data_path = "./Data/"

if __name__ == "__main__":

    test_unit = TestUnit()

    # Test sortings algorithm up to n = 'sort_up_to_lenght'
    sort_up_to_lenght = 300

    print("- Bubble Sort : Avg Case")
    # θ(n^2)
    timestamps = []
    for l in range(sort_up_to_lenght):
        array_to_sort = random.sample(range(0, l), l)
        timestamps.append(test_unit.Sort(BubbleSort, array_to_sort))
    bubble_sort_avg_case_timestamps = timestamps

    print("- Insertion Sort : Avg Case")
    # θ(n^2)
    timestamps = []
    for l in range(sort_up_to_lenght):
        array_to_sort = random.sample(range(0, l), l)
        timestamps.append(test_unit.Sort(InsertionSort, array_to_sort))
    insertion_sort_avg_case_timestamps = timestamps

    print("- Merge Sort : Avg Case")
    # θ(n log(n))
    timestamps = []
    for l in range(sort_up_to_lenght):
        array_to_sort = random.sample(range(0, l), l)
        timestamps.append(test_unit.Sort(MergeSort, array_to_sort))
    merge_sort_avg_case_timestamps = timestamps
 
    print("- Quick Sort : Avg Case")
    # θ(n log(n))
    timestamps = []
    for l in range(sort_up_to_lenght):
        array_to_sort = random.sample(range(0, l), l)
        timestamps.append(test_unit.Sort(QuickSort, array_to_sort))
    quick_sort_avg_case_timestamps = timestamps


    ##### STORE TIMESTAMPS TO CSV
    mat = [
        bubble_sort_avg_case_timestamps,
        insertion_sort_avg_case_timestamps,
        merge_sort_avg_case_timestamps,
        quick_sort_avg_case_timestamps
    ]

    test_unit.SaveMatrix("raspberry_data", mat)