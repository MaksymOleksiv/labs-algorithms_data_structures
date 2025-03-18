import unittest
from main import find_successor, BinaryTree



class TestFindSuccessor(unittest.TestCase):
    """
      10
     /   \
     5   15
    / \   \
    3  7   20
          /
         12

    """
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.left.parent = root
    root.left.left = BinaryTree(3)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(7)
    root.left.right.parent = root.left
    root.right = BinaryTree(15)
    root.right.parent = root
    root.right.right = BinaryTree(20)
    root.right.right.parent = root.right
    root.right.right.left = BinaryTree(12)
    root.right.right.left.parent = root.right.right

    def test_find_successor(self):
        self.assertEqual(find_successor(self.root, self.root.left.right), self.root)  # 7 = 10
        self.assertEqual(find_successor(self.root, self.root.right.right), None)  # 20 = None
        self.assertEqual(find_successor(self.root, self.root.right.right.left), self.root.right.right)  # 12 = 20