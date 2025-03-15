import sys
n,m=map(int,sys.stdin.readline().split())
get=list(map(int,sys.stdin.readline().split()))
get.sort()
array=[]
cur=0
def numFunc(num):
    global cur
    if (cur==m):
        print(*array)
        return
    for i in range(num,n):
        array.append(get[i])
        cur+=1
        numFunc(i)
        cur-=1
        array.pop()
numFunc(0)