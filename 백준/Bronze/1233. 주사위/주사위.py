import sys
a,b,c=map(int,sys.stdin.readline().split())
dice={}
biggest=0
for i in range(1, a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            ans=i+j+k
            if dice.get(ans):
                dice[ans]+=1
            else:
                dice[ans]=1
for k,v in dice.items():
    if v>biggest:
        biggest=v
        res=k
        
print(res)
    
