import sys
dial=sys.stdin.readline().strip()
exception={18,21,24,25}
sum=0
for i in range(len(dial)):
    getNum=int(ord(dial[i])-65)
    if getNum in exception:
        ans=int(getNum/3)+2
    else:
        ans=int(getNum/3)+3
    sum+=ans
print(sum)

    



