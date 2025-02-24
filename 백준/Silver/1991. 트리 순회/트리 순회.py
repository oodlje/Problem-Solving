import sys
num=int(sys.stdin.readline())
tree={}
for i in range (num):
    get=list(sys.stdin.readline().split())
    tree[get[0]]=[get[1],get[2]]

def preorder(start):
    print(start,end="")
    if (tree[start][0]!="."):
        preorder(tree[start][0])
    if (tree[start][1]!="."):
        preorder(tree[start][1])

def inorder(start):
    if (tree[start][0]!="."):
        inorder(tree[start][0])
    print(start,end="")
    if (tree[start][1]!="."):
        inorder(tree[start][1])

def postorder(start):
    if (tree[start][0]!="."):
        postorder(tree[start][0])
    if (tree[start][1]!="."):
        postorder(tree[start][1])
    print(start,end="")


# print(tree)
preorder('A')
print('')
inorder('A')
print('')
postorder('A')
print('')