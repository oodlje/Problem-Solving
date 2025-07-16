import sys
for _ in range(3):
    add=0
    num=int(sys.stdin.readline())
    for _ in range(num):
        cur=int(sys.stdin.readline())
        add+=cur
    if add==0:
        print(0)
    elif add>0:
        print("+")
    else:
        print("-")