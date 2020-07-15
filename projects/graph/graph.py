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
        if vertex_id in self.vertices:
            raise KeyError(f'vertex {vertex_id} has already been added')
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            raise IndexError(f'vertex {v1} and/or {v2} not in vertices')
        else:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            raise IndexError(f'vertex {vertex_id} does not exist')
        else:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make a set to track if we have been here before
        visited = set()
        # while our queue is not empty
        while q.size() > 0:
            # dequeue whatever is in the front of our line, this is our current node
            curr = q.dequeue()
        # if we have not visited this node yet,
            if curr not in visited:
                # mark as visited
                print(curr)
                visited.add(curr)
        # get its neighbors
                neighbors = self.get_neighbors(curr)
        # for each of its neighbors
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we have been here before
        visited = set()
        # while our stack is not empty
        while s.size() > 0:
            # pop off whatever is on top, this is current node
            curr = s.pop()
            # if we have not visited this node yet,
            if curr not in visited:
                # mark as visited
                print(curr)
                visited.add(curr)
        # get its neighbors
                neighbors = self.get_neighbors(curr)
        # for each of its neighbors
                for neighbor in neighbors:
                    # add to stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # enqueue a PATH to the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty:
        while q.size() > 0:
            # Dequeue the first PATH and set it to current
            curr = q.dequeue()
            # Grab the last vertex from the PATH
            vertex = curr[-1]
            # If that vertex has not been visited:
            if vertex not in visited:
                # Check if it's the target
                if vertex == destination_vertex:
                    # Return PATH
                    return curr
                # Mark as visited
                visited.add(vertex)
                # Add a PATH to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    # Copy path because different paths are added
                    path = curr.copy()
                    # Append neighbor - append returns None
                    path.append(neighbor)
                    q.enqueue(path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        s = Stack()
        # push a PATH to the starting vertex
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop and set it to current
            curr = s.pop()
            # Grab last vertex from the PATH
            vertex = curr[-1]
            # If that vertex has not been visited
            if vertex not in visited:
                # Check if it is the target
                if vertex == destination_vertex:
                    # Return PATH
                    return curr
                # Mark as visited and add to stack
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    path = curr.copy()
                    path.append(neighbor)
                    s.push(path)

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # mark node as visited
        visited.add(vertex)
        # check if it is our target node, if so return
        if vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)
        # iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        # check if visited
        for neighbor in neighbors:
            if neighbor not in visited:
                # if not, recurse
                res = self.dfs_recursive(
                    neighbor, destination_vertex, path + [neighbor], visited)
        # if recursion returns path
                if res is not None:
                    # return from here
                    return res


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
