import sys
from collections import deque
a,b,h=map(int,sys.stdin.readline().split())
# get=[[0]*b]*h 얕은복사
# 깊은복사로 수정
get = [[0] * b for _ in range(h)]
for j in range(h):
    for i in range(b):
        get[j][i]=list(map(int,sys.stdin.readline().split()))
queue=deque()
countOne=0
countTime=0
countMinus=0
dz=[0,0,0,0,1,-1]
dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]

# bfs 상하좌우 따지면서 먼저 훑고 다음 레벨로 넘어가기
# queue에 저장되는 값: i,j,횟수
def bfs():
    global countOne
    global countTime
    global countMinus
    for k in range(h):
        for i in range(b):
            for j in range(a):
                if (get[k][i][j]==1):
                    queue.append([k,i,j,0])
                    countOne+=1
                if (get[k][i][j]==-1):
                    countMinus+=1
    while queue:
        dk,di,dj,dc=queue.popleft()
        if (dc>countTime):
            countTime=dc
        for i in range(6):
            newk=dk+dz[i]
            newi=di+dx[i]
            newj=dj+dy[i]
            if (0<=newk<h and 0<=newi<b and 0<=newj<a)and(get[newk][newi][newj]==0):
                queue.append([newk,newi,newj,dc+1])
                get[newk][newi][newj]=1
                # print(str(newk)+str(newi)+str(newj))
                countOne+=1

bfs()
if (a*b*h-countMinus!=countOne):
    print(-1)
else:
    print(countTime)

        
