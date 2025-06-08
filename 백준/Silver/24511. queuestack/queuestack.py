import sys
from collections import deque
num=int(sys.stdin.readline())
queueStack=list(map(int,sys.stdin.readline().split()))
current=list(map(int,sys.stdin.readline().split()))
inputNum=int(sys.stdin.readline())
inputList=list(map(int,sys.stdin.readline().split()))

ans=deque()
for i in range(num-1,-1,-1):
    if queueStack[i]==0:
        ans.append(current[i])

for i in range(inputNum):
    ans.append(inputList[i])
    print(ans.popleft(),end=" ")
print("")


