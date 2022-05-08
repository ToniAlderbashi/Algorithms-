#By: Tonia Alderbashi 
#I worked on this other recursive implementation of Priority Queue
    #for an Extra Credit opportunity 
#I worked on another one with Isaac 

class PQ:
    def __init__(self, length_array):
        #for node in items:
            #self.add(node)
        #self.store = [0] * len(list(items))
        self.store = [0] * length_array
        self.length = length_array
        self.size = 0
       

    #find the parent index of node
    def _find_parent(self, node):
        return (node-1) // 2
        

    #find the left child index of node
    def find_left_child(self, node):
        #print("find left child for node", node)
        #print("it is", 2 * node + 1)
        return 2 * node + 1

    #find the right child index of node
    def find_right_child(self, node):
        return 2 * node + 2

    #return boolian indicating existence of a parent

    def has_parent(self, node):
        ##print('p', self._find_parent(node))
        return self._find_parent(node) >= 0

    #return boolian indicating existence of a left child

    def has_left_child(self, node):
        #print("node", node)
        return self.find_left_child(node) < self.size

    #return boolian indicating existence of a right child

    def has_right_child(self, node):
        return self.find_right_child(node) < self.size

    #return actual value of parent

    def parent(self, node):
        print(self.store)
        return self.store[self._find_parent(node)]

    #return actual value of left child

    def left_child(self, node):
        return self.store[self.find_left_child(node)]

    #return actual value of right child

    def right_child(self, node):
        return self.store[self.find_right_child(node)]

    #check if the array is full

    def is_full(self):
        return self.size  == self.length

    #swap

    def swap(self, index1, index2):
        root = self.store[index1]
        self.store[index1] = self.store[index2]
        self.store[index2] = root

    def _largest_child(self, i):
        
        if self.has_left_child:
            bigger_child = self.find_left_child(i)
            if self.has_right_child(i) and self.right_child(i) > self.left_child(i):
                bigger_child = self.find_right_child(i)
                
            return self.store[bigger_child]
        else:
            return None 

    def _build_heap(self):
        for node in self.store:
            self.add(node)

    #insert key at the last position of the heap
    #check if it is the correct position using bubble_up()

    def add(self, key):
        if self.is_full() and key > self.store[0]:
            k = self.store[0]
            self.store[0] = key
            self.store[-1] = k
            #self.store = self.store.append(0)
            #raise ValueError ("Heap is Full")

        
        #print(self.size)
        self.store[self.size] = key
        self.size = self.size + 1
        self._bubble_up(key)
        

        self._bubble_up(self.size - 1)

    def _bubble_up(self, key):
        
        
        if self.has_parent(key) and self.parent(key) < self.store[key]:
            self.swap(self._find_parent(key), key)
            self._bubble_up(self._find_parent(key))

    def get_max(self):
        #if self.size == 0:
            #raise ValueError ("Heap is Empty, Add Items!")
        item = self.store[0]
        self.store[0] = self.store[self.size-1]
        self.size = self.size - 1
        self._bubble_down(item)
        return item

    def _bubble_down(self, i = 0):

        #initialize largest to the parent
        largest = i

        #check if the node has a left child and if it is larger
        if self.has_left_child(i) and (self.store[largest] < self.left_child(i)):
            
            #if True assign left child of i to largest
            largest = self.find_left_child(i)
            
        #check if the right child is larger than largest (left child)
        if self.has_right_child(i) and (self.store[largest] < self.right_child(i)):

            #if True assign right child of i to largest
            largest = self.find_right_child(i)

        #check is largest is different than i
        #if True swap
        if largest != i:
            self.swap(i, largest)
            
            #repeat for the rest of the tree
            self._bubble_down(largest)

            
            
            
       

    def get_max(self):
        max_item = self.store[0]
        return max_item
"""
 largest = self._largest_child(i)
        if self.store[i] > self.store[child]:
            child = self.find_left_child(i)
        if 

        else:
            self.swap(i, child)
            self.bubble_down(biggest_child)"""
def main():

    print("This programm builds a Priority Queue for the following values ")
    print()
    print("5   8   1   4   7   2   3   6   9")
    print()
    pq = PQ(9)
    pq.add(5)
    pq.add(8)
    pq.add(1)
    pq.add(4)
    pq.add(7)
    pq.add(2)
    pq.add(3)
    pq.add(6)
    
    pq.add(9)

    pq.swap(pq.store[0], pq.store[-1])
    
    
    
    
        
    print('max', pq.get_max())
    print(pq._build_heap())
    
    

    
    
    
main()

        
            
        
