# 슬라이딩 윈도우
# for문을 통해 시작점의 위치를 찾고
# 이중 for문을 통해 안에 해당 값이 존재하는지 탐색 
# 매번 슬라이딩을 통해 새로운 배열이 생성될 때마다 끝값만 확인해주는 방식으로 시간단축하기
import sys
line,sliding=map(int,sys.stdin.readline().split())
gene=list(sys.stdin.readline())
a,c,g,t=map(int,sys.stdin.readline().split())
count=0
#시작지점 위치
for i in range(0,(line-sliding)+1):
    if(i==0):
        ta=a
        tc=c
        tg=g
        tt=t
        for j in range(sliding):
            if gene[j]=='A':
                ta-=1
            elif gene[j]=='C':
                tc-=1
            elif gene[j]=='G':
                tg-=1
            elif gene[j]=='T':
                tt-=1
    else:
        if gene[i-1]=='A':
            ta+=1
        elif gene[i-1]=='C':
            tc+=1
        elif gene[i-1]=='G':
            tg+=1
        elif gene[i-1]=='T':
            tt+=1

        if gene[i+sliding-1]=='A':
            ta-=1
        elif gene[i+sliding-1]=='C':
            tc-=1
        elif gene[i+sliding-1]=='G':
            tg-=1
        elif gene[i+sliding-1]=='T':
            tt-=1
    if (ta<=0 and tc<=0 and tg<=0 and tt<=0):
        count+=1

print(count)

