# 분모의 최대공약수-함수화(유클리드 호제법)를 구하고 합을 구한 뒤 약분하는 문제
import sys

def gcd(a,b):
    bmax=max(a,b)
    bmin=min(a,b)
    while True:
        if bmax%bmin==0:
            ansB=bmin
            # 최대공약수 반환
            return ansB
        else:
            newmax=bmin
            bmin=int(bmax%bmin)
            bmax=newmax

num=int(sys.stdin.readline())
street=[]
for _ in range(num):
    tree=int(sys.stdin.readline())
    street.append(tree)
street.sort()
start=street[0]
end=street[-1]
streetLen=end-start
current=street[1]-street[0]
# 입력된 여러수들의 최소공배수로 간격 지정 
for i in range(1,len(street)-1):
    current=gcd(current,street[i+1]-street[i])
needNum=streetLen//current
print(needNum-len(street)+1)


