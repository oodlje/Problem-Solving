import sys
clock=list(map(int,sys.stdin.readline().split()))
add=int(input())
clock[1]+=add
addHour=int(clock[1]/60)
if clock[1]>=60:
     clock[1]-=60*addHour  
     clock[0]+=addHour
     if clock[0]>=24:
          clock[0]=0+(clock[0]-24)

print(int(clock[0]),int(clock[1]))