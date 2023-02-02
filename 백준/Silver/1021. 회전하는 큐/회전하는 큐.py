from collections import deque


N, M = map(int,input().split())
a = list(map(int,input().split()))
N_list = deque(list(i for i in range(1,N+1)))
count = 0

for i in a:
    if N_list[0] == i:
        del N_list[0]
    else:
        if N_list.index(i) <= len(N_list) // 2:
            for j in range(N_list.index(i)):
                N_list.append(N_list.popleft())
                count += 1
            del N_list[0]

        else:
            for j in range(len(N_list)-N_list.index(i)):
                N_list.appendleft(N_list.pop())
                count += 1
            del N_list[0]
print(count)