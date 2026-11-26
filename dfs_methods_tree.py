r"""
Assessment 3.6: DFS Methods in Tree
Name: Mikhael S. Labra | BSIT-2A | CC204 Data Structure and Algorithm

The user types a first name and last name. The letters are placed in a binary
tree level by level, left to right (same way as the LABRA tree).
Example for MIKHAEL LABRA:

                      M(1)
              /                \
          I(2)                  K(3)
        /      \              /      \
     H(4)      A(5)        E(6)      L(7)
    /   \      /   \       /
  L(8) A(9)  B(10) R(11) A(12)

The number in brackets is the node's position. It only tells apart the
repeated letters (there are three A's and three L's).

DFS methods:
    Preorder  : Root -> Left -> Right
    Inorder   : Left -> Root -> Right
    Postorder : Left -> Right -> Root
"""


class Node:
    def __init__(self, letter, position):
        self.letter = letter
        self.position = position      # level-order position (1, 2, 3, ...)
        self.left = None
        self.right = None

    def label(self):
        return f"{self.letter}({self.position})"


def build_tree(text):
    """Place the letters level by level, left to right."""
    nodes = [Node(ch, i + 1) for i, ch in enumerate(text)]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0] if nodes else None


def preorder(node, visited):
    """Root -> Left -> Right"""
    if node is None:
        return
    visited.append(node)              # visit the root first
    preorder(node.left, visited)      # then the whole left subtree
    preorder(node.right, visited)     # then the whole right subtree


def inorder(node, visited):
    """Left -> Root -> Right"""
    if node is None:
        return
    inorder(node.left, visited)       # the whole left subtree first
    visited.append(node)              # then the root
    inorder(node.right, visited)      # then the whole right subtree


def postorder(node, visited):
    """Left -> Right -> Root"""
    if node is None:
        return
    postorder(node.left, visited)     # the whole left subtree first
    postorder(node.right, visited)    # then the whole right subtree
    visited.append(node)              # the root last


def show(title, method, root):
    visited = []
    method(root, visited)
    print(title)
    for step, node in enumerate(visited, 1):
        print(f"  Step {step:>2}: visit {node.label()}")
    print(title.split()[0] + ":", " - ".join(n.letter for n in visited))
    print()


if __name__ == "__main__":
    text = input("Enter your first name and last name (e.g. MIKHAEL LABRA): ")
    text = "".join(ch for ch in text.upper() if ch.isalpha())   # remove spaces, symbols

    if not text:
        print("No letters were entered.")
    else:
        root = build_tree(text)

        print("\nDFS METHODS IN BINARY TREE -", text)
        print()
        show("Preorder (Root - Left - Right)", preorder, root)
        show("Inorder (Left - Root - Right)", inorder, root)
        show("Postorder (Left - Right - Root)", postorder, root)