import sys
num=int(sys.stdin.readline())
if num==0:
    print(0)
elif num==1:
    print(1)
elif num==2:
    print(1)
else:
    a=0
    b=1
    for i in range(num-1):
        new=a+b
        a=b
        b=new
    print(new)


        