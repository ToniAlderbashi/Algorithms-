#By: Tonia ALderbashi

    
class Graph:
    """This class produces a graph object that consists of vertices and edges
        connecting them, with different weights. """
    
    def __init__(self, vertices, directed=False):

        self.directed = directed
        self.graph = {}
        

        for vertex in vertices:
            self.graph[vertex] = {}
        

    def add_edge(self, vertex1, vertex2, weight = 1):

        self.graph[vertex1][vertex2] = weight
        
        if not(self.directed):
            self.graph[vertex2][vertex1] = weight  


    def has_edge(self, vertex1, vertex2):
        try:
            c = self.graph[vertex1][vertex2]  
            return True
        except KeyError:
            return False

    def weight(self, v1, v2): 
        return self.graph[v1][v2]

    def vertex_iter(self): 

        for i in self.graph.keys():
            yield (i)


    def edge_iter(self):
        
        for v1 in self.vertex_iter():
            for v2 in self.graph[v1]:
                yield v1, v2

    def adjacent(self, v):
        return self.graph[v]
    
    def adjacent_list(self, v):
        vertex = self.graph[v]
        return list(self.graph[v].keys())











def read_file(filename):
    """This function reads a graph's vertices and edges and whether said
        graph is directed or not from a text file. Returns a graph object."""

    openfile = open(filename, "r")
    directed = openfile.readline()[0:].lower() == "directed"
    
    

    line = openfile.readline()
    line = line.strip()
    

    vertices = []
    
    vertices = line.split(" ")


    edges = []

        
    graph = Graph(vertices, edges)    

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        
        for line in lines[2:]:
            edges.append(line)
        if lines[-1] == '':
            edges.remove(edges[-1])

    for edge in edges:
        try:
            v1, v2= edge.split(" ")
            graph.add_edge(v1, v2)

        except:
            v1, v2, w = edge.split(" ")
            graph.add_edge(v1, v2, w)


    return graph

def main():
    read_file("testGraph1.txt").has_edge("a", "c")
    

main()
