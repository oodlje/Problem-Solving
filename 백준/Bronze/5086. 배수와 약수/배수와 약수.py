import sys
while True:
    num=list(map(int,sys.stdin.readline().split()))
    if(num[1]==0&num[0]==0):
        break
    elif num[0]%num[1]==0:
        print("multiple")
    elif num[1]%num[0]==0:
        print("factor")
    else:
        print("neither")
