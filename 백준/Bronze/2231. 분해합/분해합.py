import sys
import math
a=int(sys.stdin.readline())

for i in range(1, a+1):
# 256/100=2 56/10=5 6/1=6
    numLen=int(math.log10(i))
    # log10하면 자릿수-1값 도출
    if (numLen==0):
        divide=1
    else:
        divide=10**(numLen)
    get=False
    each=[]
    sum=i
    original=i
    while(divide>=1):
        each.append(int(i/divide))
        i-=int(i/divide)*divide
        divide=int(divide/10)
    for i in range(len(each)):
        sum+=each[i]
        # 각 자릿수 합
    if (sum==a):
        print(original)
        get=True
        break
if get==False:
    print(0)
    