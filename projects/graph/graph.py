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
        neighbors = []
        for neighbor in self.vertices[vertex_id]:
            neighbors.append(neighbor)
        return neighbors

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
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
                # print("self.get_neighbors(v)", self.get_neighbors(v))
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
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        print(result)
        print("------")

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if starting_vertex is None:
        #     return
        # self.dft_recursive(self.vertices[starting_vertex])
        # print(self.vertices[starting_vertex])

        # print(self.vertices[starting_vertex])
        # self.dft_recursive()

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
            print("p", p)
            # grab the last vertex from the PATH
            v = p[-1]
            # print("v", v)
            # if that vertex has not been visited:
            if v not in visited:
                # CHECK IF IT"S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return p
                # mark it as visited
                visited.add(v)
                # then add A PATH TO its neighbors to the back of the queue
                # new_path = p
                # print("type(p)", type(p))

                for neighbor in self.vertices[v]:
                    # new_path.append(neighbor)
                # q.enqueue(new_path)
                    print("neighbor", neighbor)
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path = list(p)
                    # print("new_path", new_path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                print("q.queue", q.queue)
        print("------")

        ###########################

        # q = Queue()
        # q.enqueue([starting_vertex])
        # visited = set()

        # whirsle q.size() > 0:
        #     u = q[0]
        #     print("u", u)
        #     # for v of u.neighbo


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    # graph.dft_recursive(1)

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
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
