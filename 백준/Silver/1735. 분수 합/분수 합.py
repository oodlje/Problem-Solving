# 분모의 최대공약수-함수화(유클리드 호제법)를 구하고 합을 구한 뒤 약분하는 문제
import sys
a1,b1=map(int,sys.stdin.readline().split())
a2,b2=map(int,sys.stdin.readline().split())

def gcd(bmax,bmin):
    while True:
        if bmax%bmin==0:
            ansB=bmin
            # 최대공약수 반환
            return ansB
        else:
            newmax=bmin
            bmin=int(bmax%bmin)
            bmax=newmax



#분모 통일 
bmax=max(b1,b2)
bmin=min(b1,b2)
mul=bmax*bmin

ansB=(mul)//gcd(bmax,bmin)
a1=(ansB//b1)*a1
a2=(ansB//b2)*a2
ansA=a1+a2

# 기약분수 형태 변환 
div=gcd(ansB,ansA)
ansB=ansB//div
ansA=ansA//div
print(str(ansA)+" "+str(ansB))