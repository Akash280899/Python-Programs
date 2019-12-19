#elo world welcome all==>elomaa orldwmaaa elcomewmaaaa allmaaaaa

n = "elo world shut app"
v=['a','e','i','o','u']
n=n.split(" ")
j=1
for i in n:
    b=list(i)
    if b[0] in v:
        print(i,end="")
        print("ma",end="")
    else:
        d=(i[1:]+i[0])
        print(d,end="")
        print("ma",end="")
    print(j*'a',end="")
    j+=1
    print(end=" ")

    
        
    
