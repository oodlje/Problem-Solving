import sys
num=int(sys.stdin.readline())
get=list(map(int,sys.stdin.readline().split()))
numFind=int(sys.stdin.readline())
getFind=list(map(int,sys.stdin.readline().split()))
get.sort()

for i in range(numFind):
    left=0
    right=num-1
    find=False
    while (left<=right):
        mid=int((left+right)/2)
        if (getFind[i]==get[mid]):
            find=True
            print(1)
            break
        else:
            if (getFind[i]<get[mid]):
                right=mid-1
            else:
                left=mid+1
    if (find==False):
        print(0)
