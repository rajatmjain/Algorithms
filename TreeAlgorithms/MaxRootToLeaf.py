class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def dfsRec(root:Node):
    if(root is None):
        return float('-inf')
    if(not root.left and not root.right):
        return root.val
    sum = root.val
    return sum + max(dfsRec(root.left),dfsRec(root.right)) 

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
# Max = 15

print("Depth First Rec Max Root to Leaf")
print("Max Root to Leaf: ",dfsRec(a))
print()
  