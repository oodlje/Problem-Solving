import sys
n=int(sys.stdin.readline())
log={}
leave=[]
for i in range(n):
    a,b=sys.stdin.readline().split()
    log[a]=b
for k,v in log.items():
    if (v=="enter"):
        leave.append(k)
leave.sort(reverse=True)
for i in range(len(leave)):
    print(leave[i])
