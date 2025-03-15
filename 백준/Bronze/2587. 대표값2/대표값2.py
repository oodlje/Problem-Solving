import sys
get=[]
sum=0
for i in range(5):
    add=int(input())
    get.append(add)
    sum+=add
get.sort()
print(sum//5)
print(get[2])