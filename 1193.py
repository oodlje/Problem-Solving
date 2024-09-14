given=int(input())
minus=1
left=int(given)
while (left-minus)>0:
    left=left-minus
    minus+=1
add=minus+1
#add는 분모분자 더한 값
if (add%2==0):
    #분모가 커지는 방향
    son=str(add-left)
    print(son+"/"+str(left))
else:
    mother=str(add-left)
    print(str(left)+"/"+mother)

