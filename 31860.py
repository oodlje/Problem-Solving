import sys
import heapq
#최대 힙 이용하기
#headq 최대 힙 제공하지 않아 음수로 변경해 판단하기 
#시간초과 해결방법 고려
n,m,k=map(int,sys.stdin.readline().split())
y=0
work=[0]*n
sat=[]
for i in range(n):
    heapq.heappush(work, -int(sys.stdin.readline()))
big=0

while work and -work[0] > k:
    big = -heapq.heappop(work)
    y = y//2 + big
    sat.append(y)
    big -= m

    if big > k:
        heapq.heappush(work, -big)
      
print(len(sat))
s=""
for i in range (len(sat)):
    s +=str(sat[i])+'\n'
print(s)
        
