import sys

x,y,w,h=map(int,sys.stdin.readline().split())

xMin=min(w-x,x)
yMin=min(h-y,y)
print(min(xMin,yMin))




    
    