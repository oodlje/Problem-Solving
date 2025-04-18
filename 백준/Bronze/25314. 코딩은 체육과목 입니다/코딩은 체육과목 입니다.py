import sys
num=int(sys.stdin.readline())
repeat=int(num//4)
ans=[]
for i in range(repeat):
    ans.append("long")
ans.append("int")
print(*ans)

