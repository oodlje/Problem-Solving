import sys
a,b=map(int,sys.stdin.readline().split())
chess=[0]*a
error=0
minNum=64
for i in range(a):
    chess[i]=sys.stdin.readline()


maxA=a-8
maxB=b-8
for k in range (maxA+1):
    for l in range (maxB+1):
        error=0
        if (chess[k][l]=='W'):
                status='W'
        else:
                status='B'

        for i in range(k,k+8):
            for j in range(l,l+8):
                if (chess[i][j]!=status):
                    error+=1
                if (status=='W'):
                    status='B'
                else:
                    status='W'
            if (status=='W'):
                status='B'
            else:
                status='W'
        if (min(error,64-error)<minNum):
            minNum=min(error, 64-error)
      
print(minNum)
