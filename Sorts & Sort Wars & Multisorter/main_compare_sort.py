#By: Tonia Alderbashi
#Empirical test of the efficiency of the algorithm

import time
import random
from comparison_count_sort import *

def main():
    print("Welcome to the Comparison Count Sorter\n")
    size = int(input("Enter the list size: "))
    trials = int(input("Enter the number of trials: "))
    total = 0
    print()
    for i in range(trials):
        lst = [random.randrange(0, size+1) for j in range(size)]
            
        start = time.time()
        compr(lst)
        end = time.time()

        elapsed_time = end-start
        total += elapsed_time
        
        

        print("trial ", i+1, ": ", round(elapsed_time,4))
    print()

    average = round(total/trials, 4)
    print("total: ", round(total,4))
    print()

    print("average: ", average)
    
    
if __name__ == "__main__":
    main()
