import sys
n=int(sys.stdin.readline())
num=[i+1 for i in range(9)]
ans=False
if n==1:
    ans=True
if n<=81 and n>1:
    for i in range(1,9):
        if n%num[i]==0 and n//num[i] in num:
            ans=True
            break

print(1 if ans else 0)
