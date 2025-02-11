import sys
num, gap=map(int,sys.stdin.readline().split())
seq=list(map(int,sys.stdin.readline().split()))
add=[0]*num
sum=[0]*num
for i in range(num):
    if (i==0):
        add[0]=seq[0]
    else:
        add[i]=seq[i]+add[i-1]
#num-1=-1이면 반복문 미통과
for i in range(num-1,-1,-1):
    if (((i+1)-gap)<0):
        break
    if ((i+1)-gap==0):
        sum[i]=add[i]
    else:
        sum[i]=add[i]-add[(i)-gap]

max=sum[gap-1]
for i in range(gap-1,num,1):
    if(max<sum[i]):
        max=sum[i]
print(max)
# print(add)
# print(sum)






