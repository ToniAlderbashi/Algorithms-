#By: Tonia Alderbashi

#Source removal algorithm

from GraphClass import Graph
 

def make_indegree(graph):
    indegree = {vertex:0 for vertex in graph.vertex_iter()}

    
    for edge in graph.edge_iter():
        
        
        indegree[edge[1]] += 1
    return indegree 
        
    
def find_source(indegree):
    
    for vertex in indegree:
        
        if indegree[vertex] == 0:
            return(vertex)
    return False


def removeSource(graph):

    indegree = make_indegree(graph)
    
    source = find_source(indegree)
    
    sorted_lst = []
    

    while source:
        for vertex in graph.adjacent_list(source):
            indegree[vertex]-= 1

        del indegree[source]
        
        sorted_lst.append(source)

        source = find_source(indegree)
   
    return sorted_lst


def main():

    g = Graph(["a", "b", "c", "d", "e", "f", "g"], True)
    g.add_edge("b", "a")
    g.add_edge("b", "c")
    g.add_edge("a", "d")
    g.add_edge("d", "e")
    g.add_edge("d", "f")
    g.add_edge("c", "a")

    removeSource(g)

main()
    

    
