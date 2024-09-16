import sys
num=int(input())
ndots=[0]*num
mdots=[0]*num

for i in range (num):
    n,m=map(int,sys.stdin.readline().split())
    ndots[i]=n
    mdots[i]=m
for i in range (num):
#ncr=n!/(n-c)!r!
    n=ndots[i]
    m=mdots[i]
    fac=1
    while (m>n):
        fac=fac*m
        m-=1
    fac2=1
    m=mdots[i]
    mMinusn=m-n
    while (mMinusn>0):
        fac2=fac2*mMinusn
        mMinusn-=1
    print(int(fac/fac2))


