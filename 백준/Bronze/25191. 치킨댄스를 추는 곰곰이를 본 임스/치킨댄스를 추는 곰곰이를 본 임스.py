import sys
chicken=int(sys.stdin.readline().strip())
a,b=map(int, sys.stdin.readline().strip().split())
total=a//2+b
print(total) if chicken>=total else print(chicken)


            