import sys
num=int(sys.stdin.readline())
first=[0]*num
for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    first[i]=[b,a]
first.sort()
#sort하면 0번째 index기준 정렬 이후 두 번째 index 기준 정렬 완료
for i in range(num):
    print(str(first[i][1])+" "+str(first[i][0]))