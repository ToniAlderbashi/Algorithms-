#By: Tonia Alderbashi 
#This program attemps to find the best sorting algorithm out of Bubble Sort,
    #Selection Sort and Comparison Count Sort.

from lists_of_numbers import *
from lists_of_numbers import add_one
from bubbleSort import *
from selection_sort import *
from comparison_count_sort import *
import time
import random


#Helper functions that run a certain algorithm 


def comparison_sort_time(size, total_comparison_sort = 0):
    
    """This function runs comparison count sort when called"""
    
    #This is where a list is chosen either randomized list of size "size"
        #or a list imported from lists_of_numbers.py that is in the same folder.
        #This also applies to the next two fucntions: bubble_sort_test() and
        #selection_sort_time()

        #In this case the list the function sorts is a randomly generated list
        #of a size specified by the user in the input statement of the main()
        #function bellow 
    
    lst = [random.randrange(0, 101) for j in range(size)]
    #lst = add_one_last()
    
    start = time.time()
    compr(lst)
    end = time.time()

    elapsed_time_compr = end-start
    total_comparison_sort += elapsed_time_compr
        
    return round(total_comparison_sort,4)      



def bubble_sort_test(size, total_bubble_sort = 0):
    
    """This function runs bubble sort when called"""
    
    lst = [random.randrange(0, 101) for j in range(size)]
    #lst = add_one_last()
        
    start = time.time()
    bubble_sort(lst)
    end = time.time()

    elapsed_time_bubble = end-start
    total_bubble_sort += elapsed_time_bubble

    return round(total_bubble_sort, 4)
    


def selection_sort_time(size, total_selection_sort = 0):
    
    """This function runs selection sort when called"""
    
    lst = [random.randrange(0, 101) for j in range(size)]
    #lst = add_one_last()
          
    start = time.time()
    SelectionSort(lst)
    end = time.time()

    elapsed_time_SelSort = end-start
    total_selection_sort += elapsed_time_SelSort

    return round(total_selection_sort, 4)


    
def run_x_times(x, size1):

    """The function that runs all the algorithms x number of times and prints the results
        on the screen. This function is helpful in avoid looping in all three sorting
        functions. """

    
    comparison_count = 0
    bubble_sort = 0
    selection_sort = 0


    for i in range(x):
        comparison_count += comparison_sort_time(size1)
        bubble_sort += bubble_sort_test(size1)
        selection_sort += selection_sort_time(size1)

    print()
    
    print("Total for Selection Sort for ",x, " repetitions: ",
          round(selection_sort,4))
    
    print("Total for Bubble Sort for ",x, " repetitions: ",
          round(bubble_sort,4))

    print("Total for Comparison Count Sort for",x, " repetitions: ",
          round(comparison_count,4))

def main():
    x = int(input("Enter the number of times to run the experiment: "))
    size1 = int(input("Enter the size of the list to run the experiment on: "))
    run_x_times(x,size1)
    
    
if __name__ == "__main__":
    main()
