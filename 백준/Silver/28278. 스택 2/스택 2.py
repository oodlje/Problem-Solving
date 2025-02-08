

# append가 아닌 인덱스값 조정으로 stack 구현하기
import sys
stack=[-1]*1000000
i=0
num = int(sys.stdin.readline().strip())

for _ in range(num):
    get = sys.stdin.readline().split()
    if (get[0]=='1'):
        stack[i]=get[1]
        i+=1
    elif (get[0]=='2'):
        if (i==0):
            print(-1)
        else:
            print(stack[i-1])
            stack[i-1]=-1
            i-=1
    elif (get[0]=='3'):
        print(i)
    elif (get[0]=='4'):
        if i==0:
            print(1)
        else:
            print(0)
    elif (get[0]=='5'):
        if (i==0):
            print(-1)
        else:
            print(stack[i-1])


    
