#삽입 정렬이 아닌 람다 함수로 구현
import sys
num=int(sys.stdin.readline())
first=[sys.stdin.readline().split() for _ in range(num)]
# first=[0]*num
# for i in range(num):
#     a,b=map(str,sys.stdin.readline().split())
#     first[i]=[a,b]
first.sort(key=lambda x: int(x[0]))
#첫 번째 인자를 기준으로 정렬

# for i in range(num):
#     status=i
#     for j in range(i,-1,-1):
#         if (int(first[status][0])<int(first[j][0])):
#             store=first[j]
#             first[j]=first[status]
#             first[status]=store
#             status=j
for i in range(num):
    print(str(first[i][0])+" "+str(first[i][1]))



    


    
