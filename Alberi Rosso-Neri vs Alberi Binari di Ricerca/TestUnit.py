# Marco De Groskovskaja 24/01/23 - 10/02/23 - 13/02/23

import random
from timeit import default_timer as timer
import statistics
import matplotlib.pyplot as plt

class TestUnit:

    plots_path = "./Plots/"

    number_of_ops = 10000

    # Smoothing the data by taking the mean every 'data_compression_avg_every' of a subarray of size 'data_compression_avg_size'
    data_compression_avg_size = 500
    data_compression_avg_every = 250

    def PlotTimestamps(self, timestamps, plot_name, color="blue"):

        xpoints = range(self.number_of_ops)
        ypoints = timestamps

        xpoints_compressed = [statistics.mean(xpoints[i:(i +self.data_compression_avg_size)]) for i in range(0, self.number_of_ops, self.data_compression_avg_every)]
        ypoints_compressed = [statistics.mean(ypoints[i:(i +self.data_compression_avg_size)]) for i in range(0, self.number_of_ops, self.data_compression_avg_every)]

        #plt.title("Time per operation")
        plt.xlabel("Numero di operazioni")
        plt.ylabel("Tempo trascorso in secondi")

        plt.ylim(min(ypoints_compressed[:1000]), statistics.mean(ypoints_compressed[-1000:])*2)

        plt.scatter(xpoints_compressed, ypoints_compressed, color=color)
        plt.savefig(self.plots_path+plot_name+".png")
        plt.clf()

    def PlotTwoTimestamps(self, timestamps_1, timestamps_2, plot_name, label_1, label_2):
        xpoints_1 = range(self.number_of_ops)
        ypoints_1 = timestamps_1

        xpoints_1_compressed = [statistics.mean(xpoints_1[i:(i +self.data_compression_avg_size)]) for i in range(0, self.number_of_ops, self.data_compression_avg_every)]
        ypoints_1_compressed = [statistics.mean(ypoints_1[i:(i +self.data_compression_avg_size)]) for i in range(0, self.number_of_ops, self.data_compression_avg_every)]
  
        xpoints_2 = range(self.number_of_ops)
        ypoints_2 = timestamps_2

        xpoints_2_compressed = [statistics.mean(xpoints_2[i:(i +self.data_compression_avg_size)]) for i in range(0, self.number_of_ops, self.data_compression_avg_every)]
        ypoints_2_compressed = [statistics.mean(ypoints_2[i:(i +self.data_compression_avg_size)]) for i in range(0, self.number_of_ops, self.data_compression_avg_every)]

        #plt.title("Time per operation")
        plt.xlabel("Numero di operazioni")
        plt.ylabel("Tempo trascorso in secondi")

        plt.ylim(min(min(ypoints_1_compressed[:1000]), min(ypoints_2_compressed[:1000]) ), max(statistics.mean(ypoints_1_compressed[-1000:]) , statistics.mean(ypoints_2_compressed[-1000:]))*1.5 )

        plt.scatter(xpoints_1_compressed, ypoints_1_compressed, label=label_1, color="blue")
        plt.scatter(xpoints_2_compressed, ypoints_2_compressed, label=label_2, color="red")

        plt.legend(loc="upper right")

        plt.savefig(self.plots_path+plot_name+".png")
        plt.clf()

    # Test Implementetions
    def Insertions(self, tree, unbalanced=False):
        # Unbalanced Toggle
        numbers_list = [n for n in range(self.number_of_ops)]
        if not unbalanced:
            random.shuffle(numbers_list)

        # Evaluate
        timestamps = []
        for i in range(self.number_of_ops):

            time_start = timer()
            tree.insert(numbers_list[i])
            time_end = timer()

            elapsed_time = time_end - time_start
            timestamps.append(elapsed_time)

        return timestamps

    def Searches(self, tree, unbalanced=False):
        # Unbalanced Toggle
        numbers_list = [n for n in range(self.number_of_ops)]
        if not unbalanced:
            random.shuffle(numbers_list)

        # Populate Tree
        for e in numbers_list:
            tree.insert(e)

        # Shuffle
        #if not unbalanced:
        #    random.shuffle(numbers_list)

        # Evaluate
        timestamps = []
        for i in range(self.number_of_ops):

            time_start = timer()
            tree.search(numbers_list[i])
            time_end = timer()

            elapsed_time = time_end - time_start
            timestamps.append(elapsed_time)

        return timestamps 

    def Deletions(self, tree, unbalanced=False):
        # Unbalanced Toggle
        numbers_list = [n for n in range(self.number_of_ops)]
        if not unbalanced:
            random.shuffle(numbers_list)

        # Populate Tree
        for e in numbers_list:
            tree.insert(e)

        # Shuffle
        random.shuffle(numbers_list)

        # Evaluate
        timestamps = []
        for i in range(self.number_of_ops):

            time_start = timer()
            val = numbers_list[i]
            tree.remove(val)
            time_end = timer()

            elapsed_time = time_end - time_start
            timestamps.append(elapsed_time)

        return list(reversed(timestamps))
