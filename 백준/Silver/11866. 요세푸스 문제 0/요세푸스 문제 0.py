import sys
# from collections import deque
n,k=map(int,sys.stdin.readline().split())
queue=[i+1 for i in range(n)]
status=k-1
ans=[]
while 1!=len(queue):
    ans.append(str(queue.pop(status)))
    status+=k-1
    status=status%len(queue)
ans.append(str(queue[0]))
print("<"+', '.join(ans)+">")

    