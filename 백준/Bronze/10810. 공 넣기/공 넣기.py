import sys
a,b=map(int,sys.stdin.readline().split())
array=[0]*a
for i in range(b):
    i,j,k=map(int,sys.stdin.readline().split())
    for l in range(i-1,j,1):
        array[l]=k
print(*array)




