class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


def dfs(root: Node):
    if(not root.val):
        return []
    stack = [root]
    visitedOrder = []
    while(len(stack)>0):
        current = stack.pop()
        visitedOrder.append(current.val)
        if(current.right):
            stack.append(current.right)
        if(current.left):
            stack.append(current.left)
    
    return visitedOrder

# Nodes creation
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
# Tree creation
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h

# Tree
#      a
#     / \
#    b   c
#   / \  / \
#   d  e f  g
# /
# h

print("Depth First Traversal")
print("Visited in order: ",dfs(a))





        