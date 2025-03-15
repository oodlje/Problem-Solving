import sys
# 각 인원수에서 주감독을 빼고 //연산 하고 나머지가 0이 아니면 +1하기
num=int(input())
numList=list(map(int, sys.stdin.readline().split()))
main,sub=map(int,sys.stdin.readline().split())
count=0
for i in range(num):
    left=numList[i]-main
    count+=1
    # 보조감독이 필요하면
    if (left>0):
        count+=left//sub
        if (left%sub>0):
            count+=1
print(count)
