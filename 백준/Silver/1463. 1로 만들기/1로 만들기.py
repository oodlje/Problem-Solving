import sys
num=int(sys.stdin.readline())
#n 부터 숫자를 하나씩 내려가면서 최소횟수 찾기
least=[0]*(num+1)
for i in range(num,1,-1):
    if (least[i]+1<least[i-1]) or (least[i-1]==0):
        least[i-1]=least[i]+1
    if (i%3==0):
        if (least[i]+1<least[i+1//3]) or (least[i//3]==0):
            least[i//3]=least[i]+1
    if (i%2==0):
        if (least[i]+1<least[i//2]) or (least[i//2]==0):
            least[i//2]=least[i]+1
print(least[1])