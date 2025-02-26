import sys
num=int(sys.stdin.readline())
start=1
count=0
while (1):
    if "666" in str(start):
        count+=1
    if (count==num):
        print(start)
        break
    else:
        start+=1
        continue