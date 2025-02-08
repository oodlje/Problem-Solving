import sys

while (1):
    top=0
    stack=[]
    flag=True
    # get=sys.stdin.readline()
    get=input()
    if (get=="."):
        break
    if get[-1]!=".":
        flag=False
    for i in range (len(get)):
        if get[i]=="(":
            stack.append(get[i])
            top+=1
        elif get[i]==")":
            if (stack):
                if (stack[-1]=="("):
                    stack.pop()
                    top-=1
                else:
                    flag=False
            else:
                flag=False
        elif get[i]=="[":
            stack.append(get[i])
            top+=1
        elif get[i]=="]":
            if (stack):
                if (stack[-1]=="["):
                    stack.pop()
                    top-=1
                else:
                    flag=False
            else:
                flag=False

    if (flag==True)and(top==0):
        # 조건문 괄호 따로 쓰기
        print("yes")
    else:
        print("no")

