n=int(input())
##arr=[[0]*4]*n: 모든 하위 리스트가 같은 객체를 참조하게 됨
arr = [[0] * 4 for _ in range(n)]
for i in range (n):
    get=int(input())
    arr[i][0]=int(get/25)
    get=get%25
    arr[i][1]=int(get/10)
    get=get%10
    arr[i][2]=int(get/5)
    get=get%5
    arr[i][3]=int(get/1)
    get=get%1

for i in range(n):
    for j in range(4):
        print(arr[i][j],"", end="")
    print("")

