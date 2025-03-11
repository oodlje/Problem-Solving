import sys
n=int(sys.stdin.readline())
word={}
for i in range(n):
    new=sys.stdin.readline().strip()
    if new in word.keys():
        word[new]+=1
    else:
        word[new]=1
# print(word)
freq=max(word.values())
ans=[]
# freq값이 갱신될때마다 ans값이 append되니까 오류생김 
for key,values in word.items():
    if (values==freq):
        freq=values
        ans.append(key)
ans=sorted(ans)
print(str(ans[0]))
# print(" "+str(freq))