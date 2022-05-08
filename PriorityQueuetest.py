#PriorityQueuetest.py
#This program uses unit testing to test cases of heap sort
#By: Isaac Nguyen & Tonia Alderbashi

import unittest
from PriorityQueue import *

class AutomaticHeapSortTesting(unittest.TestCase):
    def test_automaticheap(self):
        self.assertEqual([16, 17, 18, 19, 20], heapsort([20, 19, 18, 17, 16]))
        self.assertEqual([6, 7, 8, 9, 10], heapsort([7, 9, 8, 10, 6]))
        self.assertEqual([6, 6, 8, 9, 10], heapsort([6, 9, 8, 10, 6])) #edge case: duplicate items
        self.assertEqual([1, 25], heapsort([25, 1]))
        self.assertEqual([50], heapsort([50]))

if __name__ == "__main__":
    unittest.main()
