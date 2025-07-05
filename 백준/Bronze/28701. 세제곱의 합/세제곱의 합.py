import sys
num=int(sys.stdin.readline())
ans1=0
ans2=0
for i in range(1,num+1):
    ans1+=i
    ans2+=i**3
print(ans1)
print(ans1**2)
print(ans2)

