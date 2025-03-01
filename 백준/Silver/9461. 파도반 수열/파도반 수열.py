import sys
count=int(sys.stdin.readline())
testCase=[]

def fibDynamic(num):
    if (num==1)or(num==2)or(num==3):
        return 1
    else:
        f[1]=1
        f[2]=1
        f[3]=1
        for i in range(3,num+1):
            f[i]=f[i-2]+f[i-3]
        return(f[num])


for i in range (count):
    num=int(sys.stdin.readline())
    testCase.append(num)
    f=[0]*(num+1)
    print(fibDynamic(num))
