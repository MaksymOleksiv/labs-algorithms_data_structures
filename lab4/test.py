from binary_tree_priority_queue import Node, RedBlackTree

tree_data = {
    50: 10,
    30: 20,
    70: 5,
    20: 25,
    40: 15,
    60: 8,
    80: 3,
    10: 30,
    25: 22,
    35: 18,
    38: 18,
}

rb_tree = RedBlackTree()
for key, priority in tree_data.items():
    rb_tree.insert(key, priority)


print("View queue:")
for i in rb_tree.view_queue():
    print(i, end="\t\t")

print()

print("Pop elements:")
print(rb_tree.pop())
print(rb_tree.pop())

print("View queue after pop:")
for i in rb_tree.view_queue():
    print(i, end="\t\t")

