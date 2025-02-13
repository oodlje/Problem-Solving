import sys
from collections import deque
#popleft, appendleft
#함수로 만들어버리면 dec.popleft()값을 먼저 확인하고 함수 실행하기때문에 에러 발생생
num=int(sys.stdin.readline())
dec=deque()
for i in range(num):
    get=list(map(int,sys.stdin.readline().split()))
    if (get[0]==1):
        dec.appendleft(get[1])
    elif(get[0]==2):
        dec.append(get[1])
    elif(get[0]==3):
        if(dec):
            print(dec.popleft())
        else:
            print(-1)
    elif(get[0]==4):
        if(dec):
            print(dec.pop())
        else:
            print(-1)
    elif(get[0]==5):
        print(len(dec))
    elif(get[0]==6):
        if(dec):
            print(0)
        else:
            print(1)
    elif(get[0]==7):
        if(dec):
            print(dec[0])
        else:
            print(-1)
    elif(get[0]==8):
        if(dec):
            print(dec[-1])
        else:
            print(-1)
    
    


