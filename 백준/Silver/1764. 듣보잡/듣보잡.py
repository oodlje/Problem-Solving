import sys
a,b=map(int,sys.stdin.readline().split())
check={}
res=[]
for i in range (a):
    name=sys.stdin.readline().strip()
    if name in check:
        check[name]+=1
    else:
        check[name]=1
for i in range (b):
    name=sys.stdin.readline().strip()
    if name in check:
        check[name]+=1
    else:
        check[name]=1
count=0
for k,v in check.items():
    if (v==2):
        count+=1
        res.append(k)
    res.sort()
print(count)
for i in range(len(res)):
    print(res[i])
        
    

            
