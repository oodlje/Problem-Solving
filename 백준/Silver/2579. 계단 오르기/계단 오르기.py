import sys
num = int(sys.stdin.readline().strip())
stair=[0]*num
for i in range(num):
    stair[i]=int(sys.stdin.readline().strip())
point=[0]*num
step=0
#현재 최댓값=이전포인트의 최댓값+현재포인트
for i in range(num):
    #전 계단 or 전전계단에서 올라오는 경우
    if (i==0):
        point[i]=stair[i]
    elif (i==1):
        point[i]=point[i-1]+stair[i]
    elif (i==2):
        point[i]=max(stair[2]+stair[0],stair[2]+stair[1])
    else:
        point[i]=max(stair[i]+point[i-2], stair[i]+point[i-3]+stair[i-1])


print(point[num-1])

    
