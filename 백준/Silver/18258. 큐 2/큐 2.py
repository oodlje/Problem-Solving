import sys
num = int(sys.stdin.readline().strip())
queue=[]
index=0
#queue배열 만들어서 앞자리 index부터 pop 될 때 index값 하나씩 올리기
for i in range(num):
    get=list(sys.stdin.readline().split())
    if (get[0]=='push'):
        queue.append(get[1])
    elif (get[0]=='pop'):
        if (index==len(queue)):
            print(-1)
        else:
            print(queue[index])
            index+=1
    elif (get[0]=='size'):
        print(len(queue)-index)
    elif (get[0]=='empty'):
        if (index==len(queue)):
            print(1)
        else:
            print(0)
    elif (get[0]=='front'):
        if (index==len(queue)):
            print(-1)
        else:
            print(queue[index])
    elif (get[0]=='back'):
        if (index==len(queue)):
            print(-1)
        else:
            print(queue[-1])






    
