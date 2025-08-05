import sys
a=int(sys.stdin.readline())
fruit={}
ring="NO"
for i in range(a):
    which, num=map(str,sys.stdin.readline().split())
    if fruit.get(which):
        fruit[which]+=int(num)
    else:
        fruit[which]=int(num)
for k,v in fruit.items():
    if v==5:
        ring="YES"
print(ring)
         

            