import sys
while True:
    get=sys.stdin.readline().strip()
    if get=="0":
        break
    ans=len(get)+1
    for i in range(len(get)):
        if get[i]=="0":
            ans+=4
        elif get[i]=="1":
            ans+=2
        else:
            ans+=3
    print(ans)


            