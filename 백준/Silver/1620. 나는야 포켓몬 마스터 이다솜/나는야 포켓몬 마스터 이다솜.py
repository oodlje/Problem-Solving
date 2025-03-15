import sys
a,b=map(int,sys.stdin.readline().split())
pok={}
# key, value 값 뒤집어서 저장
revPok={}
for i in range(a):
    name=sys.stdin.readline().strip()
    pok[name]=i+1
    revPok[i+1]=name

for i in range(b):
    find=sys.stdin.readline().strip()
    if find.isdigit():
        print(revPok[int(find)])
    else:  print(pok[find])
