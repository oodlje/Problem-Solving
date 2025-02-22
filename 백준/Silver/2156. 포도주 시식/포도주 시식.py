import sys
num=int(sys.stdin.readline())
line=[0]*num
for i in range(num):
    line[i]=int(sys.stdin.readline())
dp=[0]*num    
# dp[i]=line[i]+line[i-1]+dp[i-3] 바로 전의 포도주 먹기
# dp[i]=line[i]+dp[i-2] 두 개 전의 포도주 먹기
dp[0]=line[0]
for i in range(1, num):
    if (i==1):
        dp[1]=line[1]+dp[0]
    elif (i==2):
        dp[2]=line[2]+max(line[1],line[0])
    else:
        findMax=0
        for j in range(0,i-2):
            if (findMax<dp[j]):
                findMax=dp[j]
        dp[i]=line[i]+max(line[i-1]+findMax,dp[i-2])
        # 계단 오르기와 다르게 모든 step 밟지 않기 때문에
        # dp[i-3]이 아닌 findMax로 잡아야    
max=0
for i in range(num):
    if (max<dp[i]):
        max=dp[i]
print(max)



