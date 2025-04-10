import sys
n,m=map(int,sys.stdin.readline().split())
rain=[[] for _ in range(n)]
for i in range(n):
    rain[i]=list(map(int,sys.stdin.readline().split()))
#시작 위치 좌표 저장 
start=[[n-2,0],[n-2,1],[n-1,0],[n-1,1]]
#방향 8개 좌표 저장
#1,3,5,7대각선 좌표자리 재사용
dir=[(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
for i in range(m):
    d,s=map(int,sys.stdin.readline().split())
    for i in range(len(start)):
        #방향만큼 이동
        start[i][0]+=dir[d-1][0]*s
        start[i][1]+=dir[d-1][1]*s
        while (start[i][0]<0):
            start[i][0]=(start[i][0])+(n)
        if (start[i][0]>=n):
            start[i][0]=start[i][0]%n
        while (start[i][1]<0):
            start[i][1]=(start[i][1])+(n)
        if (start[i][1]>=n):
            start[i][1]=start[i][1]%n
    #물 양 증가
    for i in range(len(start)):
        rain[start[i][0]][start[i][1]]+=1
    # print(rain)
    for i in range(len(start)):
        num=0
        for j in range(4):
            if (0<=(start[i][0]+dir[2*j+1][0])<n) and (0<=start[i][1]+dir[2*j+1][1]<n):
                if rain[start[i][0]+dir[2*j+1][0]][start[i][1]+dir[2*j+1][1]]>0:
                    num+=1
        rain[start[i][0]][start[i][1]]+=num
    start_set = set(map(tuple, start))
    #물 양 2씩 빼기
    startLen=len(start)
    for i in range(n):
        for j in range(n):
            if (i,j) in start_set:
                continue
            if rain[i][j]>=2:
                rain[i][j]-=2
                start.append([i,j])
    start = start[startLen:]
    # print(rain)
    # print(start)
rainSum=0
for i in range(n):
    for j in range(n):
        rainSum+=rain[i][j]
print(rainSum)
