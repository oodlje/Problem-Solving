import sys
num=int(sys.stdin.readline())
first=[0]*num
for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    first[i]=[a,b]
first.sort()
#sort하면 0번째 index기준 정렬 이후 두 번째 index 기준 정렬 완료
for i in range(num):
    print(str(first[i][0])+" "+str(first[i][1]))
# print(first)
# prev=first[0][0]
# secondSort=[first[0]]
# final=[first[0]]
# for i in range(1,num,1):
#     if (first[i][0]==prev):
#         secondSort.append(first[i])
#     else:
#         secondSort.sort()
#         final.append(secondSort)
#         secondSort=[]
#         prev=first[i][0]
# print(final)

    