import sys
sys.setrecursionlimit(10**6)
# find: 집합의 루트 노드 찾기
def find(i):
    if parent[i]!=i:
        parent[i]=find(parent[i])
    return parent[i]

# union: 두 집합 합치기 
def union(i,j):
    global parent
    rootI=find(i)
    rootJ=find(j)
    # 더 작은값을 루트노드로 지정하기 
    if (rootI<rootJ):
        parent[rootJ]=rootI
    else:
        parent[rootI]=rootJ


n,m=map(int,sys.stdin.readline().split())
parent=[i for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==0:
        union(b,c)
    else:
        #두 원소가 같은 집합에 속해있는지 확인
        if(find(b)==find(c)):
            print("yes")
        else:
            print("no")
