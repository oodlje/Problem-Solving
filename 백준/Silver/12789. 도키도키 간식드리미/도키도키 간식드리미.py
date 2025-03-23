import sys
from collections import deque
left=[]
num=int(sys.stdin.readline())
line=deque(map(int, sys.stdin.readline().split()))
need=1
while (left or line):
    if left and (left[-1]==need):
        left.pop()
        need+=1
    elif line and (line[0]==need):        
        line.popleft()
        need+=1
    elif line:
        left.append(line.popleft())
    else:
        left.pop()
if (need==num+1):
    print("Nice")
else:
    print("Sad")

