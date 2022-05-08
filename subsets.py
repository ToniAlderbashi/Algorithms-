#By: Tonia Alderbashi and Vanja Glisic 

    
def subsets(lst):

    """This program produces a list of all possible subsets of some list

        pre: a list of items
        post: returns a list of all subsets in said list"""
    l1 = [[]]

    for item in lst:  
        
        l2 = []
        

        for i in l1:   
            
            s = i[:]
 
            s += [item]
            l2.append(s)

        l1.extend(l2)


    return l1




    
def recursive_subsets(full_lst):
    """This program produces a list of all possible subsets of some list

        pre: a list of items
        post: returns a list of all subsets in said list"""
    
    lists = []
    if len(full_lst) == 0:
        
        return [[]]
        
    else:
        short_lst = recursive_subsets(full_lst[1:])

        items = []
        for item in short_lst:
            items.append([full_lst[0]] + item)
            
        return  short_lst + items




def main():
    subsets(["a", "b", "c"])
    recursive_subsets([1,2,3,4])

main()
