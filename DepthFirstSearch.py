class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


def dfs(root: Node):
    stack = [root]
    visited = []
    while(len(stack)>0):
        current = stack.pop()
        visited.append(current.val)
        if(current.right):
            stack.append(current.right)
        if(current.left):
            stack.append(current.left)
    
    return visited

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
print(dfs(a))





        