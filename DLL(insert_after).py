class Node:   
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAfter(self, node, data):
        runner = Node(None, data, node, None)
        runner.next = self.head
        if self.head is not None:
            self.head.prev = runner
        self.head = runner
    def addLast(self, data):
        if self.head is not None:
            runner = self.head
            while(runner.next != None):
                runner = runner.next
            runner.next = Node(data, None, runner)
            self.tail = runner.next
        else:
            self.head = Node(data)
            self.tail = self.head
    def Print_Next_List(self): # Traverse forwards
        runner = self.head
        while (runner is not None):
            print(runner.data) 
            runner = runner.next

    def Print_Prev_List(self): # Traverse Backwards
        runner = self.tail
        while (runner is not None):
            print(runner.data)
            runner = runner.prev

aList = Doubly_Linked_List()

aList.addLast(3)
aList.addLast(5)
aList.addLast(7)
aList.addLast(9)
aList.addLast(11)

aList.Print_Next_List()
print()
aList.Print_Prev_List()

//3 5 7 9 11
//11 9 7 5 3
