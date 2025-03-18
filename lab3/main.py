class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor

    successor = node.parent
    while successor and successor.right == node:
        node = successor
        successor = successor.parent
    return successor
