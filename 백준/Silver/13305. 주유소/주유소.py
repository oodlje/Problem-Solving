import sys
num=int(sys.stdin.readline())
edge=list(map(int,sys.stdin.readline().split()))
node=list(map(int,sys.stdin.readline().split()))
minNode=node[0]
sum=[0]*(num)
cost=node[0]*edge[0]
# 처음부터 최소 node값을 정해놓고 비용 계산하면 그리디가 아니고
# 순간에서의 최소 판단이 불가능함 
# 순간에서의 최소 node값을 이용해 비용 구하기
for i in range(1, num-1):
    if (node[i]<minNode):
        minNode=node[i]
    cost+=minNode*edge[i]

print(cost)










    

