import sys
num=int(sys.stdin.readline())
findMap=[]
ans=0
people=list(map(int,sys.stdin.readline().split()))
for i in range (len(people)):
    if people[i] in findMap:
        ans+=1
    else:
        findMap.append(people[i])
print(ans)