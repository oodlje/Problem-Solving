import sys
n,k=map(int,sys.stdin.readline().split())
ans=1
cur=0
for _ in range(k):
    ans*=(n-cur)
    cur+=1

mot=1
for i in range(k):
    mot=mot*(i+1)
ans=int(ans/mot)
print(ans)