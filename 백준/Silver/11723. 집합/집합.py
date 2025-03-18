import sys
num=int(sys.stdin.readline())
current=set()
for _ in range(num):
    get=list(map(str,sys.stdin.readline().split()))
    if (len(get)==1):
        if (get[0]=="all"):
            current = set(range(1, 21))
        else:
            current=set()
    else:
        get[1]=int(get[1])
        if (get[0]=="add"):
            current.add(get[1])
        elif (get[0]=="remove"):
            if (get[1] in current):
                current.remove(get[1])
        elif(get[0]=="check"):
            if (get[1] in current):
                print(1)
            else:
                print(0)
        elif(get[0]=="toggle"):
            if(get[1] in current):
                current.remove(get[1])
            else:
                current.add(get[1])


            
