result = 0
N = int(input())
N_list = list(map(int,input().split()))
N_list.sort()
for i in range(len(N_list)):
    result += sum(N_list[:i+1])
print(result)