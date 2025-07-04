import sys
first=int(sys.stdin.readline())
second=int(sys.stdin.readline())
start=1
ans=[]
while True:
    if start**2>second:
        break
    if start**2>=first:
        ans.append(start**2)

    start+=1

if len(ans)==0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])


