import sys
a=int(sys.stdin.readline())
star=["*" for _ in range(a)]
for i in range(a):
    if i%2==0:
        print(" ".join(star))
    else:
        print(" "+" ".join(star))