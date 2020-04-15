class Node: 
    def __init__(self, data): 
        self.info = data 
        self.next = None
        self.prev = None
head = None
tail = None
def nodeInsetail( key) : 
    global head 
    global tail 
    p = Node(key) 
    p.next = None
    if ((head) == None) : 
        (head) = p 
        (tail) = p 
        (head).prev = None
        return
    if ((p.info) < ((head).info)) : 
        p.prev = None
        (head).prev = p 
        p.next = (head) 
        (head) = p 
        return
    if ((p.info) > ((tail).info)) : 
        p.prev = (tail) 
        (tail).next = p 
        (tail) = p 
        return
    temp = (head).next
    while ((temp.info) < (p.info)) : 
        temp = temp.next
    (temp.prev).next = p 
    p.prev = temp.prev 
    temp.prev = p 
    p.next = temp 
def printList(temp) : 
    while (temp != None) : 
        print( temp.info, end = " ") 
        temp = temp.next
nodeInsetail( 6) 
nodeInsetail( 5) 
nodeInsetail( 4) 
print("Doubly linked list on printing from left to right\n" ) 
printList(head) 

//4 5 6
//6 5 4
