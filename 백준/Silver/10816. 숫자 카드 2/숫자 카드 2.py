import sys
m=int(sys.stdin.readline())
card=list(map(int,sys.stdin.readline().split()))
cardMap={}
ans=[]
for i in range(m):
    if cardMap.get(card[i]):
        cardMap[card[i]]+=1
    else:
        cardMap[card[i]]=1
n=int(sys.stdin.readline())
findCard=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    if cardMap.get(findCard[i]):
        ans.append(cardMap[findCard[i]])
    else:
        ans.append(0)
print(*ans)

    
    
