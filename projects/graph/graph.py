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
        if v1 not in self.vertices and v2 not in self.vertices:
            raise IndexError("v1 and v2 vertices do not exist")
        elif v1 in self.vertices and v2 not in self.vertices:
            raise IndexError("v2 vertex does not exist.")
        elif v2 in self.vertices and v1 not in self.vertices:
            raise IndexError("v1 vertex does not exist")
        else:
            self.vertices[v1].add(v2)
            

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # neighbors = []
        # for neighbor in self.vertices[vertex_id]:
        #     neighbors.append(neighbor)
        # return neighbors

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print("bft: ")
        result = []
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # create an empty set to store visited vertices
        visited = set()
        # while the queue is not empty:
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been visited:
            if v not in visited:
                # mark it as visited
                result.append(v)
                visited.add(v)
                # then add all of its neighbors to the back of the queue
                # for neighbor in self.vertices[v]:
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
        print(result)
        print("------")

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print("dft: ")
        result = []
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # create an empty set to store visited vertices
        visited = set()
        # while the stack is not empty:
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited:
            if v not in visited:
                # mark it as visited
                result.append(v)
                visited.add(v)
                # then add all of its neighbors to the back of the stack
                # for neighbor in self.vertices[v]:
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
        print(result)
        print("------")

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if starting_vertex is None:
        #     return
        # visited = set()
        # print(starting_vertex)
        # if starting_vertex not in visited:
        #     # print(self.vertices[starting_vertex])
        #     # print(self.vertices[2])
        #     visited.add(starting_vertex)
        #     for n in self.vertices[starting_vertex]:
        #         # print(n)
        #         self.dft_recursive(self.vertices[n])

        #######################
        # check if visited has been initialized
        if visited is None:
            visited = set()
        # mark the node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
        # call dft_recursive on each neighbor that has not been visited
        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print("bfs: ")
        # create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty:
        while q.size() > 0:
            # dequeue the first PATH\
            p = q.dequeue()
            # grab the last vertex from the PATH
            v = p[-1]
            # if that vertex has not been visited:
            if v not in visited:
                # CHECK IF IT"S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return p
                # mark it as visited
                visited.add(v)
                # then add A PATH TO its neighbors to the back of the queue
                # for neighbor in self.vertices[v]:
                for neighbor in self.get_neighbors(v):
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path = list(p)
                    # new_path = path.copy()
                    new_path.append(neighbor)
                    q.enqueue(new_path)
        print("------")


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print("dfs: ")
        # create an empty queue and enqueue A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty:
        while s.size() > 0:
            # dequeue the first PATH\
            p = s.pop()
            # grab the last vertex from the PATH
            v = p[-1]
            # if that vertex has not been visited:
            if v not in visited:
                # CHECK IF IT"S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return p
                # mark it as visited
                visited.add(v)
                # then add A PATH TO its neighbors to the back of the queue
                # for neighbor in self.vertices[v]:
                for neighbor in self.get_neighbors(v):
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path = list(p)
                    # new_path = path.copy()
                    new_path.append(neighbor)
                    s.push(new_path)
        print("------")

    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # init visited
        if visited == None:
            visited = set()
        # init path
        if path is None:
            path = []
        # add vertex to path
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # if we are at the target, return the path'
        if starting_vertex == target_vertex:
            return path
        # othwerise, call dfs_recursive on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, target_vertex, visited, path)
                if new_path is not None:
                    return new_path
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

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    graph.dft(1)
    print("dft_recursive: ")
    graph.dft_recursive(1)
    print("------")

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    print("dfs_recursive: ")
    print(graph.dfs_recursive(1, 6))
