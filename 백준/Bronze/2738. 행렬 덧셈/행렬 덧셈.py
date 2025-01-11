import sys
line=list(map(int,sys.stdin.readline().split()))
mat = [[0 for _ in range(line[1])] for _ in range(line[0])]
for i in range (line[0]):
    col=list(map(int,sys.stdin.readline().split()))
    for j in range(len(col)):
        mat[i][j]=col[j]

for i in range (line[0]):
    col=list(map(int,sys.stdin.readline().split()))
    for j in range(len(col)):
        mat[i][j]+=col[j]
for i in range(line[0]):
    for j in range(line[1]):
        print(mat[i][j],"",end="")
    print("")