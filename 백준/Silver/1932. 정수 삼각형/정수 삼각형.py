import sys
num=int(sys.stdin.readline())
line=[0]*num
for i in range(num):
    line[i]=list(map(int,sys.stdin.readline().split()))

# line[i][j]+=line[i-1][j-1] or line[i-1][j]
for i in range(1, num):
    for j in range(len(line[i])):
        if (j==0):
            line[i][0]+=line[i-1][j]
        elif (j==len(line[i])-1):
            line[i][j]+=line[i-1][j-1]
        else:
            line[i][j]+=max(line[i-1][j-1],line[i-1][j])
max=0
for i in range(num):
    if (max<line[num-1][i]):
        max=line[num-1][i]
# print(line)
print(max)



