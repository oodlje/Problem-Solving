import sys
n,m=map(int,sys.stdin.readline().split())
array=[]
cur=0
def numFunc(num):
    global cur
    if (cur==m):
        print(*array)
        return
    for i in range(num,n+1):
        if i not in array:
            array.append(i)
            cur+=1
            numFunc(i)
            cur-=1
            array.pop()
numFunc(1)