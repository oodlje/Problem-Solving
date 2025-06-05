import sys
from collections import deque
num=int(sys.stdin.readline())
queue=deque([i+1 for i in range(num)])
while len(queue)!=1:
    queue.popleft()
    next=queue.popleft()
    queue.append(next)
print(queue[0])