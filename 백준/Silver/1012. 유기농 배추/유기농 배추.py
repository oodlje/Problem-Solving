import sys
count=int(sys.stdin.readline())
sys.setrecursionlimit(10000)
def dfs(b,a):
    farm[b][a]=0
    if (b>0 and farm[b-1][a]==1):
        farm[b-1][a]=0
        dfs(b-1,a)
    if (a>0 and farm[b][a-1]==1):
        farm[b][a-1]=0
        dfs(b,a-1)
    if (b<n-1 and farm[b+1][a]==1):
        farm[b+1][a]=0
        dfs(b+1,a)
    if (a<m-1 and farm[b][a+1]==1):
        farm[b][a+1]=0
        dfs(b,a+1)

while(count!=0):
    total=0
    m,n,k=map(int,sys.stdin.readline().split())
    farm=[[0]*m for _ in range(n)]
    for i in range(k):
        a,b=map(int,sys.stdin.readline().split())
        farm[b][a]=1
    for i in range(n):
        for j in range(m):
            if (farm[i][j]==1):
                dfs(i,j)
                total+=1
    print(total)
    count-=1


    
    