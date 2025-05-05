import sys
num=0
score=0
for i in range(20):
    a,b,c=map(str,sys.stdin.readline().split())
    if c=="P":
        continue
    else:
        if c=="A+":
            alpha=4.5
        elif c=="A0":
            alpha=4.0
        elif c=="B+":
            alpha=3.5
        elif c=="B0":
            alpha=3.0
        elif c=="C+":
            alpha=2.5
        elif c=="C0":
            alpha=2.0
        elif c=="D+":
            alpha=1.5
        elif c=='D0':
            alpha=1.0
        else:
            alpha=0
    
    score+=float(float(b)*alpha)
    num+=float(b)
print(score/num)
