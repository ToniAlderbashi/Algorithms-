#PriorityQueue.py
#This program implements a PriorityQueue class using a Python list managed as a heap
#By: Isaac Nguyen and Tonia Alderbashi
'''implement heapsort(lst)
Your heapsort can just make a PriorityQueue from the list and
then use a series of get_max calls to assign items back into the list (back to front).
'''
from math import isqrt
from random import randrange

class PriorityQueue:

    def __init__(self, items=[]):
        self.heap = list(items)	 
        self._build_heap()

    def get_pq(self):
        return self.heap

    def _largest_child(self, i):
        """ returns index of node i's largest child or None when node i is a leaf """
        try:
            left = self.heap[2*i+1]
            try:
                right = self.heap[2*i+2]
                if right > left:
                    return 2*i+2
                else:
                    return 2*i+1
            except:
                return 2*i+1
        except:
            return None    
            '''if (self.heap[2*i+1]) == None:
            return None
        else:
            if self.heap[2*i+1] > self.heap[2*i+2]:
                print(self.heap[2*i+1])
                return 2*i+1
            else:
                return 2*i+2'''
        
    def _bubble_up(self, i):
        """ restore heap by bubbling up from node i """
        while i > 0:
            pi = (i-1) // 2
            if self.heap[i] <= self.heap[pi]:
                break
            self.heap[i], self.heap[pi] = self.heap[pi], self.heap[i]
            i = pi

    def _bubble_down(self, i):
        """ restore heap by bubbling down from node i """
        k = self._largest_child(i)
        print(k, i)
        if (k != None) and (self.heap[k] > self.heap[i]):
            self.heap[k], self.heap[i] = self.heap[i], self.heap[k]
            self._bubble_down(k)

    def _build_heap(self):
        ''' builds an initial heap bottom-up
        //Input: An array H [1..n] of orderable items
        //Output: A heap H [1..n]'''
        heap_size = len(self.heap)
        for i in range(isqrt(heap_size//2), 0):
            k = i
            v = self.heap[k]
            h = False
            while not h and 2*k <= heap_size:
                print("BUILD", self.heap)
                j = 2*k
                if j < n: #there are 2 children
                    if self.heap[j] < self.heap[h+1]:
                        j = j + 1
                if v >= self.heap[j]:
                    h = True
                else:
                    self.heap[k] = self.heap[j]
                    k = j
            self.heap[k] = v
            print("BUILD", self.heap)

    def add(self, item):
        """ add item to the queue """
        self.heap.append(item)

    def get_max(self):
        """ returns and removes highest priority item """
        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(0)

    def get_size(self):
        return len(self.heap)

def heapsort(lst):
    pq = PriorityQueue(lst)
    sorted_heap = []
    while pq.get_size() > 0:
        sorted_heap.append(pq.get_max())
    return sorted_heap

def main():
    print("This program implements a PriorityQueue class using a Python list managed as a heap.")
    n = int(input("Enter the number of nodes in your binary tree: "))
    random_lst = [randrange(0, 100) for i in range(0, n)]
    print(random_lst)
    PriorityQueue(random_lst)
    sorted_list = heapsort(random_lst)
    print("Your sorted list is: ", sorted_list)
    

if __name__ == '__main__':
    main()
