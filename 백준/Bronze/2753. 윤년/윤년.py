import sys
num=int(sys.stdin.readline())
if num%4==0:
    if num%400==0:
        print(1)
    elif num%100!=0:
        print(1)
    else:
        print(0)
else:
    print(0)