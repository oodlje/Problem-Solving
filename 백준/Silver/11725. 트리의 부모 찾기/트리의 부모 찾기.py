import sys
num=int(sys.stdin.readline())
node=[[] for _ in range(num)]
queue=[]
parent=[-1]*num
#queue 안에 현재 찾는 값을 넣고 
def dfs(start):
    queue.append(start)
    while queue:
        find=queue.pop(0)
        for i in node[find]:
            if (parent[i]==-1):
                queue.append(i)
                parent[i]=find
        # for i in range(num):
        #     if find in node[i]:
        #         if (parent[i]==-1):
        #             queue.append(i)
        #             parent[i]=find

for i in range(num-1):
    a,b=map(int,sys.stdin.readline().split())
    node[a-1].append(b-1)
    node[b-1].append(a-1)
dfs(0)
for i in range(1,num):
    print(parent[i]+1)
