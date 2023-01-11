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

def zipperRec(list1:Node,list2:Node):
    if(list1==None and list2==None):
        return None

    if(list2==None):
        return list1
    
    if(list1==None):
        return list2
    
    nextList1 = list1.next
    nextList2 = list2.next
    list1.next = list2
    list2.next = zipperRec(nextList1,nextList2)
    return list1
    

def zipperIter(list1:Node,list2:Node):
    tail = list1
    currentList1 = list1.next
    currentList2 = list2
    count = 0
    while(currentList1!=None and currentList2!=None):
        if(count%2==0):
            tail.next = currentList2
            currentList2 = currentList2.next
        else:
            tail.next = currentList1
            currentList1 = currentList1.next

        tail = tail.next
        count += 1

    if(currentList2!=None):
        tail.next = currentList2
    
    if(currentList1!=None):
        tail.next = currentList1 
    return list1
    
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


# LinkedList Creation
f = Node(1)
g = Node(2)
h = Node(3)
i = Node(4)
j = Node(5)
f.next = g
g.next = h
h.next = i
i.next = j

# Linked List : 1->2->3->4->5

traversalIter(zipperIter(a,f))
#traversalRec(zipperRec(a,f))