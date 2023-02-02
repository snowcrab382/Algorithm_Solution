import sys
input = sys.stdin.readline

M_zero = [0] * 20000001
M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    M_zero[i+10000000] = 1

N = int(input())
N_list = list(map(int,input().split()))
for j in N_list:
    print(M_zero[j+10000000], end=' ')