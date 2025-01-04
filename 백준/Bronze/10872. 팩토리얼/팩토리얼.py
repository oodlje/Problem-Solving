n=int(input())
cur=n
sum=1
if (n==0):
    print(1)
else:
    while(cur!=0):
        sum=sum*cur
        cur-=1  
    print(sum)