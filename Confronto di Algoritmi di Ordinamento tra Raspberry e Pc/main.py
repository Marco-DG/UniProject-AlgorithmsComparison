from QuickSort import QuickSort
from MergeSort import MergeSort
from InsertionSort import InsertionSort
from BubbleSort import BubbleSort
from TestUnit import TestUnit

import random

if __name__ == "__main__":

    test_unit = TestUnit()

    # Test sortings algorithm up to n = 'sort_up_to_lenght'
    sort_up_to_lenght = 300

    labels = [
        "Bubble Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort",
    ]

    colors = [
        "olive",
        "green",
        "orange",
        "purple"
    ]

    ### Test PC
    print("- Bubble Sort : Avg Case")
    # θ(n^2)
    timestamps = []
    for l in range(sort_up_to_lenght):
        array_to_sort = random.sample(range(0, l), l)
        timestamps.append(test_unit.Sort(BubbleSort, array_to_sort))
    pc_BubbleSort_timestamps = timestamps
    test_unit.PlotTimestamps(pc_BubbleSort_timestamps, "Pc_BubbleSort", color="blue")

    print("- Insertion Sort : Avg Case")
    # θ(n^2)
    timestamps = []
    for l in range(sort_up_to_lenght):
        array_to_sort = random.sample(range(0, l), l)
        timestamps.append(test_unit.Sort(InsertionSort, array_to_sort))
    pc_InsertionSort_timestamps = timestamps
    test_unit.PlotTimestamps(pc_InsertionSort_timestamps, "Pc_InsertionSort", color="blue")

    print("- Merge Sort : Avg Case")
    # θ(n log(n))
    timestamps = []
    for l in range(sort_up_to_lenght):
        array_to_sort = random.sample(range(0, l), l)
        timestamps.append(test_unit.Sort(MergeSort, array_to_sort))
    pc_MergeSort_timestamps = timestamps
    test_unit.PlotTimestamps(pc_MergeSort_timestamps, "Pc_MergeSort", color="blue")

    print("- Quick Sort : Avg Case")
    # θ(n log(n))
    timestamps = []
    for l in range(sort_up_to_lenght):
        array_to_sort = random.sample(range(0, l), l)
        timestamps.append(test_unit.Sort(QuickSort, array_to_sort))
    pc_QuickSort_timestamps = timestamps
    test_unit.PlotTimestamps(pc_QuickSort_timestamps, "Pc_Quicksort", color="blue")


    ### Plot Combined
    pc_timestamps = [
        pc_BubbleSort_timestamps,
        pc_InsertionSort_timestamps,
        pc_MergeSort_timestamps,
        pc_QuickSort_timestamps
    ]


    test_unit.PlotMultipleTimestamps(plot_name="Pc_CombinedTimestamps", timestamps_mat=pc_timestamps, labels_arr=labels, colors_arr=colors)


    ### Load Raspberry Data
    print("- Loading Raspberry Data")
    raspberry_timestamps = test_unit.LoadMatrix("raspberry_data")

    print("- Rasberry Data : Writing Plots")
    test_unit.PlotTimestamps(raspberry_timestamps[0], "Raspberry_BubbleSort",     color="red")
    test_unit.PlotTimestamps(raspberry_timestamps[1], "Raspberry_InsertionSort",  color="red")
    test_unit.PlotTimestamps(raspberry_timestamps[2], "Raspberry_MergeSort",      color="red")
    test_unit.PlotTimestamps(raspberry_timestamps[3], "Raspberry_Quicksort",      color="red")

    ## Combined Plots
    print("- Raspberry Data : Combining Plots")
    test_unit.PlotMultipleTimestamps(plot_name="Raspberry_CombinedTimestamps", timestamps_mat=raspberry_timestamps, labels_arr=labels, colors_arr=colors)


    print("- PC Data - Raspberry Data : Combining Plots")
    test_unit.PlotMultipleTimestamps(plot_name="PcVsRaspberry_BubbleSort", timestamps_mat=[pc_timestamps[0], raspberry_timestamps[0]], labels_arr=["Pc", "Raspberry"], colors_arr=["blue", "red"])
    test_unit.PlotMultipleTimestamps(plot_name="PcVsRaspberry_InsertionSort", timestamps_mat=[pc_timestamps[1], raspberry_timestamps[1]], labels_arr=["Pc", "Raspberry"], colors_arr=["blue", "red"])
    test_unit.PlotMultipleTimestamps(plot_name="PcVsRaspberry_MergeSort", timestamps_mat=[pc_timestamps[2], raspberry_timestamps[2]], labels_arr=["Pc", "Raspberry"], colors_arr=["blue", "red"])
    test_unit.PlotMultipleTimestamps(plot_name="PcVsRaspberry_QuickSort", timestamps_mat=[pc_timestamps[3], raspberry_timestamps[3]], labels_arr=["Pc", "Raspberry"], colors_arr=["blue", "red"])

    print("- Program Ended")
