import sys
n=int(sys.stdin.readline())
for i in range (2,n+1):
    while(True):
        if n%i==0:
            print(i)
            n=int(n/i)
        else:
            break