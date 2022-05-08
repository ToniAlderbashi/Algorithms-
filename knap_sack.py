#By Tonia and Isaac
#KnapSack Program 
import random
import functools
memoize = functools.lru_cache(maxsize=None)

from random import randrange

#import sys
#sys.setrecursionlimit(1000)

class knap_sack:

    def __init__(self, items):
        self.items = list(items)
        self.F = memoize(self.F)

    def F(self, n, C):
       
        #base case is at (-1) because the algorithm is indexed at 1 
        if n == -1 or C == -1:
            return 0

        else:

            #extrect weight and value from the input
            wn, vn = self.items[n]

            #if the weight of an item exceeds the current capasity
            #recursively run the function on the item prior
            if C - wn < 0:
                return self.F(n-1, C)
            
            #as long as the weight of an item does not exceed the current
            #capasity, run the function of item n and n-1
            #return the maximum

            #when running the function on n, add the value of n 
            else:
                return max(self.F(n - 1, C), vn + self.F(n -1 , C - wn))

             


    def solution(self, n, C):
        result = self.F(n, C)
        pairs = []
        
        #while the number of items in non-negative
        while n >= 0:
            
            

            #check if self.F(n) is bigger than  self.F(n-1)
                #if the value increased after including item n 
            if self.F(n, C) > self.F(n-1, C):

                #extrect the weight and value 
                w, v = self.items[n]

                #append the pair consisting of weight and value of the item 
                pairs.append((w,v))

                #decrease capasity 
                C -= w
                
            
            n -= 1
        

        return result, pairs
    


def main():
    print()
    print("The Knapsack Alg ")
    print()
    items = int(input("How many items do you want to run Knap Sack on? "))
    n = int(input("How many items do you want in the sack? "))
    c = int(input("How big is the capacity of the (how much weight it can hold)? "))
    

    pairs = []
    for i in range(items):
        w = randrange((items//2) - items//7)
        v = randrange(items//2)
        p = (w,v)
        pairs.append(p)
    ks = knap_sack(pairs)
    print(ks.solution(n, c))


main()
                    
                
               
            
        
