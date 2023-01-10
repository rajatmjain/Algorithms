class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


def traversalIter(head:Node):
    sum = 0
    while(head!=None):
        sum += head.value
        head = head.next
    return sum

def traversalRec(head:Node):
    if(head==None):
        return 0
    return head.value + traversalRec(head.next)
    
# LinkedList Creation
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e

# Linked List : 1->2->3->4->5

print("Sum of list Iter: ",traversalIter(a))
print("Sum of list Recur: ",traversalRec(a))