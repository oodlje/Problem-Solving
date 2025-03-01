import sys
count=int(sys.stdin.readline())
n=[0]*count
n[0]=1
if (count>=2):
    n[1]=2
for i in range(2,count):
        n[i]=(n[i-1]+n[i-2])%15746
        # if (n[i]>15746):
        #     n[i]=n[i]%15746

print(n[count-1])

# bottomup 방식
# 0이면 바로 뒤의 값은 건너뛰기
# 모든 경우의 수 구하기 위해 누적합