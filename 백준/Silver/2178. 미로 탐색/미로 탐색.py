import sys
from collections import deque
# 최단경로는 bfs
# 여러 갈래로 경로 생기면 따로 세줘야함 
n,m=map(int,sys.stdin.readline().split())
maze=[0]*n
fin=False

def bfs(a,b):
    global queue
    global fin
    queue=deque([[0,0,1]])
    # 시작 좌표, 거리 
    maze[a][b]="0"
    while (queue):
        c,d,l=queue.popleft()
        # if (not queue[cur]):
        #     cur+=1
        #     queue.append([])
        if (c>0 and maze[c-1][d]=="1"):
            maze[c-1][d]="0"
            appendAdd(c-1,d,l)
        if (d>0 and maze[c][d-1]=="1"):
            maze[c][d-1]="0"
            appendAdd(c,d-1,l)
        if (c+1<n and maze[c+1][d]=="1"):
            maze[c+1][d]="0"
            appendAdd(c+1,d,l)
        if (d+1<m and maze[c][d+1]=="1"):
            maze[c][d+1]="0"
            appendAdd(c,d+1,l)
        if (fin==True):
            break

def appendAdd(a,b,l):
    global fin
    queue.append([a,b,l+1])
    # n,m 종착점에 도달하면
    if (a==n-1 and b==m-1):
        fin=True
        print(l+1)

for i in range(n):
    # 개행 문자 제거 후 리스트로 변환
    maze[i]=list(sys.stdin.readline().strip())
bfs(0,0)

    
    