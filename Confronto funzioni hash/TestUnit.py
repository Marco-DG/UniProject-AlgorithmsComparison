# Marco De Groskovskaja 08/02/23 - 15/02/23
# Ref: Introduction to Algorithms 3rd Ed., Chapter 11

import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

class TestUnit:
    
    plots_path = "./Plots/"

    number_of_ops = None


    def __init__(self, number_of_ops):
        self.number_of_ops = number_of_ops

    def PlotTimestamps(self, timestamps, plot_name, color="blue", ylabel="Tempo trascorso in secondi"):

        xpoints = range(len(timestamps))
        ypoints = timestamps

        #plt.title("Time per operation")
        plt.xlabel("Numero di operazioni")
        plt.ylabel(ylabel)

        plt.scatter(xpoints, ypoints, color=color)
        plt.savefig(self.plots_path+plot_name+".png")
        plt.clf()

    def PlotTwoTimestamps(self, timestamps_1, timestamps_2, plot_name, label_1, label_2, ylabel="Tempo trascorso in secondi"):
        xpoints_1 = range(self.number_of_ops)
        ypoints_1 = timestamps_1

        xpoints_2 = range(self.number_of_ops)
        ypoints_2 = timestamps_2

        #plt.title("Time per operation")
        plt.xlabel("Numero di operazioni")
        plt.ylabel(ylabel)

        plt.scatter(xpoints_1, ypoints_1, label=label_1, color="blue")
        plt.scatter(xpoints_2, ypoints_2, label=label_2, color="red")

        plt.legend(loc="upper right")

        plt.savefig(self.plots_path+plot_name+".png")
        plt.clf()

    def CountCollisionOnInsertions(self, hash_table, numbers_list):
        
        # Evaluate
        collisions = []
        for i in range(self.number_of_ops):

            hash_table.insert(numbers_list[i], numbers_list[i])

            # Count Collisions as the sum of the size of all linked lists
            count = 0
            for ll in hash_table.h:
                if ll.size > 1:
                    count += ll.size -1
            
            collisions.append(count)

        return collisions


    def Insertions(self, hash_table, numbers_list):

        # Evaluate
        timestamps = []
        for i in range(self.number_of_ops):

            time_start = timer()
            hash_table.insert(numbers_list[i], numbers_list[i])
            time_end = timer()

            elapsed_time = time_end - time_start
            timestamps.append(elapsed_time)

        return timestamps

    def Searches(self, hash_table, numbers_list):

        # Populate hash_table
        for e in numbers_list:
            hash_table.insert(e, e)

        # Shuffle
        random.shuffle(numbers_list)

        # Evaluate
        timestamps = []
        for i in range(self.number_of_ops):

            time_start = timer()
            hash_table.search(numbers_list[i])
            time_end = timer()

            elapsed_time = time_end - time_start
            timestamps.append(elapsed_time)

        return timestamps 

    def Deletions(self, hash_table, numbers_list):

        # Populate hash_table
        for e in numbers_list:
            hash_table.insert(e, e)

        # Shuffle
        random.shuffle(numbers_list)

        # Evaluate
        timestamps = []
        for i in range(self.number_of_ops):

            time_start = timer()
            val = numbers_list[i]
            hash_table.remove(val)
            time_end = timer()

            elapsed_time = time_end - time_start
            timestamps.append(elapsed_time)

        return list(reversed(timestamps))
