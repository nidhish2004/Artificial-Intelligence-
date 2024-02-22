class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, node, adjacent):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(adjacent)
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("BFS Traversal:")
    g.bfs(2)  # Starting BFS from vertex 2
