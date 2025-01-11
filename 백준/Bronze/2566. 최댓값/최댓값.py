import sys
mat = [[0 for _ in range(9)] for _ in range(9)]
loc=[0,0]
max=0
for i in range(9):
    line=list(map(int,sys.stdin.readline().split()))
    for j in range(9):
        if line[j]>=max:
            max=line[j]
            loc=[i,j]
        mat[i][j]=line[j]
print(max)
print(loc[0]+1,loc[1]+1)
