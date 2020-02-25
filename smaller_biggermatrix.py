n=3

N=[0] * n
for i in range(n):
    N[i]=list(map(int,input().split()))
S=[]
m=2
S=[0] * m
for i in range(m):
    S[i]=list(map(int,input().split()))
flag=0
p=0
q=0
for i in range(n):
    c=0
    p=0
    q=0
    for j in range(n):
        if N[i][j]==S[p][q]:
            x=i
            y=j
            for p in range(m):
                for q in range(m):
                    if N[x][y]==S[p][q]:
                        y=y+1
                        c=c+1
                x=x+1
                y=j
    if c==m*m:
        flag=1
        break
                
if flag==1:
    print("TRUE")
else:
    print("FALSE")
