import sys
word=list(map(str,sys.stdin.readline().strip()))
ans=[]
for i in range(len(word)):
    ans.append(''.join(word[i:]))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
