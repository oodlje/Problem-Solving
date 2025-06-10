# 함수의 반환값(팰린드롬 여부)), recursion함수의 호출 횟수
import sys
import math
num=int(sys.stdin.readline())
for _ in range(num):
    checkPal=sys.stdin.readline().strip()
    start=0
    count=0
    isPal=1
    for i in range(math.ceil(len(checkPal)/2)):
        count+=1
        if checkPal[start]!=checkPal[len(checkPal)-1-start]:
            isPal=0
            break
        start+=1
    if isPal==1 and (len(checkPal)%2==0):
        count+=1
    print(str(isPal)+" "+str(count))
    

