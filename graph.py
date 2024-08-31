class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """Добавляет вершину в граф."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Добавляет ребро между двумя вершинами."""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def dfs(self, start, visited=None):
        """Обход графа в глубину (DFS)."""
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        """Обход графа в ширину (BFS)."""
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Пример использования:
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

print("DFS:")
g.dfs('A')  # A B D C E
print("\nBFS:")
g.bfs('A')  # A B C D E
