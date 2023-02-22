from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        try:
            f = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError
        self.graph = {}
        for line in f.readlines():
            verts = line.split()
            self.add_vertex(verts[0])
            self.add_vertex(verts[1])
            self.add_edge(verts[0], verts[1])
        f.close()
        # This method should call add_vertex and add_edge!!!

    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if not self.graph.get(key):
            self.graph[key] = Vertex(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph.get(v1).adjacent_to.append(v2)
        self.graph.get(v2).adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        return self.graph.get(key)

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        #return self.vertices.sort()
        return sorted(self.graph.keys())

    def conn_components(self):
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        # This method MUST use Depth First Search logic!
        visited = {}
        vertices = []
        stack = Stack(len(self.graph))
        for key in self.graph.keys():
            visited[key] = False  # initializes every vertex as unvisited. will be changed.
        for key in self.graph.keys():
            if visited[key] is False:
                # if the key hasn't been visited, push it to runtime stack
                temp = []
                stack.push(key)
                while stack.is_empty() is False:
                    # pop the vert and check if its adjacent verts have been visited
                    cur = stack.pop()
                    if visited[cur] is True:
                        continue
                    # adjust the visited dictionary so that cur has a value True
                    visited[cur] = True
                    # append curr to the connected components
                    temp.append(cur)
                    for v in self.graph.get(cur).adjacent_to:
                        if visited[v] is False:
                            stack.push(v)
                            # add unvisited neighbors to runtime stack
                vertices.append(sorted(temp))
        return sorted(vertices)

    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        # This method MUST use Breadth First Search logic!
        color = {}  # color by key
        queue = Queue(len(self.graph.keys()))
        for key in self.graph.keys():
            # initialize all color as None
            color[key] = None
        for key in self.graph.keys():
            if color[key] is None:
                color[key] = 1
                queue.enqueue(key)
                # color and add to runtime queue
                while queue.is_empty() is False:
                    # dequeue and alternate coloring
                    vert = queue.dequeue()
                    for v in self.graph.get(vert).adjacent_to:
                        if not color[v]:
                            color[v] = 1 - color.get(vert)
                            queue.enqueue(v)
                        elif color[v] == color[vert]:
                            return False
        return True

