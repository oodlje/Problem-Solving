import sys
get=sys.stdin.readline().strip()
#문자열 슬라이싱은 [a:b]일때 항상 a<b
seq={}
num=0
#길이 변수
for i in range(len(get)):
    #시작 위치 변수
    for j in range(i+1,len(get)+1):
        if (not seq.get(get[i:j])):
            seq[get[i:j]]=True
for k,v in seq.items():
    num+=1
print(num)
