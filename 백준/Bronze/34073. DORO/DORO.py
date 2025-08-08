import sys
num=int(sys.stdin.readline().strip())
sentence=list(map(str,sys.stdin.readline().strip().split()))
for i in range(num):
    sentence[i]=sentence[i]+"DORO"
print(" ".join(sentence))



            