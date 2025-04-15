import sys
a=int(sys.stdin.readline())
num={}
for i in range(10000):
    num[i+1]=0
for i in range(a):
    cur=int(sys.stdin.readline())
    num[cur]+=1
for i in range(10000):
        while num[i+1]!=0:
                print(i+1)
                num[i+1]-=1
