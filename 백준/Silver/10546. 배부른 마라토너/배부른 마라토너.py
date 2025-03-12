import sys
n=int(sys.stdin.readline())
log={}
leave=[]
for i in range(n):
    a=sys.stdin.readline()
    if a in log.keys():
        log[a]+=1
    else:
        log[a]=1
for i in range(n-1):
    a=sys.stdin.readline()
    log[a]-=1
for k,v in log.items():
    if (v!=0):
        print(k)
