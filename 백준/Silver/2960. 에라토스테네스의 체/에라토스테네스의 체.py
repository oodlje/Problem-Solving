import sys
import math
n,k=map(int,sys.stdin.readline().split())
prime=[0]*n
count=0
fin=0
#n보다 작은 수 돌면서 나눠지지 않으면 소수
#해당 소수의 배수도 모두 1로 초기화
#1로 초기화된 경우에는 패스
#k=1인 상황 고려하기

for i in range(2,(n+1),1):
    if(fin==1):
        break
    # print(prime)
    if (prime[i-1]==1):
        continue
    pri=True
    for j in range(2,i,1):
        if ((i%j)==0):
            pri=False
    if (pri==True):
        count+=1
        prime[i-1]=1
        if (count==k):
            print(i)
            fin=1
            break
        state=2
        while (1):
            if (i*state<=n):
                if(prime[i*state-1]==0):
                    prime[i*state-1]=1
                    count+=1
                    if (count==k):
                        print(i*state)
                        fin=1
                        break
                state+=1
            else:
                break

        # if (fin==1):
        #     break


        



    


    
