import sys
num=int(sys.stdin.readline())
string=str(sys.stdin.readline())
ans=0
for i in range (num):
    ans+=(ord(string[i])-ord('a')+1)*(31**i)
ans=ans%1234567891
print(ans)
