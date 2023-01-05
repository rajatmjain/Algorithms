class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


visitedOrder = []
def dfs(root: Node):
    if(not root):
        return []
    visitedOrder.append(root.val)   
    dfs(root.left)
    dfs(root.right)

    return visitedOrder

  
  

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h

print("Depth First Search")
print("Visited in order: ",dfs(a))