import sys
a,b=map(str,sys.stdin.readline().split())
ans=0
for i in range (len(a)):
    for j in range(len(b)):
        ans+=int(a[i])*int(b[j])
print(ans)
