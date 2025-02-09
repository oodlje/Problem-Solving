import sys
num = int(sys.stdin.readline().strip())
seq=list(sys.stdin.readline().split())
dp=[0]*len(seq)
large=0
for i in range(len(seq)):
    if (i==0):
        dp[i]=1
    else:
        large=0
        for j in range (i):
            if ((int(seq[i])>int(seq[j])) & (dp[j]>large)):
                #비교는 정수끼리
                large=dp[j]
        dp[i]=large+1

maxLen=0
for i in range(len(dp)):
    if (maxLen<dp[i]):
        maxLen=dp[i]


print(maxLen)
#print(dp)