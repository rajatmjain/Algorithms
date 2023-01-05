class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


def bfs(root: Node):
    min = root.val
    if(not root):
        return []
    queue = [root]
    while(len(queue)>0):
        current = queue.pop(0)
        if(current.val<min):
            min = current.val
        if(current.left):
            queue.append(current.left)
        if(current.right):
            queue.append(current.right)
    return min

def dfs(root: Node):
    if(not root.val):
        return []
    stack = [root]
    min = root.val
    while(len(stack)>0):
        current = stack.pop()
        if(current.val<min):
            min = current.val
        if(current.right):
            stack.append(current.right)
        if(current.left):
            stack.append(current.left)
    return min

def dfsRec(root:Node):
    if(not root.val):
        return []
    return min(root.val,dfsRec(root.left),dfs(root.right))
    




# Nodes creation
a = Node(10)
b = Node(223)
c = Node(338)
d = Node(4)
e = Node(57)
f = Node(-8)
g = Node(7)
h = Node(999)
# Tree creation
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h

# Tree
#      10
#     / \
#    223 338
#   / \  / \
#   4 57-8  7
# /
# 999
# Min = -8


print("Breadth First Min")
print("Min: ",bfs(a))
print()

print("Depth First Iter Min")
print("Min: ",dfs(a))
print()

print("Depth First Rec Min")
print("Min: ",dfs(a))
print()
  