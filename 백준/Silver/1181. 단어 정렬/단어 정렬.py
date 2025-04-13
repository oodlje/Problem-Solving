num=int(input())
arr=[]
word={}
for i in range(num):
    std=input()
    if word.get(std):
        word[std]+=1
    else:
        word[std]=0
for k,v in word.items():
    arr.append([len(k),k])
ans=sorted(arr,key=lambda x:[x[0],x[1]])
for i in range(len(ans)):
    print(str(ans[i][1]))