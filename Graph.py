"""
Assessment 3.4: Non-linear Data Structure - Graph (LABRA)
Name: Mikhael S. Labra | BSIT-2A | CC204 Data Structure and Algorithm

Graph built from the last name L-A-B-R-A:

  Vertices: L, A1, B, R, A2     (A1 and A2 are both the letter A)
  Edges:    L-A1, L-B, A1-R, A1-A2

            L
          /   \
        A1     B
       /  \
      R    A2
"""
from collections import deque


class Graph:
    def __init__(self):
        self.letters = {}      # vertex name -> letter shown in the diagram
        self.adj = {}          # adjacency list: vertex name -> list of neighbors

    def add_vertex(self, name, letter=None):
        self.letters[name] = letter or name
        self.adj[name] = []

    def add_edge(self, u, v):
        self.adj[u].append(v)  # undirected graph: store the edge both ways
        self.adj[v].append(u)

    def bfs(self, start):
        """Breadth-First Search: QUEUE + visited set."""
        visited = {start}
        queue = deque([start])
        order, step = [], 1
        while queue:
            v = queue.popleft()                      # dequeue the front vertex
            order.append(self.letters[v])            # visit it
            for w in self.adj[v]:
                if w not in visited:
                    visited.add(w)                   # mark when enqueued
                    queue.append(w)
            print(f"  Step {step}: visit {v:<2} | queue = [{', '.join(queue)}]")
            step += 1
        return order

    def dfs(self, start):
        """Depth-First Search: STACK + visited set."""
        visited = set()
        stack = [start]
        order, step = [], 1
        while stack:
            v = stack.pop()                          # pop the top vertex
            if v in visited:
                continue
            visited.add(v)                           # mark when visited
            order.append(self.letters[v])            # visit it
            for w in reversed(self.adj[v]):          # reversed so the first
                if w not in visited:                 # neighbor is popped first
                    stack.append(w)
            print(f"  Step {step}: visit {v:<2} | stack (top on right) = "
                  f"[{', '.join(stack)}]")
            step += 1
        return order


def build_graph():
    g = Graph()
    for name, letter in [("L", "L"), ("A1", "A"), ("B", "B"),
                         ("R", "R"), ("A2", "A")]:
        g.add_vertex(name, letter)
    g.add_edge("L", "A1")
    g.add_edge("L", "B")
    g.add_edge("A1", "R")
    g.add_edge("A1", "A2")
    return g


if __name__ == "__main__":
    g = build_graph()

    print("GRAPH - LABRA")
    print("\nAdjacency list")
    for v, neighbors in g.adj.items():
        print(f"  {v:<2} -> {', '.join(neighbors)}")

    print("\nBFS (Breadth-First Search) starting at L")
    print("BFS:", " - ".join(g.bfs("L")))

    print("\nDFS (Depth-First Search) starting at L")
    print("DFS:", " - ".join(g.dfs("L")))