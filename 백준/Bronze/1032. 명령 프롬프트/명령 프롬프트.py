import sys
num=int(sys.stdin.readline())
for i in range(num):
    getFile=sys.stdin.readline().strip()
    if i==0:
        check=[0 for _ in range (len(getFile))]
        cur=getFile
    else:
        for j in range (len(cur)):
            if cur[j]!=getFile[j] and check[j]==0:
                check[j]=1
ans=[]
for i in range (len(cur)):
    if check[i]==1:
        ans.append("?")
    else:
        ans.append(cur[i])
        
print(''.join(ans))