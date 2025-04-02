class Node:
    def __init__(self, key, priority, color='R'):
        self.key = key
        self.color = color  # 'R' - червоний, 'B' - чорний
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"<{self.key}: {self.priority}>"


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, color='B')  # NIL-нод (листки чорні)
        self.root = self.NIL
        self.__view_res = []

    def insert(self, key, priority):
        new_node = Node(key, priority)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.priority > current.priority:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.priority > parent.priority:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'R'
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == 'R':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'B'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def _inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node != self.NIL:
            self._inorder_traversal(node.left)
            self.__view_res.append(node)
            self._inorder_traversal(node.right)

    def view_queue(self):
        self._inorder_traversal(self.root)
        res = self.__view_res
        self.__view_res = []
        return res

    def find_max_priority(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def pop(self):
        min_node = self.find_max_priority(self.root)
        if min_node != self.NIL:
            self._delete(min_node)

    def _delete(self, node):
        original_color = node.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self.find_max_priority(node.right)
            original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if original_color == 'B':
            self._fix_delete(x)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _fix_delete(self, node):
        while node != self.root and node.color == 'B':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'R':
                    sibling.color = 'B'
                    node.parent.color = 'R'
                    self._left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'B' and sibling.right.color == 'B':
                    sibling.color = 'R'
                    node = node.parent
                else:
                    if sibling.right.color == 'B':
                        sibling.left.color = 'B'
                        sibling.color = 'R'
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'B'
                    sibling.right.color = 'B'
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'R':
                    sibling.color = 'B'
                    node.parent.color = 'R'
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'B' and sibling.left.color == 'B':
                    sibling.color = 'R'
                    node = node.parent
                else:
                    if sibling.left.color == 'B':
                        sibling.right.color = 'B'
                        sibling.color = 'R'
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'B'
                    sibling.left.color = 'B'
                    self._right_rotate(node.parent)
                    node = self.root
        node.color = 'B'
