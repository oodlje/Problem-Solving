import sys
length=list(map(int,sys.stdin.readline().split()))
dfsArr=[]
bfsArr=[]
# 지나가면 배열 1로 만들기
# 깊이우선
def dfs(start):
    dfsArr.append(start)
    visited[start-1]=1
    for i in range(length[0]):
        if (num[start-1][i]==1):
            # num[start-1][i]==0
            # num[i][start-1]==0
            # 안 지나갔으면
            if (visited[i]==0):
                dfs(i+1)

# 너비우선
def bfs(start):
    queue=[start-1]
    visited2[start-1]=1
    bfsArr.append(start)
    while (queue):
        find=queue.pop(0)
        for i in range(length[0]):
            if (num[find][i]==1)and(visited2[i]==0):
                queue.append(i)
                visited2[i]=1
                bfsArr.append(i+1)


num=[[0]*length[0] for _ in range(length[0])]
visited=[0]*length[0]
visited2=visited.copy()
for i in range(length[1]):
    a,b=map(int,sys.stdin.readline().split())
    num[a-1][b-1]=1
    num[b-1][a-1]=1
dfs(length[2])
bfs(length[2])

for i in range(len(dfsArr)):
    print(dfsArr[i],end=" ")
print()
for i in range(len(bfsArr)):
    print(bfsArr[i], end=" ")

    