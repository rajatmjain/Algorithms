class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


def bfs(root: Node):
    sum = 0
    if(not root):
        return []
    queue = [root]
    while(len(queue)>0):
        current = queue.pop(0)
        sum += current.val
        if(current.left):
            queue.append(current.left)
        if(current.right):
            queue.append(current.right)
    return sum

def dfs(root: Node):
    if(not root.val):
        return []
    stack = [root]
    sum = 0
    while(len(stack)>0):
        current = stack.pop()
        sum += current.val
        if(current.right):
            stack.append(current.right)
        if(current.left):
            stack.append(current.left)
    return sum

def dfsRec(root:Node):
    if(not root.val):
        return []
    return root.val + dfsRec(root.left) + dfs(root.right)




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
# Sum = 36


print("Breadth First Sum")
print("Sum: ",bfs(a))
print()

print("Depth First Iter Sum")
print("Sum: ",dfs(a))
print()

print("Depth First Rec Sum")
print("Sum: ",dfs(a))
print()
  