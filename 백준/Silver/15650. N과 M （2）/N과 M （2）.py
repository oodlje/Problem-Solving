import sys
n,m=map(int,sys.stdin.readline().split())
num=[]
total=set()
for i in range(n):
    num.append(i+1)

def numFunc(cur,array):
    if (cur==m):
        # 리스트 자동 공백 문자열 변환
        total.add(frozenset(array))
        return
    for i in range(n):
        if (i+1) not in array:
            array.append(i+1)
            numFunc(cur+1,array)
            array.pop()
numFunc(0,[])
# set을 정렬된 리스트로 변환한 뒤에 전체 요소들을 sort 
sorted_sets = sorted(total, key=lambda s: sorted(s))
for s in sorted_sets:
    print(*sorted(s))