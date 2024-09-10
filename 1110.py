plus=[0]*3
count=0
a=int(input())
newa=0
plus[0]=int(a/10)
plus[1]=int(a%10)
while (True):
    add=int(plus[0]+plus[1])
    add=int(add%10)
    newa=int(str(plus[1])+str(add))
    count=count+1
    if int(newa)==a:
        print(count)
        break
    else:
        plus[0]=int(newa/10)
        plus[1]=int(newa%10)
