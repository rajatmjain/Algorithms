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

def reverseIter(head:Node):
    previous = None
    current = head
    while(current!=None):
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def reverseRec(head:Node,previous):
    if(head==None):
        return previous
    next = head.next
    head.next = previous
    return reverseRec(next,head)

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

print("Recursive Reversal: ",end="")
traversalRec(reverseRec(a,None))

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

print("Iterative Reversal: ",end="")
traversalIter(reverseIter(a))