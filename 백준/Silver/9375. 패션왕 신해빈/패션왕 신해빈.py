import sys
n=int(sys.stdin.readline())

for i in range(n):
    k=int(sys.stdin.readline())
    wear={}
    for _ in range(k):
        a,b=sys.stdin.readline().split()
        if b in wear.keys():
            wear[b]+=1
        else:
            wear[b]=1
    sum=1      
    for key, value in wear.items():
        sum=sum*(value+1)
    #print(wear)
    print(sum-1)



