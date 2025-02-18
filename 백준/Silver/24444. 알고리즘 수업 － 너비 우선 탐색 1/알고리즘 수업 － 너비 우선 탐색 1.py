import sys
length=list(map(int,sys.stdin.readline().split()))
indexArr=[0]*length[0]
# 너비우선
# 행렬이 아닌 링크로 구현 
def bfs(start):
    queue=[start-1]
    visited2[start-1]=1
    count=1
    indexArr[start-1]=count
    while (queue):
        find=queue.pop(0)
        for i in num[find]:
            if (visited2[i]==0):
                queue.append(i)
                count+=1
                indexArr[i]=count
                visited2[i]=1
num=[[] for _ in range(length[0])]
visited2=[0]*length[0]
for i in range(length[1]):
    a,b=map(int,sys.stdin.readline().split())
    num[a-1].append(b-1)
    num[b-1].append(a-1)
#역순 구성 
for i in range(length[0]):
    num[i].sort()
bfs(length[2])
for i in range(length[0]):
    print(indexArr[i])
