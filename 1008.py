import sys
num=int(input())
numList=list(map(int,sys.stdin.readline().split()))
min=numList[0]
max=numList[0]

for i in range (num):
    if min>numList[i]:
        min=numList[i]
    if max<numList[i]:
        max=numList[i]
result=min*max
print(result)