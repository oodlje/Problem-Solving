import sys
num = int(sys.stdin.readline().strip())
for _ in range (num):
    top=0
    stack=[]
    flag=True
    get=sys.stdin.readline()
    for i in range (len(get)):
        if get[i]=="(":
            stack.append(get[i])
            top+=1
        elif get[i]==")":
            if (stack):
                stack.pop()
                top-=1
            else:
                flag=False
    

    if (flag==True)&(top==0):
        # 조건문 괄호 따로 쓰기
        print("YES")
    else:
        print("NO")