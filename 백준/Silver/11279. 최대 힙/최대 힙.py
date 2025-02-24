import sys
num=int(sys.stdin.readline())
tree=[]

def maxHeap(start):
    # start는 index 번호
    # 트리 올라가는 함수
    # 재귀가 아닌 반복문으로 구현하기
    while (start>0):
        # 몫 연산인 //2 사용하기
        if (tree[((start-1)//2)]<tree[start]):
            floor=(start-1)//2
            parent=tree[start]
            tree[start]=tree[floor]
            tree[floor]=parent
            start=floor
        else:
            break


for i in range (num):
    get=int(sys.stdin.readline())
    # 0 입력하면
    if (get==0):
        if (tree):
            print(tree[0])
            tree[0]=tree[-1]
            tree.pop(-1)
            start=0
            #내려가는 함수
            while (2*start+1<len(tree)):
                largest=2*start+1
                if (2*start+2<len(tree)) and (tree[2*start+1]<tree[2*start+2]):
                    largest=2*start+2
                if (tree[largest]>tree[start]):
                    tree[largest],tree[start]=tree[start],tree[largest]
                    start=largest
                else:
                    break

    
        else:
            print(0)
    # 0이 아닌 자연수 입력
    else:
        tree.append(get)
        maxHeap(len(tree)-1)
    
