import sys
length=list(map(int,sys.stdin.readline().split()))
maxLen=0
for i in range(3):
    if (length[i]>maxLen):
        maxLen=length[i]
        index=i
sum=0
for i in range(3):
    if (index==i):
        continue
    sum+=length[i]

if (sum-1<maxLen):
    maxLen=sum-1
print(sum+maxLen)



    
    