import sys
n,m=map(int,sys.stdin.readline().split())
arr=[0]
for i in range(n):
    arr.append(i+1)
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    start=0
    for j in range(0,(b-a)//2+1):
        arr[a+start],arr[b-start]=arr[b-start],arr[a+start]
        start+=1
arr.pop(0)
print(*arr)
