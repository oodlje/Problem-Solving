import sys
num=int(sys.stdin.readline())
final=[]
get=[[0]*num for _ in range(num)]
for i in range (num):
    get[i]=list(sys.stdin.readline())

#dfs 깊이우선 stack, 재귀 활용
def dfs(a,b):
    global count
    if(a+1<num) and (get[a+1][b]=="1"):
        get[a+1][b]="0"
        count+=1
        dfs(a+1,b)
    if (b+1<num) and (get[a][b+1]=="1"):
        get[a][b+1]="0"
        count+=1
        dfs(a,b+1)
    if (a-1>=0) and (get[a-1][b]=="1"):
        get[a-1][b]="0"
        count+=1
        dfs(a-1,b)
    if (b-1>=0) and (get[a][b-1]=="1"):
        get[a][b-1]="0"
        count+=1
        dfs(a,b-1)

        
for j in range(num):
    for i in range(num):
        if (get[i][j]=="1"):
            get[i][j]="0"
            count=1
            dfs(i,j)
            final.append(count)
final.sort()
print(len(final))
for i in range(len(final)):
    print(final[i])
