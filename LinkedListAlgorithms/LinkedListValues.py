class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


def traversalIter(head:Node):
    values = []
    while(head!=None):
        values.append(head.value)
        head = head.next
    return values

def traversalRec(head:Node,values:list):
    if(head==None):
        return
    values.append(head.value)
    if(head.next!=None):
        traversalRec(head.next,values)
    return values
    
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

print("Values Iter: ",traversalIter(a))
print("Values Rec: ",traversalRec(a,[]))