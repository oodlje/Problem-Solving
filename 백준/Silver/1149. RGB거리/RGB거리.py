import sys
house=int(sys.stdin.readline())
#3개 단위로 끊으면서 bottom up 방식
#i-1과 i+1이 달라야 한다는 말은 없음
cost=[]
current=[[0]*3 for _ in range(house)]
for i in range(house):
    get=list(map(int,sys.stdin.readline().split()))
    cost.append(get)

index=0
for i in range(house):
    if (i==0):
        current[i][0]=cost[0]
        current[i][1]=cost[0]
        current[i][2]=cost[0]
    # current 배열을 이중 리스트로 놓기
    current[i][0]=cost[i][0]+min(current[i-1][1],current[i-1][2])
    current[i][1]=cost[i][1]+min(current[i-1][0],current[i-1][2])
    current[i][2]=cost[i][2]+min(current[i-1][0],current[i-1][1])
# print(current)
minRes=current[house-1][0]
for i in range(3):
    if (minRes>current[house-1][i]):
        minRes=current[house-1][i]
print(minRes)