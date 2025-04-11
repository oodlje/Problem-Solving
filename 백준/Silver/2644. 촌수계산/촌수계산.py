num=int(input())
n,m=map(int,input().split())
link=int(input())
#방문 여부, 거친 간선 횟수 저장
visited=[[0,0] for _ in range (num+1)]
def dfs(start):
    # global visited
    # global graph
    visited[start][0]=1
    #연결된 node들 모두 살피기
    #m이 나올 때 거친 간선 개수 알아야 됨 
    for i in graph[start]:
        if (visited[i][0]==0):
            visited[i][1]=visited[start][1]+1
            # print(i)
            dfs(i)
    
graph=[[] for _ in range(num+1)]
for i in range(link):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(n)
if (visited[m][1]==0):
    print(-1)
else:
    print(visited[m][1])