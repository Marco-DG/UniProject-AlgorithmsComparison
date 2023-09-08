# Marco De Groskovskaja 08/02/23 - 15/02/23
# Ref: Introduction to Algorithms 3rd Ed., Chapter 11

from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np

class TestUnit:
    
    plots_path = "./Plots/"
    data_path = "./Data/"

    def PlotTimestamps(self, timestamps, plot_name, color="blue"):

        xpoints = range(len(timestamps))
        ypoints = timestamps

        #plt.title("Time per operation")
        plt.xlabel("Numero di operazioni")
        plt.ylabel("Tempo trascorso in secondi")

        plt.scatter(xpoints, ypoints, color=color)
        plt.savefig(self.plots_path+plot_name+".png")
        plt.clf()

    def PlotMultipleTimestamps(self, timestamps_mat, plot_name, labels_arr, colors_arr):
        num_curves = len(timestamps_mat)

        if num_curves != len(labels_arr):
            raise Exception("Error: timestamps_mat is of size: {}, while labels_arr is of size: {}, they should be equals".format(num_curves), len(labels_arr))

        if num_curves != len(colors_arr):
            raise Exception("Error: timestamps_mat is of size: {}, while colors_arr is of size: {}, they should be equals".format(num_curves), len(colors_arr))


        for curve_i in range(num_curves):

            xpoints = range(len(timestamps_mat[curve_i]))
            ypoints = timestamps_mat[curve_i]

            plt.scatter(xpoints, ypoints, color=colors_arr[curve_i], label=labels_arr[curve_i])

        #plt.title("Time per operation")
        plt.xlabel("Numero di operazioni")
        plt.ylabel("Tempo trascorso in secondi")

        plt.legend(loc="upper right")

        plt.savefig(self.plots_path+plot_name+".png")
        plt.clf()

    def SaveMatrix(self, matrix_name, matrix):
        
        np_mat = np.matrix(matrix)
        np_mat.dump(self.data_path + matrix_name + ".dat")

    def LoadMatrix(self, matrix_name):

        np_mat = np.load(self.data_path + matrix_name + ".dat", allow_pickle=True)
        return np_mat.tolist()

    def Sort(self, sorting_func, array_to_sort):

        arr = array_to_sort.copy()

        time_start = timer()
        sorting_func(arr)
        time_end = timer()

        elapsed_time = time_end - time_start
        return elapsed_time
