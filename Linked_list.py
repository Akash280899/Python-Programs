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
    def insert(self):
        if llist.head==None:
            llist.head=Node(int(input()))
            llist.last = llist.head 
        else:
            llist.last.next=Node(int(input()))
            llist.last=llist.last.next
    def deletehead(self):
        temp=self.head
        while temp:
            temp=temp.next
            self.head=temp
            break
    def deletelast(self):
        if self.head == None: 
            return None
        if self.head.next == None: 
            self.head = None
            return None
        second_last = self.head 
        while(second_last.next.next): 
            second_last = second_last.next
        second_last.next = None
        llist.last=second_last
        return self.head
    def deletepos(self,pos):
        temp = self.head
        dcount=0
        while(temp):
            dcount-=-1
            if(dcount==pos-1):
                tempf=temp
            if(dcount == pos+1):
                temph = temp
                tempf.next=temph
                break
            temp = temp.next
if __name__=='__main__': 
    llist = LinkedList() 
    while(1):
        print("1.Insert\n2.Delete\n3.Exit")
        n=int(input())
        if n==1:
            llist.insert()
        if n==2:
            print("1.Head\n2.Position\n3.Last")
            n=int(input())
            if n==1:
                llist.deletehead()
            if n==2:
                pos=int(input())
                llist.deletepos(pos)
            if n==3:
                print(llist.deletelast())
        if n==3:
            llist.printList()
            exit()
