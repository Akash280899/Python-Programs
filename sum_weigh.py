#25,17,0,18==>17 0 18 25(example)

import math
n=input().split(',')
n=[int(i) for i in n]
l=[]
l1=[]
for i in n:
    r=0
    s=int(math.sqrt(i))
    if s*s==i:
        r+=5
    if i%4==0 and i%6==0:
        r+=4
    if i%2==0:
        r+=3
    l.append(r)
    l1.append(i)
print(l)
print(l1)
a=zip(l,l1)
a=list(a)
a.sort()
for i in range(len(a)):
    print(a[i][1],end=" ")

