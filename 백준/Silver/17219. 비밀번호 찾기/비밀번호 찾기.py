import sys
a,b=map(int,sys.stdin.readline().split())
db={}
for i in range(a):
    get=list(map(str,sys.stdin.readline().split()))
    db[get[0]]=get[1]
for i in range(b):
    get=sys.stdin.readline().strip()
    print(db[get])
