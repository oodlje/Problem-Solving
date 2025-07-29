import sys
num=int(sys.stdin.readline())
scoreList=list(map(int,sys.stdin.readline().split()))
add=0
prev=0
for i in range(num):
    if scoreList[i]==1:
        if (prev==0):
            prev=1
            add+=1
        else:
            prev+=1
            add+=prev
    else:
        prev=0
print(add)
            
            