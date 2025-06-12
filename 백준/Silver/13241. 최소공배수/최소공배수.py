# 유클리드 호제법으로 최대공약수 구하기 
# 곱한 값을 최대공약수로 나눠 최소공배수 구하기 
import sys
a,b=map(int,sys.stdin.readline().split())
multiple=a*b
while True:
    if b%a==0:
        print(multiple//a)
        break
    else:
        reduce=int(b%a)
        b=a
        a=reduce

        