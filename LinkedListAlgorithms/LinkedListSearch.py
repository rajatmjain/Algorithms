class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


def searchIter(head:Node,toSearch):
    while(head!=None):
        if(head.value==toSearch):
            return True
        head = head.next
    return False

def searchRec(head:Node,toSearch):
    if(head==None):
        return
    if(head.value == toSearch):
        return True
    if(head.next!=None):
        if(searchRec(head.next,toSearch)):
            return True
    return False
    
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

print("Found 'c' Iter: ",searchIter(a,'c'))
print("Found 'r' Rec: ",searchRec(a,'r'))