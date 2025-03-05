import sys
a=int(sys.stdin.readline())
x=[0]*a
y=[0]*a
for i in range(a):
    x[i],y[i]=map(int,sys.stdin.readline().split())

print((max(x)-min(x))*(max(y)-min(y)))