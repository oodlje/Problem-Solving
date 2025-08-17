import sys
ans={}
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    if ans.get(n):
        ans[n]+=1
    else:
        ans[n]=1
ans_list=[]
large_key=[]
large_value=0
for k,v in ans.items():
    for i in range(v):
        ans_list.append(k)
    if v > large_value:
        large_value = v
        large_key=[k]
    elif v==large_value:
        large_key.append(k)

ans_list.sort()
middle=ans_list[len(ans_list)//2] #중앙값
mean=round(sum(ans_list)/len(ans_list))
diff=ans_list[-1]-ans_list[0] #범위

print(mean)
print(middle)
large_key.sort()
if len(large_key)>1:
    print(large_key[1])
else:
    print(large_key[0])
print(diff)


