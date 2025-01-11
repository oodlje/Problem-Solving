import sys
num=list(map(int,sys.stdin.readline().split()))
myList=[]
for i in range (num[0]):
        if (num[0]%(i+1)==0):
                myList.append(i+1)

if len(myList)>=num[1]:
        print(myList[num[1]-1])
else:
        print(0)
        