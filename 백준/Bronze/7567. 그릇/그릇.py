import sys
plate=sys.stdin.readline().strip()
past=""
ans=0
for i in range(len(plate)):
    if past=="" or plate[i]!=past:
        ans+=10
    else:
        ans+=5
    past=plate[i]
print(ans)