r"""
Assessment 3.4: Non-linear Data Structure - Binary Tree
Name: Mikhael S. Labra | BSIT-2A | CC204 Data Structure and Algorithm

The user types a name. The letters are placed in the tree level by level,
left to right. Example for LABRA:

            L
          /   \
        A1     B
       /  \
      R    A2

If a letter repeats (like the two A's), the trace shows it as A1, A2, ...
so the nodes can be told apart. The final answer shows letters only.
"""
from collections import deque


class Node:
    def __init__(self, letter, name):
        self.letter = letter    # the letter shown in the diagram
        self.name = name        # unique name used in the trace (A1, A2, ...)
        self.left = None
        self.right = None


def build_tree(text):
    """Place the letters level by level, left to right."""
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    seen = {}
    nodes = []
    for ch in text:
        seen[ch] = seen.get(ch, 0) + 1
        name = f"{ch}{seen[ch]}" if counts[ch] > 1 else ch
        nodes.append(Node(ch, name))

    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0] if nodes else None


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
        print(f"  Step {step}: visit {node.name:<3} | queue = "
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
        print(f"  Step {step}: visit {node.name:<3} | stack (top on right) = "
              f"[{', '.join(n.name for n in stack)}]")
        step += 1
    return order


if __name__ == "__main__":
    text = input("Enter a name (letters only, e.g. LABRA): ")
    text = "".join(ch for ch in text.upper() if ch.isalpha())   # remove spaces, symbols

    if not text:
        print("No letters were entered.")
    else:
        root = build_tree(text)

        print("\nBINARY TREE -", text)
        print("\nBFS (Breadth-First Search)")
        bfs_order = bfs(root)
        print("BFS:", " - ".join(bfs_order))

        print("\nDFS (Depth-First Search)")
        dfs_order = dfs(root)
        print("DFS:", " - ".join(dfs_order))