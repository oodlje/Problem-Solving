n=int(input())
ans=2
for i in range(n):
    ans=ans+(ans-1)
ans=ans*ans
print(ans)