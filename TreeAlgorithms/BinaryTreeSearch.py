class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


def bfs(root: Node,toSearchVal:any):
    visitedOrder = []
    if(not root):
        return []
    if(toSearchVal=='' or toSearchVal==None):
        return False
    queue = [root]
    while(len(queue)>0):
        current = queue.pop(0)
        if(current.val==toSearchVal):
            return True
        visitedOrder.append(current.val)
        if(current.left):
            queue.append(current.left)
        if(current.right):
            queue.append(current.right)
    return False

def dfs(root: Node,toSearchVal:any):
    if(not root.val):
        return []
    if(toSearchVal=='' or toSearchVal==None):
        return False
    stack = [root]
    visitedOrder = []
    while(len(stack)>0):
        current = stack.pop()
        if(current.val==toSearchVal):
            return True
        visitedOrder.append(current.val)
        if(current.right):
            stack.append(current.right)
        if(current.left):
            stack.append(current.left)
    return False



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

testCases = ['f','h','r','t','a','',None]

for tc in testCases:
    print("Breadth First Search")
    print("Search result for {}: ".format(tc),bfs(a,tc))
    print()

    print("Depth First Search")
    print("Search result for {}: ".format(tc),dfs(a,tc))
    print()
  