import sys
num,b=map(int,sys.stdin.readline().split())
ans=[]
divide=num
while (b<=divide):
    left=int(num%b)
    divide=int(num/b)
    ans.append(left)
    num=divide
ans.append(divide)
while len(ans)!=0:
    getAns=ans.pop()
    if getAns>=10:
        getAns=chr(getAns+55)
    print(getAns,end="")
    
print("")

    



