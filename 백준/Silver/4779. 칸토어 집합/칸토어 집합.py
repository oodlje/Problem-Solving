# 하나의 문자열로 저장하고 slicing, 3의 중간을 쪼개는 시점이 오면 stop
# 분할정복 리팩토링
def deleteMiddle(n):
    if n==1:
        return "-"
    else:
        middle=" "*(n//3)
        return deleteMiddle(n//3)+middle+deleteMiddle(n//3)
while True:
    try: 
        num=int(input())
        print(deleteMiddle(3**num))
    except EOFError:
        break
    

