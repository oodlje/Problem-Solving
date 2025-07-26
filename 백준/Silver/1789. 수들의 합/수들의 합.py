import sys
s=int(sys.stdin.readline())
add=1
sum=0
while True:
    sum+=add
    if sum==s:
        print(add)
        break
    elif sum>s:
        print(add-1)
        break
    add+=1
