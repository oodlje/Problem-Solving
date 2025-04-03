import sys
line=[0]*30
for i in range(28):
    get=int(sys.stdin.readline())
    line[get-1]=1
for i in range(30):
    if (line[i]==0):
        print(i+1)
    

    
