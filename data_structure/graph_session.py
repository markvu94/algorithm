graph_sample = {"a": ["c"],
                "b": ["c", "e"],
                "c": ["a", "b", "d", "e"],
                "d": ["c"],
                "e": ["c", "b"],
                "f": []
                }


class Graph:
    def __init__(self, graph_dict={}):
        self.graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def generate_edges(self):
        """ A static method generating the edges of the
            graph "graph".
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res

    # A function used by DFS
    def DFS_util(self, vertex, visited):

        # Mark the current node as visited
        visited.append(vertex)

        # Recursive for all the vertices adjacent to this vertex
        for i in self.graph_dict[vertex]:
            if i not in visited:
                self.DFS_util(i, visited)

                # The function to do DFS traversal. It uses

    # recursive DFSUtil()
    def DFS(self, vertex):

        # Mark all the vertices as not visited
        visited = []

        # Call the recursive helper function
        # to print DFS traversal
        self.DFS_util(vertex, visited)
        return visited

    # Function to print a BFS of graph
    def BFS(self, vertex):

        # Mark all the vertices as not visited
        visited = []

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(vertex)
        visited.append(vertex)

        while queue:

            # Dequeue a vertex from queue and print it
            vertex = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent
            # has not been visited, then mark it visited and enqueue it
            for i in self.graph_dict[vertex]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return visited

    def bfs_shortest_path(self, start, goal):
        # keep track of explored nodes
        explored = []
        # keep track of all the paths to be checked
        queue = [[start]]

        # return path if start is goal
        if start == goal:
            return "Start = goal"

        # keeps looping until all possible paths have been checked
        while queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in explored:
                neighbours = self.graph_dict[node]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = path[:]
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # return path if neighbour is goal
                    if neighbour == goal:
                        return new_path

                # mark node as explored
                explored.append(node)

        # in case there's no path between the 2 nodes
        return "So sorry, but a connecting path doesn't exist :("


g = Graph(graph_sample)
print(g)

print(g.DFS('a'))

print(g.BFS('a'))

print(g.bfs_shortest_path('a', 'e'))
