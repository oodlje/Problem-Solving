import sys
a,b=map(int,sys.stdin.readline().split())
people=list(map(int,sys.stdin.readline().split()))
ans=int(a*b)
diff=[]
for i in range(5):
    diff.append(str(people[i]-ans))
print(" ".join(diff))

            