import sys
origin=[1,1,2,2,2,8]
get=list(map(int,sys.stdin.readline().split()))
for i in range(6):
    print(origin[i]-get[i],end=" ")

