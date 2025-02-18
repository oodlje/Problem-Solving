import sys
# 노드 개수
n=int(sys.stdin.readline())
# 간선 개수
m=int(sys.stdin.readline())
visited=[0]*n
def dfs(start):
    visited[start-1]=1
    for i in range(n):
        if ((edge[start-1][i]==1) and (visited[i]==0)):
            visited[i]=1
            dfs(i+1)

edge=[[0]*n for _ in range(n)]
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    edge[a-1][b-1]=1
    edge[b-1][a-1]=1
dfs(1)

count=0
for i in range(n):
    if (i==0):
        continue
    elif (visited[i]==1):
        count+=1
print(count)




    