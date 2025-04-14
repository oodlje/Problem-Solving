import copy
num=int(input())
arr=list(map(int,input().split()))
arrCopy=copy.deepcopy(arr)
arrCopy.sort()
axis=1
axisMap={}
#딕셔너리에서 0은 get 메소드 실행 시 false로 인지 
for i in range(num):
    if axisMap.get(arrCopy[i]):
        continue
    else:
        axisMap[arrCopy[i]]=axis
        axis+=1
for i in range(num):
    arr[i]=axisMap[arr[i]]-1
print(*arr)