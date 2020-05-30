#gslv f11 in 19,2018==>11 2018


import re
num = "gslv 11,2018 19"
a = re.split("\\D+",num)
a.remove("")
for i in a:
    if '9' in i:
        a.remove(i)
print(a)

t=int(input())
l=[]
r=[]
r2=[]
r3=''
r4=[]
res=[]
flag=0
if t>=1 and t<=100:
    for i in range(0,t):
        a=input()
        if len(a)>=1 and len(a)<=1000:
            l.append(a)
for i in l:
    l1=i.split(" ")
    for i in l1:
        if '9' in i:
            l1.pop(l1.index(i))
    for i in l1:
        if i.isdigit():
            r.append(i)
        elif i.isalnum():
            for j in i:
                if j>='0' and j<='9':
                    r3=r3+j
            r.append(r3)
            r3=''
    for i in range(0,len(r)):
        if r[i]!="":
            res.append(r[i])
            flag=1
    if flag==0:
        print("-1")
    else:
        for i in res:
            print(i,end=" ")
        print()
        r=[]
        res=[]
        flag=0
