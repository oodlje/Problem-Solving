import sys
num=int(sys.stdin.readline())
length=num*2-1
star=list(" "*(num-1))
star.append("*")
startL=num-1
startR=num-1
print("".join(star))
for i in range(num-1):
    star[startL-1]="*"
    star.append("*")
    startL-=1
    startR+=1
    print("".join(star))

