class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None 
class LinkedList: 
    def __init__(self): 
        self.head = None
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data), 
            temp = temp.next
if __name__=='__main__': 
    llist = LinkedList() 
    while(1):
        print("1.Insert\n2.Delete\n3.Exit")
        n=int(input())
        if n==1:
            if llist.head==None:
                llist.head=Node(int(input()))
                llist.last = llist.head 
            else:
                llist.last.next=Node(int(input()))
                llist.last=llist.last.next
        if n==2:
            n=int(input())
            temp=llist.head
            if temp is not None:
                if temp.data==n:
                    llist.head=temp.next
                    temp=None
                    llist.printList()
            while temp is not None: 
                if temp.data==n: 
                    break
            pre=temp 
            temp=temp.next
            if temp==None: 
                llist.printList()
            pre.next=temp.next
            temp = None
        if n==3:
            llist.printList()
            exit()
    
  
    
