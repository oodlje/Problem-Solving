import sys
newLine=list(map(str,sys.stdin.readline().strip()))
ans=0
for i in range(len(newLine)-3):
    if ("".join(newLine[i:i+4])=="DKSH"):
        ans+=1
print(ans)