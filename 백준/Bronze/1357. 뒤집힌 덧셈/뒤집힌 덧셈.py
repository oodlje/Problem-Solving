import sys
def rev(num):
    for i in range(int(len(num)//2)):
        num[i],num[len(num)-1-i]= num[len(num)-1-i],num[i]
    return ''.join(num)
        
a,b=map(str,sys.stdin.readline().split())
a=list(a)
b=list(b)
sum=int(rev(a))+int(rev(b))
ans=list(rev(list(str(sum))))
while ans[0]=="0":
    ans.pop(0)
print(''.join(ans))
