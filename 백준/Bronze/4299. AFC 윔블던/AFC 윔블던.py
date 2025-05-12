import sys
n,m=map(int,sys.stdin.readline().split())
a=int((n+m)/2)
b=int((n-m)/2)
if a<0 or b<0:
    print(-1)
elif (n+m)%2!=0 or (n-m)%2!=0:
    print(-1)
elif a<=b:
    print(str(b)+" "+str(a))
elif a>b:
    print(str(a)+" "+str(b))
else:
    print(-1) 
