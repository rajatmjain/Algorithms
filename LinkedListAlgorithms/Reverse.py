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

def reverse(head:Node):
    previous = None
    current = head
    while(current!=None):
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous




# LinkedList Creation
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e

# Linked List : a->b->c->d->e

# print("Recursive Traversal: ",end="")
# traversalRec(a)
print("Iterative Traversal: ",end="")
traversalIter(reverse(a))