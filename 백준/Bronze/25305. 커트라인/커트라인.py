import sys
a,b=map(int,sys.stdin.readline().split())
array=list(map(int,sys.stdin.readline().split()))
count=0
while (count!=b):
    biggest=max(array)
    for i in range(len(array)):
        if (array[i]==biggest):
            array.pop(i)
            break
    count+=1

print(biggest)
