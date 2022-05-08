import unittest 
#By: Tonia Alderbashi
#Bubble Sort Algorithm

#The unittest will pass is return lst is uncommented 

def bubble_sort(lst): #insert a list to be sorted in non-decreasing order 
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j+1] < lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    #return lst

   
class SortTest(unittest.TestCase):
    """ Unit tests for the bubble sort algorithm"""

    def test_sort(self):
        self.assertEqual([1,2,3,4], bubble_sort([4,3,2,1]))
        self.assertEqual([2,3,4,5], bubble_sort([5,4,3,2]))
        self.assertEqual([7,33,42,69,101], bubble_sort([7,101,42,33,69]))
        
if __name__ == "__main__":
    unittest.main()
