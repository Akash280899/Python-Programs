#15==>1111==>no

n=int(input())
l=[]
b=bin(n)
bin=b[2:].split('1')
for i in range(0,len(bin)):
    c=bin[i].count('0')
    l.append(c)
print(l)
if(bin[len(bin)-1]!=''):
    l.pop()
if l==[] or max(l)==0:
    print("No binary gap")
else:
    print("The longest binary gap is ",max(l))
