import sys
import math
num=int(sys.stdin.readline())
for _ in range(num):
    getNum=int(sys.stdin.readline())
    if getNum==0 or getNum==1:
        getNum=2
    while True:
        prime=True
        for j in range (2, int(math.sqrt(getNum)+1)):
            if (getNum%j)==0:
                prime=False
                break
        if prime:
            break
        else:
            getNum+=1
    print(getNum)
        

