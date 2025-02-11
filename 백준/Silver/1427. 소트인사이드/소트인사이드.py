import sys
#스트링은 item 수정 불가능
string=input()
string=list(string)
for i in range (len(string)):
    for j in range(i):
        if (int(string[i])>int(string[j])):
            small=string[i]
            big=string[j]
            string[i]=string[j]
            string[j]=small
for i in range(len(string)):
    print(string[i],end="")


