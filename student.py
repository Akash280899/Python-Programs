class student:
    def __init__(self,no,name,s1,s2,s3,s4,s5):
        self.no=no
        self.name=name
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
    def total(self):
        tot=self.s1+self.s2+self.s3+self.s4+self.s5
        self.tot=tot
        #l.append(self.tot)
    def average(self):
        avg=self.tot/5
        self.avg=avg
        #l.append(self.avg)
    def display(self):
        print(self.tot,self.avg)
c=1
l=[]
while c<=2:
    no=int(input())
    name=input()
    s1=int(input())
    s2=int(input())
    s3=int(input())
    s4=int(input())
    s5=int(input())
    l.append(student(no,name,s1,s2,s3,s4,s5))
    c+=1
for i in range(len(l)):
    l[i].total()
    l[i].average()
    l[i].display()
for i in range(len(l)):
    print(list(l[i]))
