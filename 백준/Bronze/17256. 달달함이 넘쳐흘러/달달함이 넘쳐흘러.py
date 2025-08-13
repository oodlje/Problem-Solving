import sys
ans=[]
ax,ay,az=map(int, sys.stdin.readline().split())
cx,cy,cz=map(int, sys.stdin.readline().split())

bx=cx-az 
by=cy//ay
bz=cz-ax
ans=[bx, by, bz]

print(" ".join(list(map(str,ans))))
