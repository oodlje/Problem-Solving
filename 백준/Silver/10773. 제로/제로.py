import sys
num=int(input())
array=[]
for i in range (num):
    get=int(input())
    if (get==0):
        del array[-1]
    else:
        array.append(get)
sum=0
for i in range (len(array)):
    sum+=array[i]
print(sum)



    



    




