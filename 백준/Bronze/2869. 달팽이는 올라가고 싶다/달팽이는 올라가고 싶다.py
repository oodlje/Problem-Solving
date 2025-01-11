import sys
num=list(map(int,sys.stdin.readline().split()))
sum=0
day=0
mul=1
left=num[0]-num[1]
bef=num[2]-num[0]
sum=int(bef/left)
if (bef%left!=0):
        sum+=1
sum+=1

print(sum)