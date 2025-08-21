import sys
repeat=int(sys.stdin.readline())
award=[]
for _ in range(repeat):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b and b==c:
        award.append(10000 + a * 1000)
    elif a==b or b==c or a==c:
        if a == b:
            award.append(1000 + a * 100)
        elif b == c:
            award.append(1000 + b * 100)
        else:
            award.append(1000 + c * 100)
    else:
        award.append(max(a, b, c) * 100)
print(max(award))
