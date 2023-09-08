# Marco De Groskovskaja 24/01/23 - 10/02/23 - 13/02/23

from BinarySearchTree import BinarySearchTree
from RedBlackTree import RedBlackTree
from TestUnit import TestUnit
 
if __name__ == "__main__":

    test_unit = TestUnit()

    test_unit.number_of_ops = 10000
    test_unit.data_compression_avg_size = 100
    test_unit.data_compression_avg_every = 50

    ### Balanced
    # BST
    print("- BST Test Insertions")
    bst_insertions_timestamps = test_unit.Insertions(BinarySearchTree())
    test_unit.PlotTimestamps(bst_insertions_timestamps, "BST_Insertions", color="blue")
    print("- BST Test Searches")
    bst_searches_timestamps = test_unit.Searches(BinarySearchTree())
    test_unit.PlotTimestamps(bst_searches_timestamps, "BST_Searches", color="blue")

    print("- BST Test Deletions")
    bst_deletions_timestamps = test_unit.Deletions(BinarySearchTree())
    test_unit.PlotTimestamps(bst_deletions_timestamps, "BST_Deletions", color="blue")

    # RBT
    print("- RBT Test Insertions")
    rbt_insertions_timestamps = test_unit.Insertions(RedBlackTree())
    test_unit.PlotTimestamps(rbt_insertions_timestamps, "RBT_Insertions", color="red")
    
    print("- RBT Test Searches")
    rbt_searches_timestamps = test_unit.Searches(RedBlackTree())
    test_unit.PlotTimestamps(rbt_searches_timestamps, "RBT_Searches", color="red")
    
    print("- RBT Test Deletions")
    rbt_deletions_timestamps = test_unit.Deletions(RedBlackTree())
    test_unit.PlotTimestamps(rbt_deletions_timestamps, "RBT_Deletions", color="red")

    ### Unbalanced
    # BST
    print("- BST Test Unbalanced Insertions")
    bst_unbalanced_insertions_timestamps = test_unit.Insertions(BinarySearchTree(), unbalanced=True)
    test_unit.PlotTimestamps(bst_unbalanced_insertions_timestamps, "BST_Unbalanced_Insertions", color="blue")
    
    print("- BST Test Unbalanced Searches")
    bst_unbalanced_searches_timestamps = test_unit.Searches(BinarySearchTree(), unbalanced=True)
    test_unit.PlotTimestamps(bst_unbalanced_searches_timestamps, "BST_Unbalanced_Searches", color="blue")

    print("- BST Test Unbalanced Deletions")
    bst_unbalanced_deletions_timestamps = test_unit.Deletions(BinarySearchTree(), unbalanced=True)
    test_unit.PlotTimestamps(bst_unbalanced_deletions_timestamps, "BST_Unbalanced_Deletions", color="blue")

    # RBT
    print("- RBT Test Unbalanced Insertions")
    rbt_unbalanced_insertions_timestamps = test_unit.Insertions(RedBlackTree(), unbalanced=True)
    test_unit.PlotTimestamps(rbt_unbalanced_insertions_timestamps, "RBT_Unbalanced_Insertions", color="red")
    
    print("- RBT Test Unbalanced Searches")
    rbt_unbalanced_searches_timestamps = test_unit.Searches(RedBlackTree(), unbalanced=True)
    test_unit.PlotTimestamps(rbt_unbalanced_searches_timestamps, "RBT_Unbalanced_Searches", color="red")
    
    print("- RBT Test Unbalanced Deletions")
    rbt_unbalanced_deletions_timestamps = test_unit.Deletions(RedBlackTree(), unbalanced=True)
    test_unit.PlotTimestamps(rbt_unbalanced_deletions_timestamps, "RBT_Unbalanced_Deletions", color="red")

    ### Print Combined Plots
    print("- Combining Plots")

    # BST Balanced / BST Unbalanced
    test_unit.PlotTwoTimestamps(bst_insertions_timestamps, bst_unbalanced_insertions_timestamps, "BST_Balanced_Unbalanced_Insertions", "BST balanced", "BST unbalanced")
    test_unit.PlotTwoTimestamps(bst_searches_timestamps, bst_unbalanced_searches_timestamps, "BST_Balanced_Unbalanced_Searches", "BST balanced", "BST unbalanced")
    test_unit.PlotTwoTimestamps(bst_deletions_timestamps, bst_unbalanced_deletions_timestamps, "BST_Balanced_Unbalanced_Deletions", "BST balanced", "BST unbalanced")

    # RBT Balanced / RBT Unbalanced
    test_unit.PlotTwoTimestamps(rbt_insertions_timestamps, rbt_unbalanced_insertions_timestamps, "RBT_Balanced_Unbalanced_Insertions", "RBT balanced", "RBT unbalanced")
    test_unit.PlotTwoTimestamps(rbt_searches_timestamps, rbt_unbalanced_searches_timestamps, "RBT_Balanced_Unbalanced_Searches", "RBT balanced", "RBT unbalanced")
    test_unit.PlotTwoTimestamps(rbt_deletions_timestamps, rbt_unbalanced_deletions_timestamps, "RBT_Balanced_Unbalanced_Deletions", "RBT balanced", "RBT unbalanced")

    # BST Balanced / RBT Balanced
    test_unit.PlotTwoTimestamps(bst_insertions_timestamps, rbt_insertions_timestamps, "BST_RBT_Insertions", "BST balanced", "RBT balanced")
    test_unit.PlotTwoTimestamps(bst_searches_timestamps, rbt_searches_timestamps, "BST_RBT_Searches", "BST balanced", "RBT balanced")
    test_unit.PlotTwoTimestamps(bst_deletions_timestamps, rbt_deletions_timestamps, "BST_RBT_Deletions", "BST balanced", "RBT balanced")

    # BST Unbalanced / RBT Unbalanced
    test_unit.PlotTwoTimestamps(bst_unbalanced_insertions_timestamps, rbt_unbalanced_insertions_timestamps, "BST_RBT_Unbalanced_Insertions", "BST unbalanced", "RBT unbalanced")
    test_unit.PlotTwoTimestamps(bst_unbalanced_searches_timestamps, rbt_unbalanced_searches_timestamps, "BST_RBT_Unbalanced_Searches", "BST unbalanced", "RBT unbalanced")
    test_unit.PlotTwoTimestamps(bst_unbalanced_deletions_timestamps, rbt_unbalanced_deletions_timestamps, "BST_RBT_Unbalanced_Deletions", "BST unbalanced", "RBT unbalanced")
