import sys
clock1=list(map(int,sys.stdin.readline().split()))
if clock1[1]>=45:
    clock1[1]-=45
else:
    left=45-clock1[1]
    clock1[1]=60-left
    clock1[0]-=1
    if (clock1[0]==-1):
            clock1[0]=23

print(clock1[0],clock1[1])