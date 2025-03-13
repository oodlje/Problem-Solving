import sys
n=int(input())
star=[" "]*(2*n-1)
start_left=n-1
start_right=n-1
for i in range(n):
    star[start_left]="*"
    star[start_right]="*"
    start_left-=1
    start_right+=1
    print("".join(star).rstrip())
start_left+=1
start_right-=1
for i in range(n-1):
    star[start_left]=" "
    star[start_right]=" "
    start_left+=1
    start_right-=1
    print("".join(star).rstrip())