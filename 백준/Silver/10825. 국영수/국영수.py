num=int(input())
nameList=[[] for _ in range(num)]
for i in range(num):
    nameList[i]=list(map(str,input().split()))
    for j in range(3):
        nameList[i][j+1]=int(nameList[i][j+1])

nameList_sort=sorted(nameList,key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(num):
    print(nameList_sort[i][0])