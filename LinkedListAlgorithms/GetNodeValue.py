class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

def traversalRec(head:Node,atIndex,currentIndex):
    if(head==None):
        return None
    if(currentIndex==atIndex):
        return head.value
    if(head.next!=None):
        return traversalRec(head.next,atIndex,currentIndex+1)  


def traversalIter(head:Node,atIndex):
    index = 0
    while(head!=None):
        if(index==atIndex):
            return head.value
        head = head.next
        index += 1
    return None

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

print("Node at 2 Recur: ",traversalRec(a,2,0))
print("Node at 3 Iter: ",traversalIter(a,3))
