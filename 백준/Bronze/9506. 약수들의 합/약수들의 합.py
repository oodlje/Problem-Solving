import sys
while True:
        get=int(input())
        if (get==-1):
                break
        myList=[]
        for i in range(get):
                if get%(i+1)==0:
                        myList.append(i+1)
        sum=0
        for i in range (len(myList)-1):
                sum+=myList[i]
        if (sum==get):
                print(get,"= 1",end="")
                for i in range(len(myList)-2):
                        print(" +", myList[i+1], end="")
                print("")
        else:
                print(get, "is NOT perfect.")



