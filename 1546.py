import sys
subNum=int(input())
numList=list(map(int,sys.stdin.readline().split()))
max=numList[0]
for i in range (subNum):
    if numList[i]>max:
        max=numList[i]
add=0
for i in range (subNum):
    add=add+numList[i]
res=(add/max*100)/subNum
print(res)