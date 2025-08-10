import sys
number=int(sys.stdin.readline().strip())
for i in range(number):
    check=int(sys.stdin.readline().strip())
    print("even") if check%2 == 0 else print("odd")
