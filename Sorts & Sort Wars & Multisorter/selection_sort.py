import unittest 
#By: Tonia Alderbashi
#SelectionSort Algorithm

#The unittest will pass is return lst is uncommented 

def SelectionSort(lst):
    
    for i in range(len(lst)-1):
        minimum = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
            
        lst[i], lst[minimum] = lst[minimum], lst[i]

    #return lst


class SortTest(unittest.TestCase):
    """ Unit tests for the selection sort algorithm"""

    def test_sort(self):
        self.assertEqual([1,2,3,4], SelectionSort([4,3,2,1]))
        self.assertEqual([2,3,4,5], SelectionSort([5,4,3,2]))
        self.assertEqual([7,33,42,69,101], SelectionSort([7,101,42,33,69]))
        
if __name__ == "__main__":
    unittest.main()
