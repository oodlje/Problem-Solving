import sys
a,b=list(map(str, sys.stdin.readline().split()))
a=list(a)
b=list(b)
add5=0
add6=0

def replace(x):
    for i in range(len(a)):
        if a[i]=='5' or a[i]=='6':
            a[i]=x
    for i in range(len(b)):
        if b[i]=='5' or b[i]=='6':
            b[i]=x
replace('5')      
add5=int(''.join(a))+int(''.join(b))
replace('6')
add6=int(''.join(a))+int(''.join(b))
print(add5, add6)