import sys
num=int(sys.stdin.readline())
for _ in range(num):
    a,b=map(int,sys.stdin.readline().split())
    smaller=min(a,b)
    start=1
    for i in range (1,smaller+1):
        if a%i==0 and b%i==0:
            ans=i 
    print(int((a*b)/ans))
