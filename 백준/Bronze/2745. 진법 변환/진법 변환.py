import sys
num=list(map(str,sys.stdin.readline().split()))
sum=0
loc=0
for i in range(len(num[0])):
    cal=int(num[1])**loc
    if num[0][len(num[0])-i-1].isdigit():
        sum+=int(num[0][len(num[0])-i-1])*cal
    else:
        sum+=(ord(num[0][len(num[0])-i-1])-55)*cal
    loc+=1

print(sum)
