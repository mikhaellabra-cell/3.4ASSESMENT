"""
Assessment 3.4: Non-linear Data Structure - Binary Tree (LABRA)
Name: Mikhael S. Labra | BSIT-2A | CC204 Data Structure and Algorithm

Tree built from the last name L-A-B-R-A:

            L
          /   \
        A1     B
       /  \
      R    A2

(A1 and A2 are both the letter A; the numbers only tell the two nodes apart.)
"""
from collections import deque


class Node:
    def __init__(self, letter, name=None):
        self.letter = letter          # the letter shown in the diagram
        self.name = name or letter    # unique name used in the trace (A1, A2)
        self.left = None
        self.right = None


def build_tree():
    root = Node("L")
    root.left = Node("A", "A1")
    root.right = Node("B")
    root.left.left = Node("R")
    root.left.right = Node("A", "A2")
    return root


def bfs(root):
    """Breadth-First Search: visit level by level using a QUEUE (FIFO)."""
    order = []
    if root is None:
        return order
    queue = deque([root])
    step = 1
    while queue:
        node = queue.popleft()                       # dequeue the front node
        order.append(node.letter)                    # visit it
        if node.left:
            queue.append(node.left)                  # enqueue left child
        if node.right:
            queue.append(node.right)                 # enqueue right child
        print(f"  Step {step}: visit {node.name:<2} | queue = "
              f"[{', '.join(n.name for n in queue)}]")
        step += 1
    return order


def dfs(root):
    """Depth-First Search (preorder): go deep first using a STACK (LIFO)."""
    order = []
    if root is None:
        return order
    stack = [root]
    step = 1
    while stack:
        node = stack.pop()                           # pop the top node
        order.append(node.letter)                    # visit it
        if node.right:
            stack.append(node.right)                 # push right first ...
        if node.left:
            stack.append(node.left)                  # ... so left is popped first
        print(f"  Step {step}: visit {node.name:<2} | stack (top on right) = "
              f"[{', '.join(n.name for n in stack)}]")
        step += 1
    return order


if __name__ == "__main__":
    root = build_tree()

    print("BINARY TREE - LABRA")
    print("\nBFS (Breadth-First Search)")
    bfs_order = bfs(root)
    print("BFS:", " - ".join(bfs_order))

    print("\nDFS (Depth-First Search)")
    dfs_order = dfs(root)
    print("DFS:", " - ".join(dfs_order))