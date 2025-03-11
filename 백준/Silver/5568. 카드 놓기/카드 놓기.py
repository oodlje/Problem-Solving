import sys
n=int(input())
k=int(input())
# num: 모든 값 모아놓은 배열 
num=[]
numList=[]
count=0
for i in range(n):
    get=(input())
    num.append(get)

# 재귀함수로 구현
# result: 배열 결과, picked: 선택한 인덱스 배열
def find(result, i, picked):
    if (i==k):
        if result not in numList:
            numList.append(result)
        return
    for j in range(len(num)):
        if j not in picked:
            # result+=num[j]
            newResult=result+num[j]
            picked.append(j)
            find(newResult,i+1,picked)
            picked.pop()

find("",0,[])
print(len(numList))