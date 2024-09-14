get=str(input())
get=get.upper()
word={}
max=0
for i in range(len(get)):
    if get[i] in word:
        word[get[i]]=word[get[i]]+1
    else:
        word[get[i]]=1
for key,value in (word.items()):
    if max<value:
        max=value
        maxWord=key
    elif max==value:
        maxWord="?"
print(maxWord)
