import sys
m,n=map(int,sys.stdin.readline().split())
# 문자열 중의 일부가 포함되는지 확인하기 위해서는 for을 빠르게 쓸 수 있는 set 쓰자
count=0
myMap=set()
for i in range(m):
    get=sys.stdin.readline().strip()
    myMap.add(get)
for j in range(n):
    get=sys.stdin.readline().strip()
    if get in myMap:
        count+=1
print(count)

    
    
