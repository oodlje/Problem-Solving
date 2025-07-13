import sys
num=int(sys.stdin.readline())
nameSet={}
moreFive=False
lastName=[]
for i in range(num):
    getName=sys.stdin.readline().strip()
    if getName[0] in nameSet:
        nameSet[getName[0]]+=1
    else:
        nameSet[getName[0]]=1
for k,v in nameSet.items():
    if v>=5:
        lastName.append(k[0])
        moreFive=True
if (moreFive==True):
    lastName.sort()
    print("".join(lastName))
else:
    print("PREDAJA")    

