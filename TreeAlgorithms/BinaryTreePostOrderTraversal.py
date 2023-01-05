class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

visitedOrder = []
def postorder(root:Node):
    if(root is None):
        return []

    postorder(root.left)
    postorder(root.right)
    visitedOrder.append(root.val)
    return visitedOrder
    
     

# Nodes creation
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
# Tree creation
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h

# Tree
#      1
#     / \
#    2   3
#   / \  / \
#   4  5 6  7
# /
# 8

print("Post-Order: ",postorder(a))
print()