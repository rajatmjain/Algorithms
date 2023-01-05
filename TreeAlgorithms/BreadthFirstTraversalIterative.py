class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


def bfs(root: Node):
    visitedOrder = []
    if(not root):
        return []
    queue = [root]
    while(len(queue)>0):
        current = queue.pop(0)
        visitedOrder.append(current.val)
        if(current.left):
            queue.append(current.left)
        if(current.right):
            queue.append(current.right)
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

print("Breadth First Traversal")
print("Visited in order: ",bfs(a))





        