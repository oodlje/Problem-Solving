import sys
while True:
    num=list(map(int,sys.stdin.readline().split()))
    if (num[0]==0)&(num[1]==0)&(num[2]==0):
        break
    maxLen=max(num)
    sum=0
    for i in range(3):
        sum+=num[i]
    if maxLen>=(sum-maxLen):
        print("Invalid")
        continue
    if num[0]==num[1]:
        if num[1]==num[2]:
            print("Equilateral")
        else: 
            print("Isosceles")
    else:
        if num[1]==num[2]:
            print("Isosceles")
        elif num[0]==num[2]:
            print("Isosceles")
        else:
            print("Scalene")

