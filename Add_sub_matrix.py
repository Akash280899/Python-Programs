'''3 3
9 8 7 4 2 1 6 5 3
1 2 3 3

26'''

a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(0,len(b),a[1]):
    l.append(b[i:i+a[0]])
c=list(map(int,input().split()))
s=0
for row in range(c[0]-1,c[2]):
    for col in range(c[1]-1,c[3]):
        s+=l[row][col]
print(s)
