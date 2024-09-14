import sys
num, getname=list(map(str,sys.stdin.readline().split()))
newname=[]
count=0
for i in range(len(getname)):
    if getname[i] not in newname:
        newname.append(getname[i])
    else:
        count+=1
newname.append(str(count+4))
for i in range (len(newname)):
    newname=''.join(newname)
getnum=int(num)+1906
newname=str(getnum)+str(newname)

reverse=[0]*len(newname)
for i in range (len(newname)):
    reverse[len(newname)-1-i]=newname[i]
reverse=''.join(reverse)
result="smupc_"+str(reverse)
print(result)

