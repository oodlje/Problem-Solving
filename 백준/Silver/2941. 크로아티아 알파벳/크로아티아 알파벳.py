import sys
# 문자열 길이 2개, 3개로 쪼개서 생각?
len2={"c=","c-","d-","lj","nj","s=","z="}
len3={"dz="}
word=str(sys.stdin.readline())
cur=0
ans=0
while True:
    #마지막 원소면 out 
    if cur>=(len(word)-1):
        break
    if word[cur:cur+2] in len2:
        cur+=2  
    elif cur<=(len(word)-2) and word[cur:cur+3] in len3:
        cur+=3
    else:
        cur+=1
    ans+=1
print(ans)
    
