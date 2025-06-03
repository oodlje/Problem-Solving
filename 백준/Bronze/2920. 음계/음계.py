import sys

def song(newList):
    asc=[1,2,3,4,5,6,7,8]
    des=[8,7,6,5,4,3,2,1]
    if newList[0]==1:
        for i in range(8):
            if asc[i]!=newList[i]:
                return "mixed"
        return "ascending"
    elif newList[0]==8:
        for i in range(8):
            if des[i]!=newList[i]:
                return "mixed"
        return "descending"
    else:
        return "mixed"

newList=list(map(int, sys.stdin.readline().split()))
print(song(newList))


