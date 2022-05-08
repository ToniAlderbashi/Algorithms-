#By: Tonia ALderbashi

#Insertion sort algorithm

def insertion_sort(lst):
    
    lst_length = len(lst)

    for i in range(1, lst_length):
        
        item = lst[i]
        
        j = i - 1

        while j >= 0 and lst[j] > item:

            lst[j + 1] = lst[j]

            j -= 1

        lst[j + 1] = item
    
    

def main():
    lst = insertion_sort([9,8,7,6,5,4,3,2,1])
    

main()
