testCase=int(input())
for i in range(testCase):
    set1={}
    length=int(input())
    plain=[""]*(length+1)
    open1=list(map(str,input().split()))
    open2=list(map(str,input().split()))
    crypt=list(map(str,input().split()))
    for i in range(length):
        set1[open1[i]]=[i+1]
    for i in range(length):
        set1[open2[i]].append(i+1)
    for v in set1.values():
        plain[v[0]]=crypt[v[1]-1]
    plain=plain[1:]
    print(*plain)

        



