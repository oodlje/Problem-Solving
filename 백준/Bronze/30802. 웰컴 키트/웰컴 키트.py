import sys
people=int(sys.stdin.readline())
size=list(map(int,sys.stdin.readline().split()))
t,p=map(int,sys.stdin.readline().split())
plus=0
for i in range(6):
    if int(size[i]%t)!=0:
        plus+=int(size[i]/t)+1
    elif int(size[i]%t)==0:
        plus+=int(size[i]/t)
penA=int(people/p)
penB=0
if int(people%p)!=0:
    penB=int(people%p)
print(plus)
print(str(penA)+" "+str(penB))