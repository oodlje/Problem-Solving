import sys
ans=[]
for i in range(5):
    get=str(sys.stdin.readline().strip())
    check=False
    if len(get)>10:
        continue
    for j in range(len(get)):
        if get[j].isupper() or get[j].isdigit() or get[j]=="-":
            check=True 
        else:
            break
    if check==True:
        if "FBI" in get:
            ans.append(i+1)
if len(ans)==0:
    print("HE GOT AWAY!")
else:
    print(" ".join(map(str,ans)))