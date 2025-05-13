import sys
get=set(map(str, sys.stdin.readline()))
new=list(map(str,sys.stdin.readline()))
ans=""
for i in range(len(new)):
    if new[i] in get:
        continue
    else:
        ans+=new[i]


print(ans)