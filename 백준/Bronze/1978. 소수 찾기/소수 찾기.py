import sys
num=int(input())
prime=list(map(int,sys.stdin.readline().split()))
count=0
for j in range(len(prime)):
    flag=False
    for i in range(2, prime[j]):
        if prime[j]%(i)==0:
            flag=True
    if (flag==False):
        count+=1
    if prime[j]==1:
        count-=1
    
print(count)