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
    def search(self,dat):
        temp=self.head
        count=0
        c=0
        while temp!=None:
            if temp.data==dat:
                count+=1
                c=count
                print(count)
            temp=temp.next
            count+=1
        if c==0:
            print("not")
    def reverse(self):
        prev=None
        temp=self.head 
        while temp is not None: 
            tempv=temp.next
            temp.next=prev 
            prev=temp 
            temp=tempv
        self.head = prev
    def deleteFromStart(self):    
        if(self.head == None):    
            return;    
        else:    
            if(self.head != self.tail):    
                self.head = self.head.next;    
                self.head.previous = None;    
            else:    
                self.head = self.tail = None;    
if __name__=='__main__': 
    llist = LinkedList() 
    while(1):
        print("1.Insert\n2.Delete\n3.Search\n4.Reverse\n5.Exit")
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
            dat=int(input())
            llist.search(dat)
        if n==4:
            llist.reverse()
        if n==5:  
            llist.printList()
            exit()
