class Node: 
    def __init__(self, data=None,head=None): 
        self.data = data  
        self.next = None 
class linkedlist:
    def __init__(self): 
        self.head = None
        data=None
        position=None
    def insert(self):
        if llist.head==None:
            llist.head=Node(int(input()))
            llist.last = llist.head 
        else:
            llist.last.next=Node(int(input()))
            llist.last=llist.last.next
    def insertpos(self):
        position=int(input())
        data=int(input())
        if position == 0:
            return Node(data,head)
        
        top = self.head
        prev = Node()
        new_node = Node(data,None)
        count = 0
        while top:
            count += 1
            prev = top
            top = top.next
        
            if count == position :
                prev.next = new_node
                new_node.next = top
                return self.head  
if __name__=='__main__': 
    llist = linkedlist() 
#    input from user
    llist.insertpos()
    llist.printlist()
