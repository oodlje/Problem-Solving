import sys
m=int(input())
line=list(map(int,sys.stdin.readline().split()))
line.sort()
add=0
for i in range (m):
    for j in range(i+1):
        add+=line[j]


print(add)
    