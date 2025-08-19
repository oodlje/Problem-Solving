import sys
n=int(sys.stdin.readline())
for i in range(n):
    s=list(sys.stdin.readline().strip())
    for j in range(len(s)):
        if s[j].isupper():
            s[j]=s[j].lower()
    print(''.join(s))
    
