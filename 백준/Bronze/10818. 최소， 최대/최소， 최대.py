import sys
a=int(input())
get=list(map(int,sys.stdin.readline().split()))
print(str(min(get))+" "+str(max(get)))
