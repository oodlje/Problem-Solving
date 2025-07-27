import sys
while True:
    try:
        a=0
        b=0
        c=0
        d=0
        # 소문자, 대문자, 숫자, 공백
        getString=sys.stdin.readline().rstrip('\n')
        if not getString:
            break
        for i in range (len(getString)):
            if getString[i]==" ":
                d+=1
            elif getString[i].islower():
                a+=1
            elif getString[i].isupper():
                b+=1
            else:
                c+=1  
        print(str(a)+" "+str(b)+" "+str(c)+" "+str(d))         
    except EOFError:
        break