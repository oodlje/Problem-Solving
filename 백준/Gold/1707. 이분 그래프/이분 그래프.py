#1부터 bfs 시작해서 집합 두 개에 차례대로 배치하기
#두 집합 각자에 인접한 노드 쌍이 있는지 확인하기
import sys
def bfs(start):
    global ans
    queue=[]
    state=0
    queue.append(start)
    visited[start]=state
    while queue:
        current=queue.pop(0)
        for node in setList[current]:
            if visited[node]==-1:
                queue.append(node)
                visited[node]=1-visited[current]
            else:
                #같은 집합에 속해있는지 확인
                if visited[node]==visited[current]:
                    ans="NO"
        #인접 쌍 있는지 확인 
    # print(graph)


testCase=int(sys.stdin.readline())
for i in range (testCase):
    v,e=map(int,sys.stdin.readline().split())
    setList=[[] for _ in range(v+1)]
    visited=[-1]*(v+1)
    ans="YES"
    for j in range(e):
        a,b=map(int,sys.stdin.readline().split())
        setList[a].append(b)
        setList[b].append(a)
    for j in range(1,len(visited)):
        if visited[j]==-1:
            bfs(j)
    print(ans)

