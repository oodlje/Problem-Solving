import sys
m,n=map(int,sys.stdin.readline().split())
array=[0]
for i in range(m):
    array.append(i+1)
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    array[a],array[b]=array[b],array[a]
array.pop(0)
print(*array)
    

    
    
