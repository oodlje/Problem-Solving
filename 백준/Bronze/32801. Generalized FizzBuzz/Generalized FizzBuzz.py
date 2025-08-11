import sys
n,a,b=map(int,sys.stdin.readline().split())
Fizz=0
Buzz=0
FizzBuzz=0
for i in range(n):
    if (i+1)%a==0 and (i+1)%b==0:
        FizzBuzz+=1
    elif (i+1)%a==0:
        Fizz+=1
    elif (i+1)%b==0:
        Buzz+=1
print(Fizz, Buzz, FizzBuzz)