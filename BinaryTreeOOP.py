class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

print(root.data)
print(root.left.data)