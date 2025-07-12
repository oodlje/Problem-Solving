import sys
find=[]
a,b=map(int,sys.stdin.readline().split())
find.append(a/b*1000)
num=int(sys.stdin.readline())
for i in range(num):
    c,d=map(int,sys.stdin.readline().split())
    gram=c/d
    find.append(gram*1000)
print(min(find))