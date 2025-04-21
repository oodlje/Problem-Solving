time=int(input())
count=0
for i in range(time):
    log=input()
    if log=="ENTER":
        gom=set()
    else:
        if not log in gom:
            gom.add(log)
            count+=1
print(count)
