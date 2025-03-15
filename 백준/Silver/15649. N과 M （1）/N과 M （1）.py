import sys
n,m=map(int,sys.stdin.readline().split())
num=[]
for i in range(n):
    num.append(i+1)

def numFunc(cur,array):
    if (cur==m):
        # 리스트 자동 공백 문자열 변환
        print(*array)
        return
    for i in range(n):
        if (i+1) not in array:
            array.append(i+1)
            numFunc(cur+1,array)
            array.pop()

numFunc(0,[])
