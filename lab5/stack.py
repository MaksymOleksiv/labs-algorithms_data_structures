class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'<{self.data}>'


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        el = self.top.data
        self.top = self.top.next
        return el

    def isEmpty(self):
        return self.top is None

    def __str__(self):
        arr = [self.top.data]
        next_node = self.top.next
        while next_node is not None:
            arr.append(next_node.data)
            next_node = next_node.next
        return str(arr)
