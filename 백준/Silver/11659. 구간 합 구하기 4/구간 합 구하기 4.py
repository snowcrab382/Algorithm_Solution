import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] #구간 합을 미리 저장해두는 리스트, 0은 index가 헷갈리지 않기 위해 추가

temp = 0
for i in arr:
    temp += i
    prefix_sum.append(temp)

for i in range(M):
    x,y = map(int,input().split())
    print(prefix_sum[y]-prefix_sum[x-1])