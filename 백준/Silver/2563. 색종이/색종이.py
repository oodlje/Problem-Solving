import sys
num=int(sys.stdin.readline())
array=[[0]*100 for _ in range(100)]
count=0
for _ in range(num):
    x,y=map(int,sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            array[x+i][y+j]=1

for i in range(100):
    for j in range(100):
        if array[i][j]:
            count+=1
print(count)