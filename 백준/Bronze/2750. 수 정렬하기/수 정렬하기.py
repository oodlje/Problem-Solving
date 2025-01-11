import sys
num=int(input())
myList=[]
for i in range(num):
    get=int(input())
    myList.append(get)
myList.sort()
for i in range(num):
    print(myList[i])
