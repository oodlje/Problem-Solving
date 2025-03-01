import sys
num=int(sys.stdin.readline())
f=[0]*(num+1)
#재귀 호출과 동적 프로그래밍 비교
count2=0
# def fib(n):
#     global count1
#     if (n==1 or n==2):
#         return 1
#     else:
#         count1+=1
#         return fib(n-1)+fib(n-2)

def fibDynamic(num):
    global count2
    f[1]=1
    f[2]=1
    for i in range(3,num+1):
        count2+=1
        f[i]=f[i-1]+f[i-2]
    return f[num]

print(str(fibDynamic(num))+" "+str(count2))