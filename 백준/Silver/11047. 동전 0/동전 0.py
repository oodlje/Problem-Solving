import sys
n,m=map(int,sys.stdin.readline().split())
sum=0
store=[0]*n
for i in range (n):
    store[i]=int(input())
store.sort(reverse=True)
left=m
for i in range (n):
    if (store[i]<=left):
        sum+=int(left/store[i])
        left=int(left%store[i])

print(sum)





