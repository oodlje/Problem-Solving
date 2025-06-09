import sys
a,b=map(int,sys.stdin.readline().split())
c=int(sys.stdin.readline())
nzero=int(sys.stdin.readline())
if (c>a) and (nzero>=(b/(c-a))):
    print(1)
elif (c==a) and (b<=0):
    print(1)
else:
    print(0)