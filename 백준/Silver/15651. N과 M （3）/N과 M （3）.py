import sys
n,m=map(int,sys.stdin.readline().split())
array=[]
cur=0
def numFunc():
    global cur
    if (cur==m):
        print(*array)
        return
    for i in range(n):
        array.append(i+1)
        cur+=1
        numFunc()
        cur-=1
        array.pop()
numFunc()