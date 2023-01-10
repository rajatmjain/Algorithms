class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

def traversalRec(head:Node):
    if(head==None):
        return
    print(head.value,end="->")
    if(head.next!=None):
        traversalRec(head.next)
    else:    
        print("None")

def traversalIter(head:Node):
    while(head!=None):
        print(head.value,end="->")
        head = head.next
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


print("Recursive Traversal: ",end="")
traversalRec(a)
print("Iterative Traversal: ",end="")
traversalIter(a)