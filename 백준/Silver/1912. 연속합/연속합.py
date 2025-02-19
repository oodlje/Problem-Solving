import sys
num=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
max=arr[0]
sum=0
for i in range(num):
    sum+=arr[i]
    if (max<sum):
        max=sum
    if (sum<0):
        sum=0
print(max)

