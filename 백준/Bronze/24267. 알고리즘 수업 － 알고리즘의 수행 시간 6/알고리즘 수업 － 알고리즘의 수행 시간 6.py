import sys
num=int(sys.stdin.readline())
ans=0
for i in range(1, num-1):
    ans+=int(int(i*(1+i)/2))
print(ans)
print("3")

