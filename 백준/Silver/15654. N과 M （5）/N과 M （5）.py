import sys
n,m=map(int,sys.stdin.readline().split())
get=list(map(int,sys.stdin.readline().split()))
get.sort()
array=[]
cur=0
def numFunc():
    global cur
    if (cur==m):
        print(*array)
        return
    for i in range(n):
        if get[i] not in array:
            array.append(get[i])
            cur+=1
            numFunc()
            cur-=1
            array.pop()
numFunc()