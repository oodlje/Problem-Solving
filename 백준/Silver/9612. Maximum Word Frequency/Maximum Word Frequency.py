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
freq=0
ans=[]
for key,values in word.items():
    if (values>=freq):
        freq=values
        ans.append(key)
ans.sort(reverse=True)
print(str(ans[0]), end="")
print(" "+str(freq))