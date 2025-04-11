left={}
for i in range(10):
    get=int(input())
    num=int(get%42)
    if left.get(num):
        left[num]+=1
    else:
        left[num]=1
print(len(left.items()))
