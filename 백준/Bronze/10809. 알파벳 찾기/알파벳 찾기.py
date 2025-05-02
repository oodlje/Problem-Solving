import sys
new=list(map(str,sys.stdin.readline()))
alpha="abcdefghijklmnopqrstuvwxyz"
loc=[-1]*len(alpha)
for i in range(len(new)):
    for j in range(len(alpha)):
        if new[i]==alpha[j] and loc[j]==-1:
            loc[j]=i
print(*loc)