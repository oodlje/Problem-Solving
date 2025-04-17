import sys
total=int(sys.stdin.readline())
num=int(sys.stdin.readline())
add=0
for i in range(num):
    price,n=map(int,sys.stdin.readline().split())
    add+=price*n
if (add==total):
    print("Yes")
else:
    print("No")