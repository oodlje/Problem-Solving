import sys
day=int(input())
dp=[0]*day
dpCost=[0]*day
for i in range(day):
    t,p = map(int, sys.stdin.readline().split())
    if (i==0):
        dp[0]=t
        dpCost[0]=p
        continue
    maxCost=0
    index=0
    for j in range(i):
        if (int(dp[j])<=i):
            if (dpCost[j]>maxCost):
                maxCost=dpCost[j]
                index=j
    dpCost[i]=maxCost+p
    dp[i]=i+t

max=0
for i in range(day):
    if (max<dpCost[i])and(dp[i]<=day):
        max=dpCost[i]
# print(dpCost)
# print(dp)
print(max)


