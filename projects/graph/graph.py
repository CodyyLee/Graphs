"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist.')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create empty queue and enqueue a starting vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        #create a set to store the visited vertices
        visited = set()

        #while the queue is not empty
        while queue.size() > 0:
            #dequeue the first vertex
            vertex = queue.dequeue()

            #if vertex has not been visited
            if vertex not in visited:
                #mark the vertex as visited
                visited.add(vertex)
                #add all neighbors to back of queue
                for next_vertex in self.get_neighbors(vertex):
                    queue.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                for next_vertex in self.get_neighbors(vertex):
                    stack.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        visited.add(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create an empty queue and enqueue PATH to the starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])

        #create a set to store visited vertices
        visited = set()

        #while queue is not empty
        while queue.size() > 0:
            #dequeue the first PATH
            path = queue.dequeue()
            #grab the last vertex from the PATH
            vertex = path[-1]

            #check if the vertex has not been visited
            if vertex not in visited:
                #is this vertex the target?
                if vertex is destination_vertex:
                    #return the PATH
                    return path

                #mark it as visited
                visited.add(vertex)
                
                #then add a PATH to neighbors to the back of the queue
                for v in self.get_neighbors(vertex):
                    #make a copy of the PATH
                    copy = list(path)
                    #append the neighbor to the back of the PATH
                    copy.append(v)
                    #enqueue out new PATH
                    queue.enqueue(copy)
        
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])

        visited = set()

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex not in visited:
                if vertex is destination_vertex:
                    return path

                visited.add(vertex)
                
                for v in self.get_neighbors(vertex):
                    copy = list(path)
                    copy.append(v)
                    stack.push(copy)
        
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        stack = Stack()
        stack.push([starting_vertex])
        
        if visited is None:
            visited = set()

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex not in visited:
                if vertex is destination_vertex:
                    return path

                visited.add(vertex)
                
                for v in self.get_neighbors(vertex):
                    copy = list(path)
                    copy.append(v)
                    stack.push(copy)
                
                self.dfs_recursive(vertex, destination_vertex, visited)
        
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
