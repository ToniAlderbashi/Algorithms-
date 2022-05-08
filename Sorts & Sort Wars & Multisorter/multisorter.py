from bubbleSort import *
from selection_sort import *
from comparison_count_sort import *
import random
import time

#def multisorter(algorithm, size):


def main():
    size = int(input("Size: "))
    algorithm = int(input("Enter 0 for Bubble Sort, 1 for Selection Sort or 2 for \n"
                          "Comparison Counr Sort: "))
    trials = int(input("Number of trials: "))
    
    lst_alg = [bubble_sort, SelectionSort, compr]
    lst_algorithms = ["Bubble Sort", "Selection Sort", "Comparison Counr Sort"]
    print("This program runs", str(lst_algorithms[algorithm]), trials, "times.")
    total = 0
    
    for i in range(trials):
        lst = [random.randrange(0, size+1) for j in range(size)]
        start_time = time.time()
        lst_alg[algorithm](lst)
        end_time = time.time()
        

        elapsed_time = end_time - start_time
        total += elapsed_time
        
        
        print("trial", i+1, ":", round(elapsed_time,4))
    print("total time: ", round(total,4))

main()


