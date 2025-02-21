import sys
length=int(sys.stdin.readline())
#실제 값 저장하지 말고 개수만 출력하기
num=[[0]*10 for _ in range(length)]
for i in range (length):
    for j in range (10):
        if ((i==0)&(j!=0)):
            num[0][j]=1
        else:
            if (j!=9)and(j!=0):
                num[i][j]=num[i-1][j-1]+num[i-1][j+1]
            elif (j==9):
                num[i][j]=num[i-1][j-1]
            elif (j==0):
                num[i][j]=num[i-1][j+1]
# print(num)
sum=0
# 오버플로우 방지
for i in range(10):
    sum+=num[length-1][i]
    if (sum>1000000000):
        sum=int(sum%1000000000)
print(sum)
