import sys
num=int(sys.stdin.readline())
for i in range(num):
    ans=0
    newLine=list(map(str, sys.stdin.readline().split()))
    for j in range(len(newLine)):
        if newLine[j]=="@":
            ans*=3
        elif newLine[j]=="%":
            ans+=5
        elif newLine[j]=="#":
            ans-=7
        else:
            ans+=float(newLine[j])
    print("%.2f" % ans)

        
