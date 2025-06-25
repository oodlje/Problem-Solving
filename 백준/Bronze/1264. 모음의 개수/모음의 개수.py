import sys
myList=['a','e','i','o','u','A','E','I','O','U']
while True:
    new=sys.stdin.readline().strip()
    if new=="#":
        break
    else:
        ans=0
        for i in range(len(new)):
            if new[i] in myList:
                ans+=1
        print(ans)