import sys
num, time=map(int,sys.stdin.readline().split())
seq=list(map(int,sys.stdin.readline().split()))
add=[0]*num

for i in range(num):
    if (i==0):
        add[0]=seq[0]
    else:
        add[i]=seq[i]+add[i-1]
for _ in range(time):
    a,b=map(int,sys.stdin.readline().split())
    if (a==1):
        print(add[b-1])
    else:
        print(add[b-1]-add[a-2])
