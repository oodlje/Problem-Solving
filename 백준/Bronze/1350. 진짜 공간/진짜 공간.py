import sys
diskNum=int(sys.stdin.readline())
diskList=list(map(int,sys.stdin.readline().split()))
maximum=int(sys.stdin.readline())
ans=0
for i in range(diskNum):
    if diskList[i]==0:
        continue
    if diskList[i]<=maximum:
        ans+=maximum
    else:   
        if diskList[i]%maximum!=0:
            ans+=maximum*((diskList[i]//maximum)+1)
        else:
            ans+=maximum*((diskList[i]//maximum))


print(ans)
