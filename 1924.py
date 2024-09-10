month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
numList=list(map(int,input().split()))
alladd=0
output=""
mon=int(numList[0])
date=int(numList[1])
for i in range(mon):
    alladd=alladd+int(month[i])
alladd=alladd+date
if alladd%7==1:
    output="MON"
elif alladd%7==2:
    output="TUE"
elif alladd%7==3:
    output="WED"
elif alladd%7==4:
    output="THU"
elif alladd%7==5:
    output="FRI"
elif alladd%7==6:
    output="SAT"
elif alladd%7==0:
    output="SUN"
print(output)