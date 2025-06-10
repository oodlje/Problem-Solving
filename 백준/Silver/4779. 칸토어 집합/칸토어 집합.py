# 하나의 문자열로 저장하고 slicing, 3의 중간을 쪼개는 시점이 오면 stop
# import sys
def deleteMiddle(n):
    start=0
    if n==1:
        return ''.join(cantor)
    else:
        while start<(len(cantor)-1):
            if cantor[start]=="-":
                #slicing된 범위 길이만큼 multiple해서 replace 해야함"
                cantor[start+int(n/3):start+int(n/3)*2]=" "*(n//3)
            start+=n
        return deleteMiddle(n//3)

while True:
    try: 
        num=int(input())
        cantor=["-" for _ in range(3**num)]
        print(deleteMiddle(3**num))
    except EOFError:
        break
    

