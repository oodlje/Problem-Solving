import sys
num=int(sys.stdin.readline())
b=int(num/5)
count=-1
a=num
while (b>0):
    if (((num-(5*b))%3)==0):
        # 최소 a 갱신
        if (a>((num-b*5)/3)):
            a=int((num-b*5)/3)
    b-=1

if (num%3==0):
    if (a>num/3):
        a=int(num/3)

if (a==num):
    ans=-1
else:
    ans=a+int((num-a*3)/5)

print(ans)

