import sys
a=int(sys.stdin.readline())
pwSet=set()
for i in range(a):
    pw=str(sys.stdin.readline().strip())
    if pw in pwSet:
        ans=pw[len(pw)//2]
        ansLen=len(pw)
        break
    else:
        originpw=pw
        pw=list(pw)
        for j in range(len(pw)//2):
            pw[j],pw[len(pw)-1-j]=pw[len(pw)-1-j],pw[j]
        pw=''.join(pw)
        if originpw==pw:
            ans=pw[len(pw)//2]
            ansLen=len(pw)
        pwSet.add(pw)
print(ansLen)
print(ans)

            