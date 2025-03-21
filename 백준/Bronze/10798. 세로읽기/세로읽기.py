import sys
get=[0]*5
maxLen=0
for i in range(5):
    get[i]=sys.stdin.readline().strip()
    if (len(get[i])>maxLen):
        maxLen=len(get[i])

for i in range(maxLen):
    for j in range(5):
        if (len(get[j])>(i)):
            print(get[j][i],end="")
