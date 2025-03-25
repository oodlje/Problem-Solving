a=int(input())
b=int(input())
#소수인것 찾기
list=[]
for i in range(a,b+1):
    prime=True
    if (i==1):
        prime=False
    for j in range(2,i):
        if (i%j==0):
            prime=False
            break
    if (prime):
        list.append(i)

if (len(list)==0):
    print(-1)
else:
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    print(sum)
    print(list[0])