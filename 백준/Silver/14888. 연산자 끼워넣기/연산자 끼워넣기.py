import sys
# 각 인원수에서 주감독을 빼고 //연산 하고 나머지가 0이 아니면 +1하기
num=int(input())
numList=list(map(int, sys.stdin.readline().split()))
op=list(map(int,sys.stdin.readline().split()))
# + - * /
maxNum=-1000000000
minNum=1000000000
# 현재 연산값, 현재 재귀 횟수, 연산번호
def operation(cur,i,j):
    global maxNum
    global minNum
    if j==0:
        cur+=numList[i]
    elif j==1:
        cur-=numList[i]
    elif j==2:
        cur*=numList[i]
    elif j==3:
        if (cur<0):
            cur=-((-cur)//numList[i])
        else:
            cur//=numList[i]
    # 종결조건
    if (i==(num-1)):
        if (cur>maxNum):
            maxNum=cur
        if (cur<minNum):
            minNum=cur
        return
    for k in range(4):
        if (op[k]!=0):
            op[k]-=1
            operation(cur,i+1,k)
            op[k]+=1

for j in range(4):
    if (op[j]!=0):
        op[j]-=1
        operation(numList[0],1,j)
        op[j]+=1

print(maxNum)
print(minNum)