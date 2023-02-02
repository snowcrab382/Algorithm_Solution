N_yaknum = int(input())
N_yak = list(map(int,input().split()))
N_yak.sort()
print(N_yak[0] * N_yak[-1])