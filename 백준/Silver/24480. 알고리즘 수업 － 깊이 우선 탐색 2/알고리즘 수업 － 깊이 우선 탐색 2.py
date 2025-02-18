import sys
sys.setrecursionlimit(10**6)
length=list(map(int,sys.stdin.readline().split()))
dfsArr=[0]*length[0]

def dfs(start):
    global count
    for i in (num[start]):
        if (visited[i]==0):
            count+=1
            dfsArr[i]=count
            visited[i]=1
            dfs(i)

num=[[] for _ in range(length[0])]
visited=[0]*length[0]
for i in range(length[1]):
    a,b=map(int,sys.stdin.readline().split())
    num[a-1].append(b-1)
    num[b-1].append(a-1)

#역순 구성 
for i in range(length[0]):
    num[i].sort(reverse=True)

count=1
dfsArr[length[2]-1]=count
visited[length[2]-1]=1
dfs(length[2]-1)

for i in range(length[0]):
    print(dfsArr[i])

    