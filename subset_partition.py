#By: Tonia Alderbashi

#Subset patition algortihm

from subsets import recursive_subsets


def SubsetPartition(lst):


    if sum(lst) % 2 != 0:
        return [], []

    for subset in recursive_subsets(lst):
        
        subset_sum = sum(subset)
        
        items_left = lst[:]

        for element in subset:
            
            items_left.remove(element)

        if subset_sum == sum(items_left):
            
            return items_left, subset
            
    return [], []



