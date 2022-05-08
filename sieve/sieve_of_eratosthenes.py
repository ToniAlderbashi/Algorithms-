#By: Tonia Alderbashi
#Sieve of eratosthenes

import math
def sieve(n):
    lst = [i for i in range(2, n+1)]
    limit = math.floor(math.sqrt(n))
    for i in range(2, limit + 1 ):
        if lst[i-2] != 0:
            j = i*i
            while j <= n:
                lst[j-2] = 0
                j = j + i
    primes = []
    for item in lst:
        if item != 0:
            primes.append(item)
    return primes


            
    
def main():
    n = int(input("Enter a positive integer to calculate the primes \n"
                  "ranging from 2 to the integer: "))
    return print(sieve(n))
    
            
main()
