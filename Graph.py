r"""
Assessment 3.4: Non-linear Data Structure - Graph
Name: Mikhael S. Labra | BSIT-2A | CC204 Data Structure and Algorithm

The user types a name. Each letter becomes a vertex, placed level by level,
left to right. Each vertex is connected by an edge to its parent above it.
Example for LABRA:

  Vertices: L, A1, B, R, A2
  Edges:    L-A1, L-B, A1-R, A1-A2

            L
          /   \
        A1     B
       /  \
      R    A2

If a letter repeats (like the two A's), the trace shows it as A1, A2, ...
so the vertices can be told apart. The final answer shows letters only.
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
            print(f"  Step {step}: visit {v:<3} | queue = [{', '.join(queue)}]")
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
            print(f"  Step {step}: visit {v:<3} | stack (top on right) = "
                  f"[{', '.join(stack)}]")
            step += 1
        return order


def build_graph(text):
    """One vertex per letter (level by level); each vertex joins its parent."""
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    seen = {}
    names = []
    g = Graph()
    for ch in text:
        seen[ch] = seen.get(ch, 0) + 1
        name = f"{ch}{seen[ch]}" if counts[ch] > 1 else ch
        names.append(name)
        g.add_vertex(name, ch)

    for i in range(1, len(names)):
        g.add_edge(names[(i - 1) // 2], names[i])    # parent - child
    return g, names


if __name__ == "__main__":
    text = input("Enter a name (letters only, e.g. LABRA): ")
    text = "".join(ch for ch in text.upper() if ch.isalpha())   # remove spaces, symbols

    if not text:
        print("No letters were entered.")
    else:
        g, names = build_graph(text)
        start = names[0]

        print("\nGRAPH -", text)
        print("\nAdjacency list")
        for v, neighbors in g.adj.items():
            print(f"  {v:<3} -> {', '.join(neighbors) if neighbors else '(none)'}")

        print(f"\nBFS (Breadth-First Search) starting at {start}")
        print("BFS:", " - ".join(g.bfs(start)))

        print(f"\nDFS (Depth-First Search) starting at {start}")
        print("DFS:", " - ".join(g.dfs(start)))