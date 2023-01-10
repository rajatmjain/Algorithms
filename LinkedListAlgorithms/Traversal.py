class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

def traversal(head:Node):
    if(head.value==None):
        return
    print(head.value,end="->")
    if(head.next!=None):
        traversal(head.next)
    else:    
        print("None")



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e

traversal(a)