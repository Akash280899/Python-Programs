a=int(input())
l=[]
v=['a','e','i','o','u','A','E','I','O','U',]
for i in range(a):
    b=input().split(" ")
    b=[str(x) for x in str(b)]
    l.append(b)
for i in l:
    l=list(i)
    print(l)
    for i in range(0,len(l)):
        if(l[i]>='A' and l[i]<='Z') or (l[i]>='a' and l[i]<='z'):
            if l[i] in v:
                l[i]=l[i].upper()
            else:
                l[i]=l[i].lower()
    print(''.join(l))
