'''7
3
==>2.(3)

4
2
==>2.

5212
5
==>1042.4 '''

def convert(n,d):
    res=[str(n//d)+'.']
    sr=[n%d]
    n%=d
    while n!=0:
        n*=10
        rd,n=divmod(n,d)
        res.append(str(rd))
        if n not in sr:
            sr.append(n)
        else:
            res.insert(sr.index(n)+1,'(')
            res.append(')')
            break
    return ''.join(res)
a=int(input())
b=int(input())
print(convert(a,b))
