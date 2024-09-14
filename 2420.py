import sys
numList=list(map(int,sys.stdin.readline().split()))
if (numList[0]-numList[1]>0):
    print(numList[0]-numList[1])
else:
    print(-numList[0]+numList[1])