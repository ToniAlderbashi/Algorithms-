import unittest 
#By: Tonia Alderbashi
#Comparison Count Sort Algorithm and testing code

#The unittest will pass is return lst is uncommented 

def compr(lst):
    
    count = [0 for i in range(len(lst))]
    

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] < lst[j]:
                count[j] = count[j]+1
            else:
                count[i] = count[i]+1
    s_lst = [None for i in range(len(lst))]
    for i in range(len(lst)):
        s_lst[count[i]]=lst[i]
    return s_lst


class SortTest(unittest.TestCase):
    """ Unit tests for the compare count sort algorithm"""

    def test_sort(self):
        self.assertEqual([1,2,3,4], compr([4,3,2,1]))
        self.assertEqual([2,3,4,5], compr([5,4,3,2]))
        self.assertEqual([7,33,42,69,101], compr([7,101,42,33,69]))
        
if __name__ == "__main__":
    unittest.main()



    
