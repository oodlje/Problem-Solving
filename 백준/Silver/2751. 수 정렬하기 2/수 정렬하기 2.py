import sys
#스트링은 item 수정 불가능
num=int(sys.stdin.readline())
array=[0]*num
for i in range (num):
    array[i]=int(sys.stdin.readline())
array.sort()
for i in range (num):
    print(array[i])


