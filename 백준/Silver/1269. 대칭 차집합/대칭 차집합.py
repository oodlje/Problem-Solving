import sys
#대칭 차집합의 합이니까 전체에서 중복된 것을 빼주면 됨
#get 메소즈 사용하기
a,b=map(int, sys.stdin.readline().split())
myMap={}
getA=list(map(int,sys.stdin.readline().split()))
getB=list(map(int,sys.stdin.readline().split()))
for i in range(a):
    if (myMap.get(getA[i])):
        myMap[getA[i]]+=1
    else:
        myMap[getA[i]]=1
for i in range(b):
    if (myMap.get(getB[i])):
        myMap[getB[i]]+=1
    else:
        myMap[getB[i]]=1
count=0
for k,v in myMap.items():
    if (v==1):
        count+=1
print(count)