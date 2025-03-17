
for i in range(9):
    get=int(input())
    if (i==0):
        max=get
        index=0
    else:
        if (max<get):
            max=get
            index=i
print(max)
print(index+1)