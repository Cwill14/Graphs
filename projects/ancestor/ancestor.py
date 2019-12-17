# from util import Queue
# from graph import Graph
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

        
def earliest_ancestor(ancestors, starting_child):
    graph = Graph()
    for a in ancestors:
        graph.add_vertex(a[0])
        graph.add_vertex(a[1])
        graph.add_edge(a[1], a[0])

    q = Queue()
    q.enqueue([starting_child])
    max_length = 1
    current_earliest_ancestor = -1
    while q.size() > 0:
        p = q.dequeue()
        v = p[-1]
        print("------")
        print("len(p): ", len(p))
        print("max_length: ", max_length)
        print("v: ", v)
        print("current_earliest_ancestor: ", current_earliest_ancestor)
        if (len(p) >= max_length and v < current_earliest_ancestor) or (len(p) > max_length):
            current_earliest_ancestor = v
            max_length = len(p)

        for neighbor in graph.vertices[v]:
            new_path = list(p)
            new_path.append(neighbor)
            q.enqueue(new_path)

    return current_earliest_ancestor
# def earliest_ancestor(ancestors, starting_node):
#     # Build the graph
#     graph = Graph()
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # Build edges in reverse
#         graph.add_edge(pair[1], pair[0])
#     # Do a BFS (storing the path)
#     q = Queue()
#     q.enqueue([starting_node])
#     max_path_len = 1
#     earliest_ancestor = -1
#     while q.size() > 0:
#         path = q.dequeue()
#         v = path[-1]
#         # If the path is longer or equal and the value is smaller, or if the path is longer)
#         if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
#             earliest_ancestor = v
#             max_path_len = len(path)
#         for neighbor in graph.vertices[v]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)
#     return earliest_ancestor
    


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print("earliest_ancestor(test_ancestors, 6) = ", earliest_ancestor(test_ancestors, 6))