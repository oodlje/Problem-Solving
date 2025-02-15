import sys
xAxis=[0]*1000
yAxis=[0]*1000
for _ in range(3):
    a,b=map(int,sys.stdin.readline().split())
    xAxis[a-1]+=1
    yAxis[b-1]+=1

for i in range(1000):
    if (xAxis[i]==1):
        x=i+1
    if (yAxis[i]==1):
        y=i+1

print(str(x)+" "+str(y))







    
    