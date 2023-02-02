import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
N_index = [0] * 20000001

for i in N_list:
    N_index[i+10000000] += 1

M = int(input())
M_list = list(map(int,input().split()))

for j in M_list:
    print(N_index[j+10000000], end=' ')