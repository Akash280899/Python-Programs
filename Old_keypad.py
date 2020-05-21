'''23
ad ae af bd be bf cd ce cf

526
jam jan jao jbm jbn jbo jcm jcn jco kam kan kao kbm kbn kbo kcm kcn kco lam lan lao lbm lbn lbo lcm lcn lco

'''




h=["0","1",'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
def prinnt(number,cur,op,n):
    if cur==n:
        print(''.join(op),end=" ")
        return
    for i in range(len(h[number[cur]])):
        op.append(h[number[cur]][i])
        prinnt(number,cur+1,op,n)
        op.pop()
        if number[cur]==0 or number[cur]==1:
            return
def words(number,n):
    prinnt(number,0,[],n)
a=int(input())
if a>=0 and a<=10000:
    a=[int(x) for x in str(a)]
    n=len(a)
    words(a,n)
