import sys
num=int(sys.stdin.readline())
confer=[]
for i in range (num):
    a,b=map(int,sys.stdin.readline().split())
    confer.append([a,b])

# 빨리 끝나는 순으로 정렬
confer.sort(key=lambda x: [x[1],x[0]])

# start, end 값을 새로 갱신하기
# confer[i][0]=start, confer[i][1]=end

count=1
end=confer[0][1]
for i in range(1,num):
    start=confer[i][0]
    if(start>=end):
        count+=1
        end=confer[i][1]
    
print(count)