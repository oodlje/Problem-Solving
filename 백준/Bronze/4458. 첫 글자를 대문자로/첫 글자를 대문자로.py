import sys
num=int(sys.stdin.readline())
for i in range (num):
    sentence=list(map(str,sys.stdin.readline().split()))
    for j in range(len(sentence)):
        if j==0:
            sentence[j]=sentence[j][0].upper()+sentence[j][1:]
            break
    print(" ".join(sentence))
    