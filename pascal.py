a=int(input())
b=[1]
c=[0]
l=[]
for i in range(a+1):
    l.append(b)
    b=[b+c for b,c in zip(b+c,c+b)]
print(*l[len(l)-1])

#to print 1 3 3 1
