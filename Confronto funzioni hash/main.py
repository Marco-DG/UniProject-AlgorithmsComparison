# Marco De Groskovskaja 08/02/23 - 16/02/23

import random

from HashDivisionMethod import HashDivisionMethod
from HashMultiplicationMethod import HashMultiplicationMethod
from TestUnit import TestUnit

if __name__ == "__main__":

    m = 1000
    test_unit = TestUnit(m)


    ###### Number List Randomized
    numbers_list_randomized = random.sample(range(0, m*10), m)


    ### Time measures
    print("- HashDivisionMethod Insertions")
    hdm_insertions_timestamps = test_unit.Insertions(HashDivisionMethod(m), numbers_list_randomized)
    test_unit.PlotTimestamps(hdm_insertions_timestamps, "HDM_Insertions", color="blue")

    print("- HashDivisionMethod Searches")
    hdm_searches_timestamps = test_unit.Searches(HashDivisionMethod(m), numbers_list_randomized)
    test_unit.PlotTimestamps(hdm_searches_timestamps, "HDM_Searches", color="blue")

    print("- HashDivisionMethod Deletions")
    hdm_deletions_timestamps = test_unit.Deletions(HashDivisionMethod(m), numbers_list_randomized)
    test_unit.PlotTimestamps(hdm_deletions_timestamps, "HDM_Deletions", color="blue")

    print("- HashMultiplicationMethod Insertions")
    hmm_insertions_timestamps = test_unit.Insertions(HashMultiplicationMethod(m), numbers_list_randomized)
    test_unit.PlotTimestamps(hmm_insertions_timestamps, "HMM_Insertions", color="red")

    print("- HashMultiplicationMethod Searches")
    hmm_searches_timestamps = test_unit.Searches(HashMultiplicationMethod(m), numbers_list_randomized)
    test_unit.PlotTimestamps(hmm_searches_timestamps, "HMM_Searches", color="red")

    print("- HashMultiplicationMethod Deletions")
    hmm_deletions_timestamps = test_unit.Deletions(HashMultiplicationMethod(m), numbers_list_randomized)
    test_unit.PlotTimestamps(hmm_deletions_timestamps, "HMM_Deletions", color="red")

    ### Collisions count

    ### Collisions per Load Factor
    n = [i for i in range(0, m)]

    print("- HashDivisionMethod Collisions on Insertions")
    hdm_insertions_collisions = test_unit.CountCollisionOnInsertions(HashDivisionMethod(m), numbers_list_randomized)
    test_unit.PlotTimestamps(hdm_insertions_collisions, "HDM_CollisionsOnInsertions", color="blue", ylabel="Numero di collisioni")

    print("- HashMultiplicationnMethod Collisions on Insertions")
    hmm_insertions_collisions = test_unit.CountCollisionOnInsertions(HashMultiplicationMethod(m), numbers_list_randomized)
    test_unit.PlotTimestamps(hmm_insertions_collisions, "HMM_CollisionsOnInsertions", color="red", ylabel="Numero di collisioni")



    ### Print Combined Plots
    print("- Combining Plots")
    test_unit.PlotTwoTimestamps(hdm_insertions_timestamps, hmm_insertions_timestamps, "HDM_HMM_Insertions", "Metodo delle divisioni", "Metodo delle moltiplicazioni")
    test_unit.PlotTwoTimestamps(hdm_searches_timestamps, hmm_searches_timestamps, "HDM_HMM_Searches", "Metodo delle divisioni", "Metodo delle moltiplicazioni")
    test_unit.PlotTwoTimestamps(hdm_deletions_timestamps, hmm_deletions_timestamps, "HDM_HMM_Deletions", "Metodo delle divisioni", "Metodo delle moltiplicazioni")
    
    test_unit.PlotTwoTimestamps(hdm_insertions_collisions, hmm_insertions_collisions, "HDM_HMM_CollisionsOnInsertions", "Metodo delle divisioni", "Metodo delle moltiplicazioni", ylabel="Numero di collisioni")


    '''
    ###### Number List m multiple

    numbers_list_unbalanced = [1+m*i for i in range(m)]


    ### Time measures
    print("- HashDivisionMethod Unbalanced Insertions")
    hdm_unbalanced_insertions_timestamps = test_unit.Insertions(HashDivisionMethod(m), numbers_list_unbalanced)
    test_unit.PlotTimestamps(hdm_unbalanced_insertions_timestamps, "HDM_Unbalanced_Insertions", color="cyan")

    print("- HashDivisionMethod Unbalanced Searches")
    hdm_unbalanced_searches_timestamps = test_unit.Searches(HashDivisionMethod(m), numbers_list_unbalanced)
    test_unit.PlotTimestamps(hdm_unbalanced_searches_timestamps, "HDM_Unbalanced_Searches", color="cyan")

    print("- HashDivisionMethod Unbalanced Deletions")
    hdm_unbalanced_deletions_timestamps = test_unit.Deletions(HashDivisionMethod(m), numbers_list_unbalanced)
    test_unit.PlotTimestamps(hdm_unbalanced_deletions_timestamps, "HDM_Unbalanced_Deletions", color="cyan")

    print("- HashMultiplicationMethod Unbalanced Insertions")
    hmm_unbalanced_insertions_timestamps = test_unit.Insertions(HashMultiplicationMethod(m), numbers_list_unbalanced)
    test_unit.PlotTimestamps(hmm_unbalanced_insertions_timestamps, "HMM_Unbalanced_Insertions", color="orange")

    print("- HashMultiplicationMethod Unbalanced Searches")
    hmm_unbalanced_searches_timestamps = test_unit.Searches(HashMultiplicationMethod(m), numbers_list_unbalanced)
    test_unit.PlotTimestamps(hmm_unbalanced_searches_timestamps, "HMM_Unbalanced_Searches", color="orange")

    print("- HashMultiplicationMethod Unbalanced Deletions")
    hmm_unbalanced_deletions_timestamps = test_unit.Deletions(HashMultiplicationMethod(m), numbers_list_unbalanced)
    test_unit.PlotTimestamps(hmm_unbalanced_deletions_timestamps, "HMM_Unbalanced_Deletions", color="orange")

    ### Collisions count

    ### Collisions per Load Factor
    n = [i for i in range(0, m)]

    print("- HashDivisionMethod Collisions on Unbalanced Insertions")
    hdm_unbalanced_insertions_collisions = []
    for n_i in n:
        hdm_unbalanced_insertions_collisions.append(test_unit.CountCollisionOnInsertions(HashDivisionMethod(m), numbers_list_unbalanced, n_i))
    test_unit.PlotTimestamps(hdm_unbalanced_insertions_collisions, "HDM_Unbalanced_CollisionsOnInsertions", color="cyan")

    print("- HashMultiplicationnMethod Collisions on Unbalanced Insertions")
    hmm_unbalanced_insertions_collisions = []
    for n_i in n:
        hmm_unbalanced_insertions_collisions.append(test_unit.CountCollisionOnInsertions(HashMultiplicationMethod(m), numbers_list_unbalanced, n_i))
    test_unit.PlotTimestamps(hmm_unbalanced_insertions_collisions, "HMM_Unbalanced_CollisionsOnInsertions", color="orange")
    '''