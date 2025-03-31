import sys
from heapq import *
inf=1e12
# 다익스트라 알고리즘
# 달빛 여우: 일반 다익스트라 알고리즘 적용하기
# 달빛 늑대: 각 노드값 1/2,2배씩 계산해서 알고리즘 적용하기
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
def dstra(dist, node):
    heap=[]
    distList=[inf]*a
    heappush(heap,(0,0))
    while heap:
        w,now=heappop(heap)
        if w>distList[now]:
            continue
        for k,v in way[now]:
            if (w+v<distList[k]):
                distList[k]=w+v
                heappush(heap,(distList[k],k))
        # visit.pop(get[1]-1)
    # print(distList)
    return distList

def dstraWolf(dist, node):
    heap=[]
    # 0: 느림 1: 빠름
    distList=[[inf] * a for _ in range(2)]
    heappush(heap,(0,0,0))
    while heap:
        w,now,s=heappop(heap)
        if w>distList[s][now]:
            continue
        for k,v in way[now]:
            if (s==1):
                # 부동소수점 주의 
                v<<=1
                if(w+(v)<distList[0][k]):
                    distList[0][k]=w+(v)
                    heappush(heap,(w+(v),k,0))
            if (s==0):
                v>>=1
                if(w+(v)<distList[1][k]):
                    distList[1][k]=w+(v)
                    heappush(heap,(w+(v),k,1))
    # print(distList)
    return distList

a,b=map(int,sys.stdin.readline().split())
way=[[] for _ in range(a)]
for _ in range(b):
    i,j,k=map(int,sys.stdin.readline().split())
    i -= 1
    j -= 1
    way[i].append((j,k*2))
    way[j].append((i,k*2))
    #실수 범위 정수 범위 계산 오류 방지 위해
fox=dstra(0,1)
wolf=dstraWolf(0,1)
wolfMin=[]
count = 0
for i in range(1, a):  # 1번 제외
    fox_dist = fox[i]
    wolf_dist = min(wolf[0][i], wolf[1][i])
    if fox_dist < wolf_dist:
        count += 1
print(count)



