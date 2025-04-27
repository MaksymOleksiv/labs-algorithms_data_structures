class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty() or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
