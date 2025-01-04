n=int(input())
init=n
n=n-1
key=1
while True&(init!=1):
    if n<=6*key:
        key=key+1
        break
    n=n-6*key
    key=key+1

print(key)