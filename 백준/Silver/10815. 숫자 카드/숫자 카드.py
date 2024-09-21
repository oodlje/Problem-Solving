import sys
n=input()
numList=list(map(int,sys.stdin.readline().split()))
m=input()
numList2=list(map(int,sys.stdin.readline().split()))

numList.sort()
newList=[0]*len(numList2)

for i in range (len(numList2)):
    start=0
    end=(len(numList)-1)
    while start<=end:
        mid=(start+end)//2
        if numList[mid]==numList2[i]:
            newList[i]=1
            break
        elif numList[mid]>numList2[i]:
            end=mid-1
        else:
            start=mid+1

print(' '.join(map(str, newList)))

            
        
