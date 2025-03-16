import sys
from collections import deque
a,b=map(int,sys.stdin.readline().split())
get=[0]*b
for i in range(b):
    get[i]=list(map(int,sys.stdin.readline().split()))
queue=deque()
countOne=0
countTime=0
countMinus=0

# bfs 상하좌우 따지면서 먼저 훑고 다음 레벨로 넘어가기
# queue에 저장되는 값: i,j,횟수
def bfs():
    global countOne
    global countTime
    global countMinus
    for i in range(b):
        for j in range(a):
            if (get[i][j]==1):
                queue.append([i,j,0])
                countOne+=1
            if (get[i][j]==-1):
                countMinus+=1
    while queue:
        s=queue.popleft()
        if (s[2]>countTime):
            countTime=s[2]
        if (s[0]>0 and (get[s[0]-1][s[1]]==0)):
            x=s[0]-1
            y=s[1]
            queue.append([x,y,s[2]+1])
            get[x][y]=1
            countOne+=1
        if (s[1]>0 and (get[s[0]][s[1]-1]==0)):
            x=s[0]
            y=s[1]-1
            queue.append([x,y,s[2]+1])
            get[x][y]=1
            countOne+=1
        if (s[0]<b-1 and (get[s[0]+1][s[1]]==0)):
            x=s[0]+1
            y=s[1]
            queue.append([x,y,s[2]+1])
            get[x][y]=1
            countOne+=1
        if (s[1]<a-1 and (get[s[0]][s[1]+1]==0)):
            x=s[0]
            y=s[1]+1
            queue.append([x,y,s[2]+1])
            get[x][y]=1
            countOne+=1

bfs()
if (a*b-countMinus!=countOne):
    print(-1)
else:
    print(countTime)

        
