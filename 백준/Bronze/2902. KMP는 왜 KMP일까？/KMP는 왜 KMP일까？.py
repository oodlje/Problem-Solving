import sys
full=(sys.stdin.readline().strip())
ans=[]
for i in range(len(full)):
    if i==0:
        ans.append(full[i])
    elif full[i]=="-":
        ans.append(full[i+1])

print("".join(ans))