#By: Tonia Alderbashi
#Quick sort algorithm and a helper function Lomuto's Partition algorithm

def quicksort(lst, l, r):

    if l < r:
        s = LomutoPartition(lst, l, r)
        quicksort(lst, l, s - 1)
        quicksort(lst, s + 1, r)
    return lst



def LomutoPartition(lst,l,r):

    p = lst[l]
    s = l

    for i in range(l+1,r):
        if lst[i] < p:
            s += 1
            lst[s],lst[i] = lst[i],lst[s]
    lst[l],lst[s] = lst[s],lst[l]
    return s


                   
