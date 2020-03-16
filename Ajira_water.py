'''clu=[["c1","200","400"],["c2","200","300"],["c3","100","100"],["c4","150","300"]]
pipe1=["c1","c3",["c1","c2"],["c3","c4"]]'''
days=int(input())
cl=int(input())
days1=1
clu=[]
pipe1=[]
e=[]
for i in range(cl):
    a=input().split()
    clu.append(a)
pipes=int(input())
for i in range(pipes):
    b=input()
    if("F" in b):
        d=b.replace("F","")
        d=d.replace("_","")
        pipe1.append(d)
    else:
        d=b.replace("_",",")
        d=d.split(",")
        f=d[0]
        h=d[1]
        pipe1.append([f,h])
for i in range(len(clu)):
    e.append(int(clu[i][2]))
while(days1<=days):
    for i in range(len(clu)):
        if((int(clu[i][1]))*days1>(int(clu[i][2]))):
            c=clu[i][0]
            for j in range(len(pipe1)):
                if(c==pipe1[j][1]):
                    d=list(pipe1[j])
                if c==pipe1[j]:
                    d=pipe1[j]
            if(isinstance(d, list)):
                for k in range(len(d)):
                    for l in range(len(clu)):
                        if (d[k]==clu[l][0]):
                            if(int(clu[l][2])==e[-1]):
                                continue
                            else:
                                e.append(int(clu[l][2]))
            else:
                for l in range(len(clu)):
                    if (d==clu[l][0]):
                        e.append(int(clu[l][2]))
    days1+=1
print(sum(e))
print(type(e))
clu=[["c1","200","300"],["c2","150","300"],["c3","200","200"],["c4","100","400"]]
pipe1=["c1","c3",["c1","c2"],["c3","c4"]]
templist=clu
days=5
days1=1
e=[]
for i in range(len(clu)):
    e.append(int(clu[i][2]))
    temp=int(clu[i][1])
    temp1=int(clu[i][2])
    res=temp1-temp
    if res<temp:
        clu[i][2]=temp1
        #e.append(int(clu[i][2]))
    elif res>=temp:
        clu[i][2]=res
while(days1<=days):
    # for i in range(len(clu)):
    #     e.append(int(clu[i][2]))
        
    for i in range(len(clu)):
        temp=int(clu[i][1])
        temp1=int(clu[i][2])
        res=temp1-temp
        if res==0:
            clu[i][2]=int(templist[i][2])
        elif res<temp:
            clu[i][2]=temp1
            e.append(int(clu[i][2]))
        elif res>temp:
            clu[i][2]=res
            #e.append(int(clu[i][2]))
        # temp=int(clu[i][1])
        # temp1=int(clu[i][2])
        # if temp*days1>temp1:
        #     e.append(temp1)
            #clu[i][2]=temp1-temp
    days1+=1
