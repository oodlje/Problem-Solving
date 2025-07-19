import sys
# 배열 sort하고
# n보다 작은 하한선 값 선택 하한선+1 -> 상한선-1
# n보다 큰 상한선 값 선택  n -> 상한선-1
# 이중 반복문  
sLen=int(sys.stdin.readline())
sArray=list(map(int,sys.stdin.readline().split()))
n=int(sys.stdin.readline())
sArray.sort()
add=0
sMin=0
sMax=1001
for i in range(sLen):
    if sArray[i]<n:
        sMin=sArray[i]
    elif sArray[i]>n:
        sMax=sArray[i]
        break
    else:
        add=-1
        break
        # 0 출력
# sMin+1 - n  부터 n - sMax-1까지
if add==-1:
    print(0)
else:
    for i in range(sMin+1, n+1, 1):
        for j in range(n,sMax,1):
            if i!=j:
                # print(i,j)
                add+=1
    print(add)

    
