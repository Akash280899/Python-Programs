a=int(input())
for i in range(a):
    b=input()
    c=[str(x) for x in str(b)]
    e=[]
    for j in range(len(c)):
        if(c[j]=='a' or c[j]=='e' or c[j]=='i' or c[j]=='o' or c[j]=='u'):
            e.append(c[j].upper())
        else:
            e.append(c[j].lower())
    for i in e:
        print(i,end="")
    print()
