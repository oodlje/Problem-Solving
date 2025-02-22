import sys
num=int(sys.stdin.readline())
edge=list(map(int,sys.stdin.readline().split()))
node=list(map(int,sys.stdin.readline().split()))
minNode=node[0]
sum=[0]*(num)
cost=0
# 가장 작은 노드값 구하기
for i in range(num-1):
    if (minNode>node[i]):
        minNode=node[i]
# print(minNode)
# 각 위치에서의 edge 누적합 구하기
sum[num-1]=0
for i in range(num-2,-1,-1):
    sum[i]=sum[i+1]+edge[i]
# print(sum)
# 비용 구하기
for i in range(num-1):
    if (node[i]>minNode):
        cost+=node[i]*edge[i]
    else:
        cost+=node[i]*sum[i]
        break

print(cost)










    

