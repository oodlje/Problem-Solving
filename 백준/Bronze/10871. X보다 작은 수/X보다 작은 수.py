import sys
n,x=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
ans=[]
for i in range(n):
    if arr[i]<x:
        ans.append(arr[i])
print(*ans)


