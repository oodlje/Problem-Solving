#나머지값 할당할 때는 나머지가 0인경우 생각하기
#나머지값은 n일 때 0~(n-1)
import sys
count=int(input())
total=1
totalList=[0]*count
for i in range(count):
    total=1
    numList=list(map(int,sys.stdin.readline().split()))
    a=numList[0]
    b=numList[1]
    if ((a==1) or (a==5) or (a==6)):
        totalList[i]=a
    else:
        if (b%4==0):
            b=4
        else:
            b=b%4
        for j in range(b):
            total=total*a
        if (total%10==0):
            totalList[i]=10
        else:
            totalList[i]=total%10

for i in range(count):
    print(totalList[i])